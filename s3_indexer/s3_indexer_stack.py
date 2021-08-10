#!/usr/bin/env python3

from aws_cdk import (
    core as cdk,
    aws_lambda as lmda,
    aws_dynamodb as ddb,
    aws_s3 as s3
)

from aws_cdk.aws_lambda_event_sources import S3EventSource


class S3IndexerStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, s3_bucket, ddb_table_name, ddb_billing_mode,
                 lambda_concurrency, ddb_read_capacity, ddb_write_capacity, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the S3 bucket for which we will be storing object information in DDB
        self._s3_bucket = s3.Bucket(
            self,
            s3_bucket,
            bucket_name=s3_bucket
        )

        # Create DynamoDB table for S3 index records
        self._ddb_table = ddb.Table(
            self,
            ddb_table_name,
            table_name=ddb_table_name,
            billing_mode=ddb.BillingMode(ddb_billing_mode),
            partition_key={'name': 's3_key', 'type': ddb.AttributeType.STRING},
            read_capacity=ddb_read_capacity,
            write_capacity=ddb_write_capacity
        )

        # Add GSI's for query patterns
        # Content Type
        self._ddb_table.add_global_secondary_index(
            read_capacity=ddb_read_capacity,
            write_capacity=ddb_write_capacity,
            index_name=f"{ddb_table_name}-content-type-index",
            partition_key=ddb.Attribute(name="content_type", type=ddb.AttributeType.STRING)
        )

        # Create the indexing Lambda function
        self._indexer_lambda = lmda.Function(
            self,
            'S3IndexHandler',
            runtime=lmda.Runtime.PYTHON_3_8,
            code=lmda.Code.asset('s3_indexer/lambda'),
            handler='indexer.handler',
            dead_letter_queue_enabled=True,
            reserved_concurrent_executions=lambda_concurrency,
            environment = {
                'DDB_TABLE_NAME': self._ddb_table.table_name,
                'S3_BUCKET_NAME': self._s3_bucket.bucket_name
            }
        )

        # Add an event source from our S3 bucket to trigger our Lambda function
        self._indexer_lambda.add_event_source(S3EventSource(self._s3_bucket,
                                                            events=[
                                                                s3.EventType.OBJECT_CREATED,
                                                                s3.EventType.OBJECT_REMOVED],
                                                            )
                                              )

        # Add permissions for Lambda to read/write from DynamoDB
        self._ddb_table.grant_read_write_data(self._indexer_lambda)
        self._ddb_table.grant_read_data(self._indexer_lambda)

        # Add permissions for Lambda to read S3 object information
        self._s3_bucket.grant_read(self._indexer_lambda)

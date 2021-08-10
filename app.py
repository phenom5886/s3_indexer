#!/usr/bin/env python3
import yaml
from aws_cdk import core as cdk
from s3_indexer.s3_indexer_stack import S3IndexerStack

# Load in our config
with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

# Ensure we have to DDB configuration we need
if data['dynamodb']['billing_mode'] == 'PROVISIONED':
    try:
        read_capacity = data['dynamodb']['read_capacity']
        write_capacity = data['dynamodb']['write_capacity']
    except KeyError:
        print('Error: You must provide DynamoDB read_capacity and write_capacity configurations '
              'when using Provisioned mode')
        exit(1)

elif data['dynamodb']['billing_mode'] == 'PAY_PER_REQUEST':
    pass

else:
    raise Exception('Invalid DynamoDB billing mode in configuration YAML')

# Load and synth the stack
app = cdk.App()

S3IndexerStack(app,
               "S3IndexerStack",
               s3_bucket=data['s3']['bucket_name'],
               ddb_table_name=data['dynamodb']['table_name'],
               ddb_billing_mode=data['dynamodb']['billing_mode'],
               ddb_read_capacity=data['dynamodb']['read_capacity'] if
               data['dynamodb']['billing_mode'] == 'PROVISIONED' else None,
               ddb_write_capacity=data['dynamodb']['write_capacity']
               if data['dynamodb']['billing_mode'] == 'PROVISIONED' else None,
               lambda_concurrency=data['lambda']['reserved_concurrency']
               )

app.synth()

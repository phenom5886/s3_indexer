#!/usr/bin/env python3
import yaml
from aws_cdk import core as cdk
from s3_indexer.s3_indexer_stack import S3IndexerStack

# Load in our config
with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

# Load and synth the stack
app = cdk.App()
S3IndexerStack(app,
               "S3IndexerStack",
               s3_bucket=data['s3_bucket_name'],
               ddb_table_name=data['dynamodb_table_name']
               )
app.synth()

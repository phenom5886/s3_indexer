#!/usr/bin/env python3
import boto3
import botocore
import os
import urllib


def add_ddb_record(table_name, key, metadata):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        table.put_item(
            Item={
                's3_key': key,
                'content_type': metadata[0],
                'e_tag': metadata[1],
                'size': metadata[2],
                'created_at': metadata[3].strftime("%Y-%m-%d %H:%M:%SZ")
            }
        )

    except botocore.exceptions.ClientError as e:
        raise


def del_ddb_record(table_name, key):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        table.delete_item(
            Key={
                's3_key': key
            }
        )

    except botocore.exceptions.ClientError as e:
        raise


def read_s3_metadata(s3_bucket, s3_key):

    s3 = boto3.resource('s3')
    object = s3.Object(s3_bucket, s3_key)

    type = object.content_type
    etag = object.e_tag
    size = object.content_length
    creation_date = object.last_modified

    return type, etag[1:-1], size, creation_date


def handler(event, context):
    # Read DDB table and S3 bucket from environment variable
    ddb_table_name = os.environ['DDB_TABLE_NAME']
    s3_bucket_name = os.environ['S3_BUCKET_NAME']

    # Read information about the S3 event
    event_s3_bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    event_type = event['Records'][0]['eventName']

    # Before we proceed, ensure the event is for correct bucket
    if event_s3_bucket_name == s3_bucket_name:
        pass
    else:
        print("Error: Event not for configured S3 bucket - please check configuration")
        exit(1)

    # S3 Put
    if event_type == 'ObjectCreated:Put':
        # Read additional metadata from S3
        object_info = read_s3_metadata(event_s3_bucket_name, key)

        # Put object in DynamoDB
        print(f"Info: Adding DynamoDB record for S3 key: {key}")
        add_ddb_record(ddb_table_name, key, object_info)

    # S3 Delete
    elif event_type == 'ObjectRemoved:Delete':
        # Remove item from DynamoDB
        print(f"Info: Deleting DynamoDB record for S3 key: {key}")
        del_ddb_record(ddb_table_name, key)

    else:
        print(f"Info: Event type {event_type} not catered for - exiting")
        exit(1)

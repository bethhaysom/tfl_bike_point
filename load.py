import os
import json
import logging
from dotenv import load_dotenv
import boto3

# Connecting to .env to pull through AWS keys
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# Connecting to .json files (test)
# test_file = '2026-11-11 16-35-19.json'
# file_location = 'data/2026-11-11 16-35-19.json'

# Dynamic file names + connections
data_dir = 'data'
file_location = os.listdir(data_dir)

# Configuring s3 credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Testing whether credentials we've set up work
# s3_client.upload_file(
#     file_location,        # local file location
#     AWS_BUCKET_NAME,      # name of bucket to upload to
#     test_file             # name for uploaded file
# )

# For each file in data_dir...
for file in file_location:
    to_upload = f'{data_dir}/{file}' # navigate to file location
    try:
        s3_client.upload_file(to_upload, AWS_BUCKET_NAME, file) # uploading each file
        os.remove(to_upload)
        print(f'File {file} successfully uploaded!')
    except Exception as e:
        print(f'Something went wrong... Error: {e}')
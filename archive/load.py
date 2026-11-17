import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
import boto3

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # capturing time for file name

# setting up files for logging
log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log' # .log is a filetype specifically for logs (similar to .txt)

# configuration of log file
logging.basicConfig(
    filename = log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO # ignore anything below INFO
)

logger = logging.getLogger() # at this point the log is set up but won't create files. need to add these bits in
logger.info('Logger was succesfully initialiser.')


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
        logger.info(f'file {file} successfully uploaded!')
    except Exception as e:
        print(f'Something went wrong... Error: {e}')
        logger.error(f'something went wrong... error: {e}')


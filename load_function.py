import os
import logging
from dotenv import load_dotenv
import boto3

logger = logging.getLogger(__name__) # attributes logs in function to their own logs

def load_to_s3(data_dir: str, AWS_ACCESS_KEY: str, AWS_SECRET_ACCESS_KEY: str, AWS_BUCKET_NAME: str):
    """Function to upload files to S3

    Args:
        data_dir (str): filepath to find saved data
        AWS_ACCESS_KEY (str): key value (get value from .env)
        AWS_SECRET_ACCESS_KEY (str): secret key value (get value from .env)
        AWS_BUCKET_NAME (str): S3 bucket name (get value from .env)
    """

    file_location = os.listdir(data_dir)

    # Configuring s3 credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

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

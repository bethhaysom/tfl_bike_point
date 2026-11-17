import os
import logging
from datetime import datetime
from modules.extract_function import extract_to_json
from modules.load_function import load_to_s3
from modules.logging_function import logging_config
from dotenv import load_dotenv

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # capturing time for file name

# setting up files for logging
log_dir = 'logs'

logging_config(log_dir, timestamp)

logger = logging.getLogger() # at this point the log is set up but won't create files. need to add these bits in
logger.info('Logger was succesfully initialised.')

# configure params for function
url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_result = extract_to_json(url, data_dir, timestamp, max_attempts=3, delay=30)

if extract_result:
    # Connecting to .env to pull through AWS keys
    load_dotenv()

    # Get keys
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

    # run load to s3
    load_result = load_to_s3(data_dir, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME)

else: 
    logger.info('Extract saved no data, nothing to attempt to upload so aborted.')
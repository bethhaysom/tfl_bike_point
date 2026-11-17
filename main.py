from datetime import datetime
from modules.extract_function import extract_to_json
import logging
import os

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # capturing time for file name

# setting up files for logging
log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
log_filename = f'{log_dir}/extract_{timestamp}.log' 

# configuration of log file
logging.basicConfig(
    filename = log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO # ignore anything below INFO
)

logger = logging.getLogger() # at this point the log is set up but won't create files. need to add these bits in
logger.info('Logger was succesfully initialiser.')


# configure params for function
url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_result = extract_to_json(url, data_dir, timestamp, max_attempts=3, delay=30)

print(extract_result)
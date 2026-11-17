import os
import json
import time
import logging
import requests

logger = logging.getLogger(__name__) # attributes logs in function to their own logs

def extract_to_json(url: str, data_dir: str, timestamp: str, max_attempts: int, delay: int): 
    """Function to extract JSON files from a URL and save to a destination

    Args:
        url (str): URL to pull data from API
        data_dir (str): filepath to save data to
        timestamp (str): timestamp to append to filename
        max_attmepts (int): number of times to retry API calls
        delay (int): how long to wait between call attempts
    """

    os.makedirs(data_dir,exist_ok=True) # make directory if not exist
    filename = f'{data_dir}/{timestamp}.json' # build out the file name
    attempt = 1

    while attempt <= max_attempts:
        # calling API
        response = requests.get(url) # fetching api
        status_code = response.status_code

        # handling status code responses
        if 200 <= status_code < 300:
            try: # using try/except to catch any errors that might occur when saving the data
                data = response.json() # turns response from api into json 

                with open(filename, 'w') as file: # w=write so will open and write file (this is where file is created)
                    json.dump(data, file)

                print(f'file {filename} saved successfully - yay!')
                logger.info(f'file {filename} saved successfully - yay!')

                # flag that data was saved successfully
                return True
            
            except Exception as e:
                print(f'An error occurred when saving the JSON: {e}')
                logger.error(f'An error occurred when saving the JSON: {e}')

            break 

        elif 300 <= status_code < 500:
            print(f'API call failed, status code {status_code}')
            logger.error(f'API call failed, status code {status_code}')
            break

        else:
            if attempt == max_attempts:
                print(f'Max number of attempts reached. Status code {status_code}. Investigate further pls.')
                logging.warning(f'Max number of attempts reached. Status code {status_code}. Investigate further pls.')
            else:
                print(f'Attempt {attempt} failed, status code {status_code}. Trying again...')
                logger.error
            
            attempt += 1
            time.sleep(delay)

    # return statement if unsuccessful
    return False
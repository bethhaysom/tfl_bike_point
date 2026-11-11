import os
import json
import time
from datetime import datetime
import requests

# naming file for output
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # capturing time for file name
data_dir = 'data' # variable to repeat for data folder
os.makedirs(data_dir,exist_ok=True) # directions to create data folder
filename = f'{data_dir}/{timestamp}.json' # naming convention for data when we save (data_dir will navigate to right folder with timestamp as file name)

url = 'https://api.tfl.gov.uk/BikePoint/' # defining API url

# defining params for while loop
attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    # calling API
    response = requests.get(url) # fetching api
    status_code = response.status_code

    # handling status code responses
    if 200 <= status_code < 300:
        data = response.json() # turns response from api into json 

        with open(filename, 'w') as file: # w=write so will open and write file (this is where file is created)
            json.dump(data, file)

        print(f'file {filename} saved successfully - yay!')
        break 

    elif 300 <= status_code < 500:
        print(f'API call failed, status code {status_code}')
        break

    else:
        if attempt == max_attempts:
            print(f'Max number of attempts reached. Status code {status_code}. Investigate further pls.')
        else:
            print(f'Attempt {attempt} failed, status code {status_code}. Trying again...')
        
        attempt += 1
        time.sleep(30) # this makes it wait for 30 seconds before rerunning



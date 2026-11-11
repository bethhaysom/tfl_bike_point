# Bike Point Project Pipeline
---
A data pipeline from the TFL Bike Point API using Python to extract the API.

**Use Case:** Looking at Bike Point availability over time, ie 'Popular Times', with a goal of refreshes every 5 mins

**The API:** The Bike Point data is a snapshot of how the TFL Bike Points look at a given moment, including total capacity, how many regular vs electric bikes are docked and how many available spaces there are. It also includes geographic points for each bike point.

---
## Python Script: Calling the API
A python script set up to call the API, saving the data in `.json` format when this is successful, and act as needed when responses signify that this hasn't worked. 

<details>
<summary>Breakdown of Python Script</summary>

#### Setting up
First the script lists all of the required packages for `import` and sets the `timestamp` variable, which will be referenced later for file names.
```python
import os
import json
import time
import logging
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
```

#### File and variable configuration
Next the script outlines files for outputs and variables that will be used to call the API

This starts with the Log file configuration, so that any info / warnings / errors are captured when the script runs.
```python
# configuration of log file
logging.basicConfig(
    filename = log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO # ignore anything below INFO
)

logger = logging.getLogger() 
logger.info('Logger was succesfully initialiser.')
```
Then the output file is configured, so that every time the API is run, it is saved as a `.json` file with the `timestamp` as the file name (this is so it can be used later for analysis over time).
``` python
# naming file for output
data_dir = 'data' 
os.makedirs(data_dir,exist_ok=True) 
filename = f'{data_dir}/{timestamp}.json' 
```
Finally, variables are defined to be used later, including the url for the API.
``` python
url = 'https://api.tfl.gov.uk/BikePoint/' # defining API url

# defining params for while loop
attempt = 1
max_attempts = 3
```

#### The While Loop
To call the API, a `while` loop is set up, so that the script will stop running if the attempts exceed the specified maximum. 
``` python
while attempt <= max_attempts:
    # calling API
    response = requests.get(url) 
    status_code = response.status_code
```
Once we've called the API, an `if` statement is used within the `while` loop so the status code responses are handled appropriately. 

Option 1 - if the request has been received successfully:
``` python
    if 200 <= status_code < 300: # request was received successfully
        try:
            data = response.json() 

            with open(filename, 'w') as file: 
                json.dump(data, file)

            print(f'file {filename} saved successfully - yay!')
            logger.info(f'file {filename} saved successfully - yay!')
        except Exception as e:
            print(f'An error occurred when saving the JSON: {e}')
            logger.error(f'An error occurred when saving the JSON: {e}')

        break 
```
Option 2 - if the status code means the API can't be run:
``` python
    elif 300 <= status_code < 500: # issue that means the api can't be run
        print(f'API call failed, status code {status_code}')
        logger.error(f'API call failed, status code {status_code}')
        break
```
Option 3 - if it hasn't been successful but can be attempted again:
``` python
    else:
        if attempt == max_attempts:
            print(f'Max number of attempts reached. Status code {status_code}. Investigate further pls.')
            logging.warning(f'Max number of attempts reached. Status code {status_code}. Investigate further pls.')
        else: 
            print(f'Attempt {attempt} failed, status code {status_code}. Trying again...')
            logger.error
        
        attempt += 1
        time.sleep(30)
```
</details>















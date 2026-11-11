import os
import json
from datetime import datetime
import requests

# naming file for output
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # capturing time for file name
data_dir = 'data' # variable to repeat for data folder
os.makedirs(data_dir,exist_ok=True) # directions to create data folder
filename = f'{data_dir}/{timestamp}.json' # naming convention for data when we save (data_dir will navigate to right folder with timestamp as file name)

url = 'https://api.tfl.gov.uk/BikePoint/' 

response = requests.get(url) # fetching api

data = response.json() # turns response from api into json 

with open(filename, 'w') as file: # w=write so will open and write file (this is where file is created)
    json.dump(data, file)
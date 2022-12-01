import os, json

from app.utils.Counter import Counter

# Function to read the content of a JSON file.
def read_json(file):    
    current_directory = os.getcwd()
    with open(f'./{current_directory}/data/{file}', 'r') as f:
        data = json.load(f)
    
    return data


restaurants_cfg = read_json('restaurants.json').get('restaurants')

restaurants = dict()
order_indexer = Counter()

HOST_NAME = os.getenv('HOST_NAME')
RESTAURANT_ID = os.getenv('RESTAURANT_ID')

FOOD_ORDERING_PORT = os.getenv('FOOD_ORDERING_PORT')
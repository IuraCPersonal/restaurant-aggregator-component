import json
import time

from app import app
from pprint import pprint
from flask import request

from app.modules import *
from app.helpers.Print import Print
from app.Restaurant import Restaurant


# Create the 'register' endpoint.
@app.route('/register', methods=['POST'])
def register():
    content = request.get_json()
    restaurant = Restaurant(content)
    restaurants_list[restaurant.restaurant_id] = restaurant

    Print.welcome(restaurant.name)

    return json.dumps({'success': True}), 200

# Create the 'menu' endpoint.
@app.route('/menu', methods=['GET'])
def menu():
    content = {
        'restaurants': len(restaurants_list),
        'restaurants_data': [{
            'name': el.name,
            'menu_items': el.menu_items,
            'menu': el.menu,
            'rating': None
        } for el in restaurants_list.values()]
    }

    return content

# Create the 'order' endpoint.
@app.route('/order', methods=['POST'])
def order():
    content = request.get_json()

    Print.order_recieved(content)

    response = {
        'order_id': None,
        'orders': [{
            'restaurant_id': el['restaurant_id'],
            'restaurant_address': None,
            'order_id': None,
            'estimated_waiting_time': None,
            'created_time': None,
            'registered_time': time.time()
        } for el in content['orders']]
    }

    return response

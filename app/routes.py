import json, time

from app import app
from flask import request
from pprint import pprint

from app.modules import *
from app.utils.Print import Print
from app.Restaurant import Restaurant
from app.utils.OrderManager import OrderManager


# Create the 'register' endpoint.
@app.route('/register', methods=['POST'])
def register():
    content = request.get_json()

    restaurant = Restaurant(content)
    restaurants[restaurant.restaurant_id] = restaurant

    # Welcome to Business 💸
    Print.welcome(restaurant.name)

    return json.dumps({'success': True}), 200


# Create the 'menu' endpoint.
@app.route('/menu', methods=['GET'])
def menu():
    content = {
        'restaurants': len(restaurants),
        'restaurants_data': [{
            'id': el.restaurant_id,
            'name': el.name,
            'menu_items': el.menu_items,
            'menu': el.menu,
            'rating': None
        } for el in restaurants.values()]
    }

    return content


# Create the 'order' endpoint.
@app.route('/order', methods=['POST'])
def order():
    content = request.get_json()

    OrderManager.distribute(content)
    Print.order_recieved(content)

    response = {
        "order_id": order_indexer.get_index(),
        "orders": [{
            "restaurant_id": el['restaurant_id'],
            "restaurant_address": restaurants.get(index+1).address,
            "order_id": index+1,
            "estimated_waiting_time": None,
            "created_time": el['created_time'],
            "registered_time": time.time()
            } for index, el in enumerate(content["orders"])
        ]}

    return response
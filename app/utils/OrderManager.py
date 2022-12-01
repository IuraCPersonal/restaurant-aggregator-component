import time
import requests

from app.modules import restaurants_cfg

class OrderManager:
    @staticmethod
    def distribute(content):
        client = content.get('client_id')
        orders = content.get('orders')

        for order in orders:
            restaurant_id = order.get('restaurant_id')
            restaurant_port = restaurants_cfg.get(str(restaurant_id)).get('dining-port')

            time.sleep(1)

            _ = requests.post(
                url=f'http://dining-hall-{restaurant_id}:{restaurant_port}/v2/order',
                json=order
            )

            time.sleep(1)
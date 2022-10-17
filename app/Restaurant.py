class Restaurant:
    def __init__(self, content):
        self.restaurant_id = content['restaurant_id']
        self.name = content['name']
        self.address = content['address']
        self.menu_items = content['menu_items']
        self.menu = content['menu']
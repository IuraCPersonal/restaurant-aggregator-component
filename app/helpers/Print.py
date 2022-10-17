import threading, json

from pprint import pprint
from colorama import init, Fore, Back, Style


class Print:
    __lock = threading.Lock()

    @staticmethod
    def welcome(restaurant_name):
        with Print.__lock:
            print(f'[{Fore.YELLOW}RA{Style.RESET_ALL}] Restaurant ({Fore.GREEN}{restaurant_name}{Style.RESET_ALL}) is now OPEN.')

    @staticmethod
    def order_recieved(content):
        with Print.__lock:
            print(f'[{Fore.YELLOW}RA{Style.RESET_ALL}] Order recieved...')
            print(json.dumps(content, sort_keys=True, indent=4))

    @staticmethod
    def log(text):
        with Print.__lock:
            print(f'[{Fore.YELLOW}RA{Style.RESET_ALL}] {text}')
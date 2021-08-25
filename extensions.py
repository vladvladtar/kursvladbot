import requests
import json
from config import keys

class APIException(Exception):   #исключения
    pass

class CryptoCoverter: #общий обработчик ошибок ввода пользователем
    @classmethod
    def get_price(quote, base, amount):
        pass

    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неудалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base


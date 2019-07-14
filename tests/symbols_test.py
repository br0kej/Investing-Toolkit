from investingtoolkit.symbols import Symbols
from datatest import validate
import json

x = Symbols('MSFT', apiKey='demo')


def test_symbol_value():
    assert x.symbol == 'MSFT'


def test_base_url_value():
    assert x.baseUrl == 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='


def test_set_url_value():
    x.set_url()
    assert x.url == 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=demo'


def test_get_response_type():
    x.get_response()
    test_response = x.response
    validate(test_response, dict)


def test_get_current_price_type():
    x.get_current_price()
    test_current_price = x.current_price
    validate(test_current_price, float)


def test_get_high_type():
    x.get_high()
    test_high = x.high
    validate(test_high, float)


def test_get_low_type():
    x.get_low()
    test_low = x.low
    validate(test_low, float)


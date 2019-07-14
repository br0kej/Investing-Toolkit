from investingtoolkit.apikeys import ApiKeys
from datatest import validate
import pytest

x = ApiKeys(api='TestApi')


def test_api_value():
    assert x.api_name == "TestApi"


def test_directory_name_value():
    assert x.directory_name == "keys/"


def test_check_keys_directory_no_check():
    assert x.directory_exists is True


def test_check_keys_directory_with_check():
    x.check_keys_directory()
    assert x.directory_exists is False


def test_check_keys_directory_once_made():
    x.check_keys_directory()
    x.make_keys_directory()
    x.check_keys_directory()
    assert x.directory_exists is True


def test_input_api_key_value():
    x.input_api_key()
    assert x.pickled_api_key is not None

from investingtoolkit.apikeys import ApiKeys
import os

x = ApiKeys('test_keys', api='TestApi')

if os.path.isdir('test_keys'):
    os.rmdir('test_keys')

def test_api_value():
    assert x.api_name == "TestApi"


def test_directory_name_value():
    assert x.directory_name == "test_keys"


def test_check_keys_directory_no_check():
    assert x.directory_exists is True


def test_check_keys_directory_with_check():
    x.check_keys_directory()
    assert x.directory_exists is False


def test_pickled_api_key():
    assert x.pickled_api_key is None


def test_input_api_key_value(monkeypatch):
    os.mkdir(x.directory_name)
    key = "apikey123456"
    monkeypatch.setattr('builtins.input', lambda prompt: key)
    x.input_api_key()
    assert input('Please enter your API Key for TestApi: ' == 'apikey123456')

def test_remove_keys_directory():
    os.remove('./test_keys/TestApi.p')
    os.rmdir(x.directory_name)


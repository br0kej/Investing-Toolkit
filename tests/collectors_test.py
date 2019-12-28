from investingtoolkit.collectors.collectors import Collector
import os
import datetime

x = Collector("https://en.wikipedia.org/wiki/FTSE_250_Index", "test_output")

def test_timestamp_format():
    assert datetime.datetime.strptime(x.timestamp, '%Y-%m-%d')

def test_target_url():
    assert x.target_url == "https://en.wikipedia.org/wiki/FTSE_250_Index"

def test_output_directory():
    assert x.output_directory == 'test_output'

def test_html_element():
    assert x.html_element == "table"

def test_check_output_directory():
    assert os.path.exists(x.output_directory)

#TODO: Create test using Responses Library - https://pypi.org/project/responses/
def test_make_requests():
    pass

#TODO: Look into how to create test this function
def test_parse_html():
    pass

#TODO: Creat test for  this function
def test_extract_target_html_object():
    pass

def test_output_to_json():
    results = [{'test1':'123'}]
    x.output_to_json('test', results)
    assert os.path.exists('test_output/test' + x.timestamp + '.json')

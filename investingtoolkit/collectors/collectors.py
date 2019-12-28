import os
import datetime
import json
import requests
from bs4 import BeautifulSoup

class Collector:

    def __init__(self, target_url, html_element='table', output_directory):
        self.results = list()
        self.timestamp = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
        self.target_url = target_url
        self.html_element = html_element
        self.output_directory = output_directory
        self.check_output_directory()
        self.make_request()
        self.parse_html()
        self.extract_target_html_object()

    def check_output_directory(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def make_request(self):
        self.request_response = requests.get(self.target_url)
    
    def parse_html(self):
        self.parsed_html = BeautifulSoup(self.request_response.content, features="html.parser")

    def extract_target_html_object(self):
        self.extracted_html_object = self.parsed_html(self.html_element)

    def output_to_json(self, output_directory, filename, results):
        output_path = output_directory + filename + str(self.timestamp) + '.json'
        with open(output_path) as file:
            json.dump(results, file)

TODO: Implement
class FTSE100(Collector):
    pass

#    def iterate_extracted_html_object(self, element_position, sub_element):
#        for row in self.extract_target_html_object[element_position].findall(sub_element)[1:-1]:

class FTSE250(Collector):
    pass
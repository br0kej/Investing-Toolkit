import os
import datetime
import json
import requests
from bs4 import BeautifulSoup

class Collector:

    def __init__(self, target_url, output_directory):
        self.results = list()
        self.timestamp = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
        self.target_url = target_url
        self.output_directory = output_directory
        self.primary_element = None
        self.check_output_directory()
        self.make_request()
        self.parse_html()

    def check_output_directory(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def make_request(self):
        self.request_response = requests.get(self.target_url)
    
    def parse_html(self):
        self.parsed_html = BeautifulSoup(self.request_response.content, features="html.parser")

    def extract_target_html_object(self):
        self.extracted_html_object = self.parsed_html.findAll(self.primary_element)

    def output_to_json(self, filename, results):
        output_path = self.output_directory + '/' + filename + str(self.timestamp) + '.json'
        with open(output_path, 'w') as file:
            json.dump(results, file)

class FTSE100(Collector):

    def __init__(self, target_url, output_directory):
        Collector.__init__(self, target_url, output_directory)
        self.primary_element = 'table'
        self.primary_element_position = 2
        self.secondary_element = 'tr'
        self.tertiary_element = 'td'

    def generate_output(self):
        self.extract_target_html_object()
        target_html = self.extracted_html_object[self.primary_element_position].findAll(self.secondary_element)[1:-1]
        for row in target_html:
            col = row.findAll(self.tertiary_element)
            self.results.append({'name': str(col[0].text),
                                'symbol': str(col[1].text.strip())})

class FTSE250(Collector):

    def __init__(self, target_url, output_directory):
        Collector.__init__(self, target_url, output_directory)
        self.primary_element = 'table'
        self.primary_element_position = 1
        self.secondary_element = 'tr'
        self.tertiary_element = 'td'

    def generate_output(self):
        self.extract_target_html_object()
        target_html = self.extracted_html_object[self.primary_element_position].findAll(self.secondary_element)[1:-1]
        for row in target_html:
            col = row.findAll(self.tertiary_element)
            self.results.append({'name': str(col[0].text),
                                'symbol': str(col[1].text.strip())})
import os
import pickle


class ApiKeys:
    def __init__(self, api=''):
        self.api_name = api
        self.directory_name = "keys/"
        self.directory_exists = True
        self.pickled_api_key = None
        self.api_key_path = None
        self.loaded_api_key = None

    def check_keys_directory(self):
        if not os.path.isdir(self.directory_name):
            self.directory_exists = False

    def make_keys_directory(self):
        if self.directory_exists is False:
            os.mkdir(self.directory_name)

    def input_api_key(self):
        api_key = input('Please enter API Key for ' + self.api_name + ': ')
        self.pickled_api_key = pickle.dump(api_key, open(self.directory_name + self.api_name + ".p", "wb"))

    def get_api_key_path(self):
        self.api_key_path = self.directory_name + self.api_name + ".p"

    def load_api_key(self):
        self.loaded_api_key = pickle.load(open(self.api_key_path, "rb"))

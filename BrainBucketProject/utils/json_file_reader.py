import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_email(self, section_name):
        if 'email' not in self.data.keys():
            raise Exception("Email option is not present in the config file")
        return self.data['email']

    def get_password(self, section_name):
        if 'password' not in self.data.keys():
            raise Exception("Password option is not present in the config file")
        return self.data['password']

    def get_browser_width(self):
        if 'width' not in self.data.keys():
            raise Exception("Width option is not present in the config file")
        return self.data['width']

    def get_browser_length(self):
        if 'length' not in self.data.keys():
            raise Exception("Length option is not present in the config file")
        return self.data['length']

    def get_user1_email(self):
        if 'email' not in self.data.keys():
            raise Exception("email option is not found in user1 section")
        return self.data['email']

    def get_user1_password(self):
        if 'password' not in self.data.keys():
            raise Exception("password option is not found in iser1 section")
        return self.data['password']

    def get_url(self):
        if 'url' not in self.data.keys():
            raise Exception("URL option is not present in the config file")
        return self.data['url']

    def get_username(self):
        if 'username' not in self.data.keys():
            raise Exception("username option is not found in BrowserStack section")
        return self.data['username']

    def get_accesskey(self):
        if 'accesskey' not in self.data.keys():
            raise Exception("Access key option is not found in BrowserStack section")
        return self.data['accesskey']
from configparser import ConfigParser

class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self):
        value = self.data.get('environment', 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self):
        value = self.data.get('environment', 'wait', fallback=None)
        if value is None:
            raise Exception("Wait_time option is not present in the config file")
        return int(value)

    def get_email(self):
        value = self.data.get('user1', 'email', fallback=None)
        if value is None:
            raise Exception("Email option is not present in the config file")
        return value

    def get_password(self):
        value = self.data.get('user1', 'password', fallback=None)
        if value is None:
            raise Exception("Email option is not present in the config file")
        return value

    def get_browser_width(self):
        value = self.data.get('environment', 'width', fallback=None)
        if value is None:
            raise Exception("Width option is not present in the config file")
        return value

    def get_browser_length(self):
        value = self.data.get('environment', 'length', fallback=None)
        if value is None:
            raise Exception("Length option is not present in the config file")
        return value

    def get_user1_email(self):
        value = self.data.get('user1', "email", fallback=None)
        if value is None:
            raise Exception("email option is not found in user1 section")
        return value

    def get_user1_password(self):
        value = self.data.get('user1', "password", fallback=None)
        if value is None:
            raise Exception("password option is not found in iser1 section")
        return value

    def get_url(self):
        value = self.data.get('environment', 'url', fallback=None)
        if value is None:
            raise Exception("URL option is not found in environment section")
        return value

    def get_username(self):
        value = self.data.get('browserstack', 'username', fallback=None)
        if value is None:
            raise Exception('Username option is not found in browserstack section')
        return value

    def get_accesskey(self):
        value = self.data.get('browserstack', 'accesskey', fallback=None)
        if value is None:
            raise Exception('Access Key option is not found in browserstack section')
        return value


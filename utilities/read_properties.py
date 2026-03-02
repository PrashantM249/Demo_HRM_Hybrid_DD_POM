import configparser
import os


config = configparser.RawConfigParser()

# Get the absolute path to the config file
config_path = os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini')
config.read(config_path)


class Read_Config():
    @staticmethod
    def get_login_page_url():
        url = config.get("admin login info","admin_page_url")
        return url

    @staticmethod
    def get_username():
        username = config.get("admin login info","username")
        return username


    @staticmethod
    def get_password():
        password = config.get("admin login info","password")
        return password

    @staticmethod
    def get_admin_invalidusername():
        invalidusername = config.get("admin login info","invalid_username")
        return invalidusername

    @staticmethod
    def get_admin_invalidpassword():
        invalidpassword = config.get("admin login info","invalid_password")
        return invalidpassword


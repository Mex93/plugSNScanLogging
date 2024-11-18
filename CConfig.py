import configparser
from os import path

MAX_PALLET_PLACES = 100


class ConfigError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class CConfig:
    def __init__(self):
        self.__LAST_VENDOR_NAME = ''
        self.__LAST_DEVICE_NAME = ''
        self.__LAST_LOT_COUNT = ''

        self.__config = configparser.ConfigParser()
        self.__config.add_section('program')

    def set_default_for_values(self):
        self.__LAST_VENDOR_NAME = ''
        self.__LAST_DEVICE_NAME = ''
        self.__LAST_LOT_COUNT = ''

    def get_config(self):
        self.__config.read('config.ini', encoding="utf-8")

        self.__LAST_VENDOR_NAME = self.__config.get('program', 'LAST_VENDOR')
        self.__LAST_DEVICE_NAME = self.__config.get('program', 'LAST_DNAME')
        self.__LAST_LOT_COUNT = self.__config.get('program', 'LAST_LOT_COUNT')

    @staticmethod
    def is_config_created():
        if path.isfile('config.ini') is True:
            return True
        return False

    def create_config(self):
        with open('config.ini', 'w') as config_file:
            self.__config.set('program', 'LAST_VENDOR', '')
            self.__config.set('program', 'LAST_DNAME', '')
            self.__config.set('program', 'LAST_LOT_COUNT', '')

            self.set_default_for_values()
            self.__config.write(config_file)

    def get_lvendor(self) -> str: return self.__LAST_VENDOR_NAME

    def get_ldevice(self) -> str: return self.__LAST_DEVICE_NAME

    def get_lcount(self) -> str: return self.__LAST_LOT_COUNT

    def set_lvender(self, text: str):
        with open('config.ini', 'w') as config_file:
            self.__config.set('program', 'LAST_VENDOR', text)
            self.__config.write(config_file)

    def set_ldevice(self, text: str):
        with open('config.ini', 'w') as config_file:
            self.__config.set('program', 'LAST_DNAME', text)
            self.__config.write(config_file)

    def set_lcount(self, text: str):
        with open('config.ini', 'w') as config_file:
            self.__config.set('program', 'LAST_LOT_COUNT', text)
            self.__config.write(config_file)

    def save_config(self):
        if self.is_config_created() is False:
            with open('config.ini', 'w') as config_file:
                self.__config.write(config_file)

    def load_data(self) -> None:
        if self.is_config_created():
            self.get_config()
        else:
            self.create_config()
            self.get_config()


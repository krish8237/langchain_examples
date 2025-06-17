import yaml

class ConfigReader:

    def __init__(self, config_file):
        self.__config_file = config_file
        self.__read_config()

    def __read_config(self):
        with open(self.__config_file,"r") as config_reader:
            self.__config_data = yaml.safe_load(config_reader.read())

    def get_config_value(self, key):
        return self.__config_data[key]
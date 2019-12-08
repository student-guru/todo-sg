""" This module contains the Config class. """
import os.path
import yaml

class Config():
    """ Add basic config class """

    def __init__(self):
        """ Class constructor """
        if os.path.isfile('config/config.yaml'):
            config_dict = yaml.safe_load(open('config/config.yaml', 'r'))
            self.backend_ip = config_dict['development']['backend']['ip']
            self.backend_port = config_dict['development']['backend']['port']
            self.debug_mode = config_dict['development']['backend']['debug_mode']
        else:
            print('No config yaml file found.')
            exit(1)
    
    def get_backend_socket(self):
        "Return the backend socket."
        return ':'.join([self.backend_ip, str(self.backend_port)])

CONFIGURATION = Config()

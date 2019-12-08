""" This module contains the Config class. """
import os.path
import yaml

class Config():
    """ Add basic config class """

    def __init__(self):
        """ Class constructor """
        if os.path.isfile('config/config.yaml'):
            config_dict = yaml.safe_load(open('config/config.yaml', 'r'))
        else:
            print('No config yaml file found.')
            exit(1)

CONFIGURATION = Config()

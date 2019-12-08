""" This module contains the Config class. """
import os.path
import yaml
import redis
import logging

class Config():
    """ Add basic config class """

    def __init__(self):
        """ Class constructor """
        if os.path.isfile('config/config.yaml'):
            config_dict = yaml.safe_load(open('config/config.yaml', 'r'))
            self.backend_ip = config_dict['development']['backend']['ip']
            self.backend_port = config_dict['development']['backend']['port']
            self.debug_mode = config_dict['development']['backend']['debug_mode']
            self.db_ip = config_dict['development']['backend']['db_ip']
            self.logging_level = config_dict['development']['logging']['level']
            self.logging_format = config_dict['development']['logging']['format']
            self.logging_datefmt = config_dict['development']['logging']['datefmt']
        else:
            print('No config yaml file found.')
            exit(1)
    
    def get_backend_socket(self):
        """Return the backend socket."""
        return ':'.join([self.backend_ip, str(self.backend_port)])

    def get_db(self):
        """ Return Db object """
        redis_con = redis.Redis(host=self.db_ip, decode_responses=True, db=1)
        return redis_con
    
    def get_logger(self, module_name):
        """ Set up logging and return logger name """
        LOGGER = logging.getLogger(f'app:{module_name}')
        logging.basicConfig(format=self.logging_format, level=self.logging_level,
                            datefmt=self.logging_datefmt)
        
        return LOGGER

CONFIGURATION = Config()

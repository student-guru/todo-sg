""" This is the main application module. """
from flask_cors import CORS
from flask import Flask 

from config import CONFIGURATION

APP = Flask(__name__)

CORS(APP)
# APP.secret_key = CONFIGURATION.secret_key
APP.config['SERVER_NAME'] = CONFIGURATION.get_backend_socket()

if __name__ == '__main__':
    APP.run(debug=CONFIGURATION.debug_mode,
            host=CONFIGURATION.backend_ip, port=CONFIGURATION.backend_port)

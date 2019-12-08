""" This is the main application module. """

# Python libs.
from flask_cors import CORS
from src import APP

# Porject files.
from src.modules import API
from config import CONFIGURATION

CORS(APP)
# APP.secret_key = CONFIGURATION.secret_key
APP.config['SERVER_NAME'] = CONFIGURATION.get_backend_socket()
API.init_app(APP)

if __name__ == '__main__':
    APP.run(debug=CONFIGURATION.debug_mode,
            host=CONFIGURATION.backend_ip, port=CONFIGURATION.backend_port)

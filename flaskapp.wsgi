import sys
import logging
import os

# Add the application directory to the Python path
sys.path.insert(0, '/home/ubuntu/flask_app')

# Set the Flask application
from app import app as application

# Logging (optional)
logging.basicConfig(stream=sys.stderr)
sys.stderr = open('/var/log/apache2/flaskapp.log', 'a+')



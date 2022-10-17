import sys
import logging

from flask import Flask

from app.modules import *

# Disable Flask console messages.
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

# Setup Flask and other dependencies.
app = Flask(__name__)

from app import routes

app.run(host=HOST_NAME, port=AGGREGATOR_PORT, debug=False, use_reloader=False)
import logging
from logging.config import dictConfig
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
# Set the app's logger level to "warning"
# and any other necessary changes
app.logger.setLevel(logging.WARNING)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)

import FlaskExercise.views
from flask import Flask
from flask_socketio import SocketIO
from flask_mongoengine import MongoEngine
from flask_migrate import Migrate
from flask_cors import CORS
from flask_babel import Babel
from flask_bootstrap import Bootstrap
import os
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
db = MongoEngine(app)
app.config["MONGODB_HOST"] = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false"
socketio = SocketIO(app, async_mode="eventlet")
CORS(app)
Bootstrap(app)

from .util import (
    construct_scenario,
    config_broker,
    connection_broker,
)
from .controller import main_controller

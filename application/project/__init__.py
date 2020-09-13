from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import make_config
from flask_cors import CORS
from flask_babel import Babel
from flask_bootstrap import Bootstrap
import os
import eventlet
eventlet.monkey_patch()

try:
    os.remove("storage.db")
except Exception:
    pass

app = Flask(__name__)
make_config(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, async_mode='eventlet')
babel = Babel(app)
CORS(app)
Bootstrap(app)


from .util import (
    construct_scenario,
    config_broker,
    connection_broker,
)
from .controller import main_controller
#from .model import {{device}}

db.create_all()

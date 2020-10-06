import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO
from flask_mongoengine import MongoEngine


app = Flask(__name__)
socketio = SocketIO(app, async_mode="eventlet")
app.config['MONGODB_SETTINGS'] = {
    'db': 'devices',
    'host': 'mongodb://localhost/devices'
}
db = MongoEngine(app)


from .util import (
    components_config,
    config_broker,
    connection_broker,
    start_subscribers,
)
from .controller import main_controller
from .model import (
    {% for device in devices %}
    {{device}}_model,{% endfor %}
)
from .service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
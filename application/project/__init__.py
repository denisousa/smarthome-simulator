import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO
from flask_mongoengine import MongoEngine
from pymongo import MongoClient


def drop_database(database_name):
    mongo_client = MongoClient('mongodb://localhost:27017')
    database_list = mongo_client.database_names()
    mongo_client.drop_database(database_name)
    mongo_client.close()


drop_database('devices')
app = Flask(__name__)
socketio = SocketIO(app, async_mode="eventlet")
app.config['MONGODB_SETTINGS'] = {
    'db': 'devices',
    'host': 'mongodb://localhost/devices'
}
db = MongoEngine(app)


from .util import (
    components_config,
)

from .controller.receive_data import receive_data
from .controller.interface import interface
from .controller.actuator import (
    {% for device in device_actuator %}
    {{device[0].split("|")[0]}},{% endfor %}    
)
from .controller import connect
from .controller import disconnect

# from .controller.disconnect_middleware import (
#     {% for device in devices %}
#     {{device}},{% endfor %}
# )

from .model import (
    {% for device in devices %}
    {{device}}_model,{% endfor %}
)

from .service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
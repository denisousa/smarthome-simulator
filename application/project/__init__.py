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
)
from .controller import (
    main_controller,
    {% for device in device_actuator %}
    {{device[0].split("|")[0]}},{% endfor %}    
)
from .model import (
    {% for device in devices %}
    {{device}}_model,{% endfor %}
)
from .service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
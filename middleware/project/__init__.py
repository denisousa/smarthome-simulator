import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_mongoengine import MongoEngine
from flasgger import Swagger


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'smarthome',
    'host': 'mongodb://localhost/middleware'
}
app.config['DOCUMENTATION'] = '../documentation/'
db = MongoEngine(app)
swagger = Swagger(app)


from .controller import (
    features_controller,
    receive_data_controller,
    send_data_controller,
    thirdy_party_controller
)
from .model import middleware_model
from .service import middleware_service
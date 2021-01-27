import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_mongoengine import MongoEngine
from flasgger import Swagger
from flask_cors import CORS
from pymongo import MongoClient


def drop_database(database_name):
    mongo_client = MongoClient('mongodb://localhost:27017')
    database_list = mongo_client.database_names()
    mongo_client.drop_database(database_name)
    mongo_client.close()


drop_database('middleware')
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'smarthome',
    'host': 'mongodb://localhost/middleware'
}
app.config['DOCUMENTATION'] = '../documentation/'
db = MongoEngine(app)
swagger = Swagger(app)
CORS(app)


from .controller import (
    features_controller,
    receive_data_controller,
    send_data_controller,
    thirdy_party_controller
)
from .model import middleware_model
from .service import middleware_service

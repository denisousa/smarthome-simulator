from flask import Flask
from flask_mongoengine import MongoEngine
from pymongo import MongoClient


def drop_database(database_name):
    mongo_client = MongoClient('mongodb://localhost:27017')
    database_list = mongo_client.database_names()
    mongo_client.drop_database(database_name)
    mongo_client.close()


drop_database('environments')
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'environments',
    'host': 'mongodb://localhost/environments'
}
db = MongoEngine(app)


from .controller import environment_controller, update_controller
from .entitys import environment_entity
from .models import environment_model
from .services import environment_service

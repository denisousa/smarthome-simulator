from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'environments',
    'host': 'mongodb://localhost/environments'
}
db = MongoEngine(app)


from .controller import environment_controller
from .entitys import environment_entity
from .models import environment_model
from .services import environment_service

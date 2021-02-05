from flask import Flask
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
import socketio
import asyncio
from multiprocessing import Process


def drop_database(database_name):
    mongo_client = MongoClient('mongodb://localhost:27017')
    mongo_client.drop_database(database_name)
    mongo_client.close()


drop_database('environments')
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'environments',
    'host': 'mongodb://localhost/environments'
}
db = MongoEngine(app)

sio = socketio.Client(logger=True, engineio_logger=True)

def connect_websocket():
    asyncio.run(
        sio.connect('http://localhost:5000')
    )

# p = Process(target=connect_websocket)
# p.start()
# p.join()


from .controller import environment_controller, update_controller
from .entitys import environment_entity
from .models import environment_model
from .services import environment_service

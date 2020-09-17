from project.util.config_broker import ConfigScenario
from threading import Thread
from project import socketio
import pika
import json


class {{name_device}}Publisher(ConfigScenario, Thread):
    def __init__(self):
        ConfigScenario.__init__(self)
        Thread.__init__(self)

    def run(self):
        {% for communication in communications %}
        print("{{name_device}} -> {{communication}}")
        self.publish_data("{{communication}}_route")
        {% endfor %}

    def publish_data(self, routing_key):
        self.channel.basic_publish(
            exchange="exchange",
            routing_key=routing_key,
            properties=pika.BasicProperties(delivery_mode=2,),
            body=json.dumps({'teste': 'teste'}),
        )       
        #socketio.emit("", status)

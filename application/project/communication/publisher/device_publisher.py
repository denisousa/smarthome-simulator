from project.util.config_broker import ConfigScenario
from threading import Thread
from project import socketio
import pika
import json


class {{name_device}}Publisher(ConfigScenario, Thread):
    def __init__(self, data):
        ConfigScenario.__init__(self)
        Thread.__init__(self)
        self.data = data

    def run(self):
        {% for communication in communications %}
        print("{{name_device}} -> {{communication}}")
        self.publish_data("{{communication}}_route")
        {% endfor %}

    def publish_data(self, routing_key):
        self.data['data_from'] = '{{name_device}}'
        self.channel.basic_publish(
            exchange="exchange",
            routing_key=routing_key,
            properties=pika.BasicProperties(delivery_mode=2,),
            body=json.dumps(self.data),
        )

from project.util.config_broker import ConfigScenario
from threading import Thread
from project import socketio
import pika
import json


class {{name_device}}Subscriber(ConfigScenario, Thread):
    def __init__(self):
        ConfigScenario.__init__(self)
        Thread.__init__(self)
        self.declare_queue("{{name_device}}_queue")
        self.bind_exchange_queue("exchange", "{{name_device}}_queue", "{{name_device}}_route")

    def run(self):
        print('Running {{name_device}}...')
        pass

    def callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        body = body.decode("UTF-8")
        body = json.loads(body)
        print(body)
        #socketio.emit("", body)

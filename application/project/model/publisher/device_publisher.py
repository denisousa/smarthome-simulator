from project.util.construct_scenario import (
    exchange,
    bm_info,
)
from project.util.config_broker import ConfigScenario
from project.model.service.baby_monitor_service import BabyMonitorService
from project.model.baby_monitor import BabyMonitorSend, BabyMonitorReceive
from project.util.generate_data import data_from_baby
from project.util.clean_dict import clean_dict_baby_monitor
from threading import Thread
from project import socketio
import json
from project.util.generate_log import log
import pika
import random
from project.model.publisher.smartphone_publisher import SmartphonePublisher
from datetime import datetime
from project.controller.smartphone_controller import user_confirm


class {{device_publisher}}(ConfigScenario, Thread):
    def __init__(self):
        ConfigScenario.__init__(self)
        Thread.__init__(self)
        self.declare_exchange(exchange, "topic")

    def run(self):
        status = self.generate_status()
        self.publish_info_baby(status)

    def publish_info_baby(self, status):
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=bm_info,
            properties=pika.BasicProperties(delivery_mode=2,),
            body=json.dumps(status),
        )
        socketio.emit("BabyMonitorSent", status)
        print("(Publish) BM: ", status)

from project.util.config_broker import ConfigScenario
from project.util.construct_scenario import (
    exchange,
    queue_baby_monitor,
    queue_smartphone_bm,
    queue_smart_tv,
    bm_msg
)
from threading import Thread
from project import socketio
import json


class {{device_subscribe}}(ConfigScenario, Thread):
    def __init__(self):
        ConfigScenario.__init__(self)
        Thread.__init__(self)
        self.declare_exchange(exchange, "topic")
        self.declare_queue(queue_baby_monitor)
        self.declare_queue(queue_smartphone_bm)
        self.declare_queue(queue_smart_tv)
        self.bind_exchange_queue(exchange, queue_baby_monitor, bm_msg)

    def run(self):
        self.check_baby_status()

    def stop(self):
        print("(Subscribe) BM: Close")
        raise SystemExit()

    def callback_baby_monitor(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        body = body.decode("UTF-8")
        body = json.loads(body)
        socketio.emit("BabyMonitorReceive", body)

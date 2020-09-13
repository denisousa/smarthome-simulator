from project.model.subscriber.{{device_subscribe}} import {{class_device_subscriber}}
from multiprocessing import Process
from time import sleep
import pika

subscriber_list = []
subscriber_list.append({{class_device_subscriber}}())

process_list = []
for subscriber in subscriber_list:
    process = Process(target=sub.run)
    process.start()
    process_list.append(process)

sleep(1)

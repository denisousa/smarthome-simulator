from project.communication.subscriber import (
    {% for device in devices %}
    {{device}}_subscriber,{% endfor %}
)
from multiprocessing import Process
from time import sleep


subscriber_list = []
{% for device in devices %}
subscriber_list.append({{device}}_subscriber.{{device}}Subscriber()){% endfor %}

print('Start Subscribers:')
for sub in subscriber_list:
    process = Process(target=sub.run)
    process.start()

sleep(1)

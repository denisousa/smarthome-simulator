from project import socketio
'''from project.model.subscriber.baby_monitor_subscriber import {{class_device_subscriber}}
from project.model.publisher.baby_monitor_publisher import {{class_device_subscriber}}'''
from time import sleep

{{btn_device}} = False


@socketio.on("{}Connect".format({{device}}))
def {{device_connect}}():
    global {{btn_device}}
    {{btn_device}} = True
    info = {"info": "{{}} Start".format({{device}})}
    socketio.emit("{}Information".format, info)
    subscriber = {{class_device_subscriber}}()
    subscriber.start()
    while True:
        sleep(1)
        if {{btn_device}}:
            publisher = {{class_device_publisher}}()
            publisher.start()
        else:
            subscriber.stop()
            break


@socketio.on("{{}}Disconnect")
def {{device_disconnect}}():
    global {{btn_device}}
    {{btn_device}} = False

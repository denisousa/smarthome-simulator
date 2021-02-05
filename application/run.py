from project import app, socketio


if __name__ == "__main__":
    print('Run Simulator \n')
    socketio.run(app, port=5000)

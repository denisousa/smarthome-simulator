from project import app, socketio


if __name__ == "__main__":
    print('Run Middleware \n')
    socketio.run(app)

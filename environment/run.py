from project import app

# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
if __name__ == "__main__":
    app.run(port=5001)

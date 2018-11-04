from flask import Flask
import docker
app = Flask(__name__)

@app.route('/')
def hello_world():
    client = docker.from_env()
    return client.containers.run('hello-world')
    #return 'Hello, World!'


from flask import Flask, render_template, request, send_from_directory
import docker
import os
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def result():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def getUserInput():
    # Get user input from front end
    text = request.form['box']
    print(text)

    # Make a python file that will contain user input
    # File is overwritten when user submits more than one input
    # counter = 1
    fileName = "userFile.py"
     # + str(counter)
    outF = open(fileName, "w")
    outF.writelines(text)
    outF.close()
    os.system("docker build -t test-file .")

    os.system("docker run test-file > output.txt")

    x = ""
    with open("output.txt", "r") as f:
        for line in f:
            x += str(line)





    # client = docker.from_env()
    # image = client.containers.run("test-file")
    return render_template("index.html", output=x)


if __name__ == '__main__':
   app.run(debug = True)

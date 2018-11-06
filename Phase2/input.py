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


@app.route('/input')
def result():
    return render_template("input.html")

@app.route('/output')
def result2():
    return render_template("output.html")

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
    os.system("sudo docker build -t test-file .")
    client = docker.from_env()
    image = client.containers.run("test-file")
    return render_template("output.html", output=str(image))


if __name__ == '__main__':
   app.run(debug = True)

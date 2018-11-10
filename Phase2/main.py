from flask import Flask, render_template, request, send_from_directory
import docker
import os
app = Flask(__name__, static_url_path='')

broker = {"saiyans": "",
            "namekians": "",
            "earthlings": "",
            "villians": ""}

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def result():
    return render_template("pubsub.html")
#
# @app.route('/publish')
# def result2():
#     return render_template("publish.html")
# def dispInput(testStr):
#     return render_template("publish.html", output=testStr)

@app.route('/', methods=['GET', 'POST'])
def getUserInput():
    # Get user input from front end
    # text = request.form['box']
    # dispInput(text)
    if (request.form.get('saiyan') == 'saiyan'):
        print("saiyan is selected")
    if (request.form.get('namekian') == 'namekian'):
        print("namekian is selected")
    return render_template("pubsub.html")


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")


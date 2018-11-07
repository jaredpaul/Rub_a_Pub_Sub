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


@app.route('/subscribe')
def result():
    return render_template("subscribe.html")

@app.route('/publish')
def result2():
    return render_template("publish.html")
def dispInput(testStr):
    return render_template("publish.html", output=testStr)

@app.route('/subscribe', methods=['GET', 'POST'])
def getUserInput():
    # Get user input from front end
    text = request.form['box']
    dispInput(text)
    return render_template("subscribe.html")


if __name__ == '__main__':
   app.run(debug = True)

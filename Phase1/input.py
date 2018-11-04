from flask import Flask, render_template, request, send_from_directory
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
    text = request.form['box']
    print(text)
    return render_template("index.html", output=text)
    # return text



if __name__ == '__main__':
   app.run(debug = True)
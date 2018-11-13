from flask import Flask, render_template, request, send_from_directory
import docker
import os
import redis

app = Flask(__name__, static_url_path='')

r = redis.Redis(
    host='hostname',
    password='password')

conn = redis.Redis('localhost')


map = {'info': []}

subs = {}

pubs = {"Saiyans": False,
        "Namekians": False,
        "Earthlings": False,
        "the Majin race": False,
        "the Ginyu Force": False,
        "the Z-Fighters": False
        }

conn.hmset("mapDict", map)

conn.hmset("subsDict", subs)

conn.hmset("pubsDict", pubs)



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
    for key in request.form:
        print(key)
        if key == "subName":
            already = ""
            str = ""
            topic = request.form.get("subSelect")
            usrName = request.form.get("subName")
            a = conn.hgetall("subsDict")
            if usrName in a:
                t = a[usrName]
                if topic not in t:
                    t.append(topic)
                    a[usrName] = t
                else:
                    s = "Sorry! Cannot subscribe to the same thing twice!"
                    b = conn.hgetall("mapDict")
                    tempp = b['info']
                    tempp.append(s)
                    b = tempp
                    for prev in tempp:
                        str += prev + '\n'
                    conn.hmset("mapDict", b)
                    return render_template("pubsub.html", output=str)
            else:
                c = conn.hgetall("pubsDict")
                for j in c:
                    if c[j]:
                        already += usrName + " has received information that has already been published regarding " + topic + "!"
                a[usrName] = [topic]

            notifyText = usrName + " has subscribed to information regarding " + topic + "!"
            notifyText += "\n" + already
            b = conn.hgetall("mapDict")
            tempp = b['info']
            tempp.append(notifyText)
            b['info'] = tempp
            conn.hmset("mapDict", b)
            conn.hmset("pubsDict", c)
            conn.hmset("subsDict", a)
            for prev in tempp:
                str += prev + '\n'
            return render_template("pubsub.html", output=str)

        if key == "pubInfo":
            str = ""
            topic = request.form.get("pubSelect")
            wasSub = ""
            c = conn.hgetall("pubsDict")
            c[topic] = True
            a = conn.hgetall("subsDict")
            for u in a:
                t = a[u]
                for info in t:
                    if topic == info:
                        wasSub += u + " has received new information regarding " + topic + "!"
            b = conn.hgetall("mapDict")
            tempp = b['info']
            if wasSub != "":
                tempp.append(wasSub)
                b['info'] = tempp
            for prev in tempp:
                str += prev + '\n'

            conn.hmset("subsDict", a)
            conn.hmset("mapDict", b)
            conn.hmset("pubsDict", c)


    return render_template("pubsub.html", output=str)


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")

from flask import Flask, render_template, request, send_from_directory
import docker
import os
import redis
app = Flask(__name__, static_url_path='')

map = {'info': []}

subs = {}

r = redis.Redis(host='localhost', port=6379)

pubs = {"Saiyans": False,
        "Namekians": False,
        "Earthlings": False,
        "the Majin race": False,
        "the Ginyu Force": False,
        "the Z-Fighters": False
        }



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
            already = "\n"
            str = "\n"
            topic = request.form.get("subSelect")
            usrName = request.form.get("subName")
            #if usrName in subs:
            if usrName in r:
                #t = subs[usrName]
                t = r.get(usrName)
                if topic not in t:
                    t.append(topic)
                    #subs[usrName] = t
                    r.set(usrName, t)
                else:
                    s = "Sorry! Cannot subscribe to the same thing twice!\n"
                    tempp = map['info']
                    tempp.append(s)
                    map['info'] = tempp
                    for prev in tempp:
                        str += prev + '\n'
                    return render_template("pubsub.html", output=str)
            else:
                print(pubs)
                for j in pubs:
                    if pubs[j]:
                        already += usrName + " has received information that has already been published regarding " + topic + "\n"
                #subs[usrName] = [topic]
                r.set(usrName, topic)

            notifyText = usrName + " has subscribed to information regarding " + topic + "!\n"
            notifyText += "\n" + already
            tempp = map['info']
            tempp.append(notifyText)
            map['info'] = tempp
            for prev in tempp:
                str += prev + '\n'
            return render_template("pubsub.html", output=str)

        if key == "pubInfo":
            str = ""
            topic = request.form.get("pubSelect")
            wasSub = ""
            pubs[topic] = True
            #for u in subs:
            for u in r:
                #t = subs[u]
                t = r.get(u)
                for info in t:
                    if topic == info:
                        wasSub += u + " has received new information regarding " + topic + "!\n"
            tempp = map['info']
            if wasSub != "":
                tempp.append(wasSub)
                map['info'] = tempp
            for prev in tempp:
                str += prev + '\n'

            print(pubs)

    return render_template("pubsub.html", output=str)


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")

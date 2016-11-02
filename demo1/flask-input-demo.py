from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    server = request.form['server']
    vlan = request.form['vlan']
    port = request.form['port']
    return "Server:  " + server + "Vlan:  " + vlan + "Port:  " + port

if __name__ == '__main__':
    app.run()
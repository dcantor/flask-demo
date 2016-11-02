from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    server = request.form['server']
    vlan = request.form['vlan']
    port = request.form['port']
    print ("the vlan is '" + vlan + "'")
    f = open("filename.txt", 'a')
    f.write("server is: " + server + "\n")
    f.write("vlan is: " + vlan + "\n")
    f.write("port is: " + port + "\n")
    f.close()
    return redirect('/')

if __name__ == '__main__':
    app.run()
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Method used: %s" % request.method

@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run()

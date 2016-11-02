from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef", "Toothpaste"]
    return render_template("shopping.html", food=food)

if __name__ == "__main__":
    app.run()

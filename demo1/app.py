from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

@app.before_first_request
def before_request():
    #create db if needed and connect
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    #close the db connection
    db.close()

@app.route('/')
def home():
    #render the home page with saved posts
    return render_template('home.html', posts=Post.select().order_by(Post.date))

@app.route('/new_post/')
def new_post():
    return render_template('new_post.html')

@app.route('/create/', methods=['POST'])
def create_post():
    #creates the new post
    Post.create(
        title=request.form['title'],
        text=request.form['text']
    )

    #return user to home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()

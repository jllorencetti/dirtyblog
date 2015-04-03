from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from flask.templating import render_template
from config import BASE_DIR
import config
from models import get_post_by_url, get_all_posts
import os
from functools import wraps
import markdown2
import codecs
import datetime

app = Flask(__name__)
today = datetime.date.today()

USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

basedir = BASE_DIR

app.config.from_object(__name__)


@app.context_processor
def inject_config():
    return dict(config=config)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or\
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('posting'))
    return render_template('login.html', error=error)


@app.route('/')
def index():
    return render_template('index.html',
                           posts=get_all_posts()[:config.HOME_MAX_POSTS],
                           menu_posts=get_all_posts())


@app.route('/about')
def about():
    return render_template('about.html', menu_posts=get_all_posts())


@app.route('/books')
def books():
    return render_template('books.html', menu_posts=get_all_posts())


@app.route('/posts/<post_url>')
def post(post_url):
    actual_post = get_post_by_url(post_url)
    return render_template('post.html', post=actual_post,
                           menu_posts=get_all_posts())
@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required. Please try again.")
        return redirect(url_for('main'))
    else:
        filename = basedir + "/posts/" + str(today) + "_" + title + "_" + title
        if not os.path.exists(os.path.dirname(filename)):
          os.makedirs(os.path.dirname(filename))
        with open(filename, "w") as f:
          f.write(title)
          f.write("\n")
          f.write("=")
          f.write("\n")
          f.write("\n")
          f.write("\n")
          f.write(post)
        markdown2.markdown(filename)
        return redirect(url_for('index'))
        get_all_posts()

@app.route('/posting')
@login_required
def posting():
    return render_template('main.html')



@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recente', feed_url=request.url, url=request.url_root)
    articles = get_all_posts()[:config.FEEDS_MAX_POSTS]
    for article in articles:
        feed.add(article.title,
                 content=unicode(article.get_content()),
                 content_type='html',
                 author='<your name here>',
                 url=article.url,
                 updated=article.get_datetime(),
                 published=article.get_datetime())
    return feed.get_response()


if __name__ == '__main__':
    app.run(debug=config.DEBUG)

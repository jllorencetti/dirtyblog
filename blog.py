# coding=utf-8
from flask import Flask, request
from flask.templating import render_template
from werkzeug.contrib.atom import AtomFeed

from models import get_post_by_url, get_all_posts


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', posts=get_all_posts()[:5], menu_posts=get_all_posts())


@app.route('/about')
def about():
    return render_template('about.html', menu_posts=get_all_posts())


@app.route('/books')
def books():
    return render_template('books.html', menu_posts=get_all_posts())


@app.route('/posts/<post_url>')
def post(post_url):
    actual_post = get_post_by_url(post_url)
    return render_template('post.html', post=actual_post, menu_posts=get_all_posts())


@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recente', feed_url=request.url, url=request.url_root)
    articles = get_all_posts()[:5]
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
    app.run(debug=True)

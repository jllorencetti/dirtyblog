import datetime

import os
import codecs
import markdown

import config

posts_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'posts')
cached_posts = []


def get_post_by_url(post_url):
    for p in get_all_posts():
        if p.url == post_url:
            return p


def get_all_posts():
    if not cached_posts:
        for _, _, files in os.walk(u'' + posts_directory.decode()):
            for filename in files:
                post = Post(filename.split('_')[0], filename.split('_')[1], filename.split('_')[2], filename)
                cached_posts.append(post)
        cached_posts.sort(key=lambda x: x.get_datetime(), reverse=True)
    return cached_posts


class Post(object):
    def __init__(self, date, url, title, filename, content=''):
        self.date = date
        self.url = url
        self.title = title
        self.content = content
        self.filename = filename

    def get_datetime(self):
        if self.date.split('-').__len__() != 3:
            splited = [2010, 1, 1]
        else:
            splited = [int(item) for item in self.date.split('-')]
        return datetime.datetime(splited[0], splited[1], splited[2])

    def get_str_datetime(self):
        return self.get_datetime().strftime("%d/%m/%Y")

    def few_content(self):
        return markdown.markdown(self.get_content()[:config.PREVIEW_POST_SIZE] + '...')

    def get_content(self):
        with codecs.open(os.path.join(posts_directory, self.filename), 'r', 'utf-8') as f:
            return markdown.markdown(f.read())



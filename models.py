import os
import glob
import datetime
import codecs

import markdown

from config import POSTS_DIRECTORY, PREVIEW_POST_SIZE

cached_posts = []


def get_post_by_url(post_url):
    for p in get_all_posts():
        if p.url == post_url:
            return p


def get_all_posts():
    if not cached_posts:
        for filepath in glob.glob('{}/*'.format(POSTS_DIRECTORY)):
            filename = os.path.split(filepath)[1]
            info = get_fileinfo(os.path.join(POSTS_DIRECTORY, filename))
            if not info['visible']:
                continue
            post = Post(info['date'], info['url'], info['title'], filename)
            cached_posts.append(post)
        cached_posts.sort(key=lambda x: x.get_datetime(), reverse=True)
    return cached_posts


def parse_metadata(text):
    metas = {key.lower(): value for (key, value) in
             [line.split(': ') for line in text.splitlines()]}

    metas['visible'] = 'True' in metas.get('visible', '')

    return metas


def parse_content(lines):
    content = ''
    content_found = False
    for line in lines:
        if content_found:
            content += line
        if 'content' in line.lower():
            content_found = True
    return content


def get_fileinfo(filename):
    text = ''
    with codecs.open(filename, 'r', 'utf-8') as f:
        for line in f:
            if 'content' in line.lower():
                break
            text += line
    return parse_metadata(text)


def get_filecontent(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        return parse_content(f.readlines())


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
        return markdown.markdown(self.get_content()[:PREVIEW_POST_SIZE] + '...')

    def get_content(self):
        return markdown.markdown(get_filecontent(os.path.join(POSTS_DIRECTORY, self.filename)))

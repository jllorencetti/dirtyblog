 [![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

About
=
This project is a little and simple Flask app which I use to maintain my blog.
It's ready to run on Heroku.
Every post is written as a separated Markdown file located in the posts directory.

Installation
=
All the requirements are listed in the requirements.txt file.
I suggest that you create a virtualenv to install the dependencies.
To install it just run:
pip install -r requirements.txt

Configuration
=
To use it you just need to configure the variables located in the config.py file.
There is configuration for setting the blog name, the base title, your Twitter and GitHub profile (if you want to list it in the blog), and a few other options.

If you want to edit the templates, some of these configurations can be deleted.

Usage
=
As said above, you need to store you posts files in the posts directory, and each post should have a URL, Title, Date and
Content tags in the header of the file, check the sample post for information.

Please, turn off the DEBUG mode in the config.py file when deploying to "production". :P

Hope you enjoy. :)

Feedback really appreciated.

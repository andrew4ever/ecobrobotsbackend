#!/usr/bin/python3
from run import create_app
from wsgiref.handlers import CGIHandler

from os import getcwd
from sys import path
path.insert(0, getcwd())
print("Content-Type: text/html\n\n")


class ProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SERVER_NAME'] = ""
        environ['SERVER_PORT'] = "80"
        environ['REQUEST_METHOD'] = "GET"
        environ['SCRIPT_NAME'] = ""
        environ['QUERY_STRING'] = ""
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        return self.app(environ, start_response)


if __name__ == '__main__':
    app = create_app()
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)

#!/usr/bin/python3
from wsgiref.handlers import CGIHandler
from os import getcwd

activate_this = '{0}/venv/bin/activate_this.py'.format(getcwd())
exec(open(activate_this).read(), dict(__file__=activate_this))

from run import create_app
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

#!/usr/bin/python3.6
from wsgiref.handlers import CGIHandler

activate_this = '/home/au402216/eco.brobots.org.ua/www/ecobrobotsbackend/venv/bin/activate_this.py'
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

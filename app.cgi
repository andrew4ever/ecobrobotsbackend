#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from app import create_app

CGIHandler().run(create_app())

#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld, '/api/v1.0', '/')

print app.url_map


if __name__ == '__main__':
    app.run(host='192.168.1.215')

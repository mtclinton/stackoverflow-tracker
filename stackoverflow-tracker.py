from flask import Flask, render_template, request, g
import sqlite3 as sql
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from HelloApiHandler import HelloApiHandler
from ListApiHandler import ListApiHandler

app = Flask(__name__)
CORS(app) #comment this on deployment

api = Api(app)



api.add_resource(ListApiHandler, '/')
api.add_resource(HelloApiHandler, '/<int:month>')


if __name__ == '__main__':
    app.run(debug=True)
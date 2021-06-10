from flask import Flask, render_template, request, g
import sqlite3 as sql
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment


from handler import NewHandler, PageHandler, RankingHandler, StarredHandler

app = Flask(__name__)
CORS(app) #comment this on deployment

api = Api(app)

api.add_resource(PageHandler.AllPageApiHandler, "/all/<string:topic>/<int:page>")
api.add_resource(NewHandler.AllNewApiHandler, "/new/all/<string:topic>/<int:page>")
api.add_resource(NewHandler.NewApiHandler, "/new/<string:topic>/<int:page>")
api.add_resource(RankingHandler.RankingApiHandler, "/rank/<string:topic>/<int:page>")
api.add_resource(StarredHandler.StarredApiHandler, "/starred/<string:topic>/<int:page>")

api.add_resource(PageHandler.PageApiHandler, "/<string:topic>/<int:page>")

if __name__ == '__main__':
    app.run(debug=True)
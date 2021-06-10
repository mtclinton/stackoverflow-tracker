from flask_restful import Api, Resource, reqparse
from handler import util
import sqlite3 as sql

class PageApiHandler(Resource):
    def get(self, topic, page):
        off = page*15
        data = util.query_db("select * from stackoverflow where topic=:topic AND read == 0 order by votes desc limit 15 offset :page", { 'topic': topic, 'page' : off})
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }

class AllPageApiHandler(Resource):
    def get(self, topic, page):
        off = page*15
        data = util.query_db("select * from stackoverflow where topic=:topic order by votes desc limit 15 offset :page", { 'topic': topic, 'page' : off})
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }

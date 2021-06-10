from flask_restful import Api, Resource, reqparse
from handler import util


class NewApiHandler(Resource):
    def get(self, page, topic_name):
        data = util.query_db("select * from stackoverflow order by date desc limit 15 offset %s where topic == %s AND read == 0;", (str(page*15), topic_name))
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }

class AllNewApiHandler(Resource):
    def get(self, page, topic_name):
        data = util.query_db("select * from stackoverflow order by date desc limit 15 offset %s where topic == %s;", (str(page*15), topic_name))
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }
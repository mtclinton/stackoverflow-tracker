from flask_restful import Api, Resource, reqparse
from handler import util

class RankingApiHandler(Resource):
    def get(self, page, topic_name):
        data = util.query_db("select * from stackoverflow order by ranking desc limit 15 offset %s where topic == %s;", (str(page*15), topic_name))
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }


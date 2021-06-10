from flask_restful import Api, Resource, reqparse
from handler import util


class StarredApiHandler(Resource):
    def get(self, page, topic_name):
        data = util.query_db("select * from stackoverflow order by votes desc limit 15 offset %s where topic == %s where starred == 1;", (str(page*15), topic_name))
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }

from flask_restful import Api, Resource, reqparse
from flask import Flask, render_template, request, g
import sqlite3 as sql

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

class ListApiHandler(Resource):
    def get(self):
        data = query_db('select * from stackoverflow order by votes desc limit 15')
        return {
            'resultStatus': 'SUCCESS',
            'message': data
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args['type']
        request_json = args['message']
        # ret_status, ret_msg = ReturnData(request_type, request_json)
        # currently just returning the req straight
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"

        final_ret = {"status": "Success", "message": message}

        return final_ret

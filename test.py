from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = {'name':'max'}
        return data, 200
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        
        nameFile = open('name.txt','w')
        nameFile.write(args['name'])
        data = {'ok':'dokey'}
        return data, 200
        nameFile.close()

class Locations(Resource):
    pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()

# -*-coding:utf-8 -*-
from flask_restful import Resource, reqparse
from lib.Salt import salt_api
from etc.configure import GetConfigure


class AddCron(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cabinet', type=str, location=['form', 'json', 'values', 'args'], required=True)
        parser.add_argument('host', type=str, location=['form', 'json', 'values', 'args'], required=True)
        parser.add_argument('crontab', type=str, location=['form', 'json', 'values', 'args'], required=True)
        args = parser.parse_args(strict=True)
        cabinet = args['cabinet']
        host = args['host']
        crontab = args['crontab']
        print(cabinet,host,crontab)
        return 200



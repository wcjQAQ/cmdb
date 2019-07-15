# -*-coding:utf-8 -*-
from flask_restful import Resource
from lib.Salt import salt_api
from etc.configure import GetConfigure
import re
import operator

class ShowCron(Resource):
     def get(self, hostname,users):
         arg = '%s' %users
         tgt = '%s' %hostname
         crontablist = salt_api()
         crontab = crontablist.list_crontab(tgt=tgt, arg=arg)
         return crontab


class ShowUsers(Resource):
    def get(self, hostname):
        arg = 'ls /var/spool/cron'
        tgt = '%s' % hostname
        crontablist = salt_api()
        users =  crontablist.run_command(tgt=tgt, arg=arg)['return'][0][tgt]
        return  re.split('\n',users)

class ShowCabinets(Resource):
    def get(self):
        sql = 'select  distinct cabinet from hosts'
        __db = GetConfigure.get_mysql_client()
        info = __db.select(sql)
        cabinets = []
        for i in info:
            cabinet = i[0]
            cabinets.append(cabinet)
        return cabinets


    def post(self):
        pass


class ShowHosts(Resource):
    def get(self, cabinet):
        sql = 'select ip from hosts where Cabinet = "%s"' % (cabinet)
        __db = GetConfigure.get_mysql_client()
        info = __db.select(sql)
        hosts = []
        for i in info:
            host = i[0]
            hosts.append(host)
        return hosts

class ShowHostInfo(Resource):
    def get(self, cabinet, host):
        sql = "select info from hosts where Cabinet = '%s' and ip = '%s'" % (cabinet, host)
        __db = GetConfigure.get_mysql_client()
        info = __db.select(sql)
        for i in info:
            hostinfo = i[0]
        return hostinfo


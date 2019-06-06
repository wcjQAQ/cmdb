from flask_restful import Resource
from lib.Salt import salt_api

class Show(Resource):
     def get(self, hostname,users):
         arg = 'crontab -l -u %s' %users
         tgt = '%s' %hostname
         crontablist = salt_api()
         return  crontablist.run_crontab(tgt=tgt, arg=arg)



class ShowUsers(Resource):
    def get(self, hostname):
        arg = 'ls /var/spool/cron'
        tgt = '%s' % hostname
        crontablist = salt_api()
        return crontablist.run_crontab(tgt=tgt, arg=arg)

class ShowCabinet(Resource):
    def get(self):
        cabinet = ['A1','A2','A3','A4','A5']
        return cabinet

class ShowHost(Resource):
    def get(self):
        arg = 'salt-key'
        tgt = 'c1'
        show_hosts = salt_api()
        return show_hosts.list_host(tgt=tgt, arg=arg)


import requests
from requests.packages import urllib3
urllib3.disable_warnings()
import json
import re



class salt_api(object):
    def __init__(self):
        #self.__url = 'https://192.168.57.11:8888'
        self.__url = 'http://10.10.50.89:8888'
        self.__token = self.__get_token()

    def __get_token(self):
        url = self.__url + '/login'
        print(url)
        data = {
            'username': 'saltapi',
            #'password': 'saltapi',
            'password': 'qiyuwbg@2016',
            'eauth': 'pam'
        }
        headers = {
            'Accept': 'application/json'
        }
        try:
            token = requests.post(url, data, headers, verify=False).json()['return'][0]['token']
            return token
        except:
            print('获取token失败')

    def post_request(self, data):
      try:
        headers = {
            'Accept': 'application/json',
            'X-Auth-Token': self.__token
        }
        req = requests.post(self.__url, data, headers=headers, verify=False)
        return  json.loads(req.text)
        #return req
      except BaseException as error:
        print(error)



    def list_crontab(self, arg, tgt):
        data = {
            'client': 'local',
            'tgt': tgt,
            'fun': 'cron.list_tab',
            'arg': arg
        }
        response = self.post_request(data)
        print(response['return'][0][tgt]['pre'])
        for i in response['return'][0][tgt]['pre']:
          print(i)

    def run_command(self, arg, tgt):
        data = {
            'client': 'local',
            'tgt': tgt,
            'fun': 'cmd.run',
            'arg': arg
        }
        response = self.post_request(data)
        return response


haha = salt_api()
arg = 'ls /var/spool/cron'
tgt = '10.10.50.51'
aa = haha.run_command(arg,tgt)
print(aa)
print((aa['return'][0][tgt]))


#xixi = 'sdssddsdsdsdssssssddsds'
#print(re.split(r'sssss', xixi))

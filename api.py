import requests
from requests.packages import urllib3
urllib3.disable_warnings()
import json
import re



class salt_api(object):
    def __init__(self):
        self.__url = 'https://192.168.57.11:8888'
        self.__token = self.__get_token()

    def __get_token(self):
        url = self.__url + '/login'
        print(url)
        data = {
            'username': 'saltapi',
            'password': 'saltapi',
            'eauth': 'pam'
        }
        headers = {
            'Accept': 'application/x-yaml'
        }
        try:
            token = requests.post(url, data, headers, verify=False).json()['return'][0]['token']
            return token
        except:
            print('获取token失败')

    def post_request(self, data):
        headers = {
            'Accept': 'application/x-yaml',
            'X-Auth-Token': self.__token
            #'X-Auth-Token': '3dbe5b332174b7f0ec4cbe48b97c87087c33cbe5'
        }
        req = requests.post(self.__url, data, headers=headers, verify=False).text
        reqList = req.split(":")
        #print(reqList)
        reqDict = reqList[2].split("\n")
        crontab = []
        for i in reqDict:
            if re.search('[a-z]|[A-Z]', i):
                #print(i.strip().strip('\''))
                crontab.append(i.strip().strip('\''))
        return crontab




    def run_crontab(self, arg, tgt):
        data = {
            'client': 'local',
            'tgt': tgt,
            'fun': 'cmd.run',
            'arg': arg
        }
        response = self.post_request(data)
        return response

    def list_hosts(self, ar, tgt):
        data = {
            'client': 'local',
            'tgt': tgt,
            'fun': 'cmd.run',
            'arg': arg
        }
        response = self.post_request(data)
        return response
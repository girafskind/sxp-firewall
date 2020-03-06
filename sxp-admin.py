import json
import sys
import urllib3
import requests

from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

server = "https://hawk-asa01:4443"



req = urllib3.PoolManager()

TOKEN = '57FEDA@4096@3FB4@67FD4111442B3A2B881B8BBE197B89BD1AE173A0'


def getACLS(server,interface, object=None):

	req = urllib3.PoolManager()

	header = {'content-type': 'application/json','User-agent': 'REST API Agent','X-Auth-Token': TOKEN}

	url = server + "/api/access/in/"+interface+"/rules/"+object

	response = requests.get(url, headers=header, verify=False)
	response_json = response.json()
#	response_list = response_json['items']


	print(response_json['active'])

def enableACL(object,interface):
	req = urllib3.PoolManager()
	header = {'content-type': 'application/json','User-agent': 'REST API Agent','X-Auth-Token': TOKEN}

	payload = {"active" : True}

	url = server + "/api/access/in/"+interface+"/rules/"+object

	requests.patch(url, headers=header, data=json.dumps(payload), verify=False)

def disableACL(object,interface):
	req = urllib3.PoolManager()
	header = {'content-type': 'application/json','User-agent': 'REST API Agent','X-Auth-Token': TOKEN}

	payload = {"active" : False}

	url = server + "/api/access/in/"+interface+"/rules/"+object

	requests.patch(url, headers=header, data=json.dumps(payload), verify=False)



getACLS(server,"LAN","2605530362")
#enableACL("2605530362","LAN")
disableACL("2605530362","LAN")
getACLS(server,"LAN","2605530362")

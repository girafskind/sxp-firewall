import json
import sys
import urllib3
import requests

from urllib3.exceptions import InsecureRequestWarning

from config import TOKEN, SERVER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


req = urllib3.PoolManager()



def getACLS(server,interface, object=""):

	req = urllib3.PoolManager()

	header = {'content-type': 'application/json','User-agent': 'REST API Agent','X-Auth-Token': TOKEN}

	url = server + "/api/access/in/"+interface+"/rules/"+object

	response = requests.get(url, headers=header, verify=False)
	response_json = response.json()

	print("Log1")
	print(response_json)


def enableACL(server,object,interface):
	req = urllib3.PoolManager()
	header = {'content-type': 'application/json','User-agent': 'REST API Agent','X-Auth-Token': TOKEN}

	payload = {"active" : True}

	url = server + "/api/access/in/"+interface+"/rules/"+object

	requests.patch(url, headers=header, data=json.dumps(payload), verify=False)

def disableACL(server,object,interface):
	req = urllib3.PoolManager()
	header = {'content-type': 'application/json','User-agent': 'REST API Agent','X-Auth-Token': TOKEN}

	payload = {"active" : False}

	url = server + "/api/access/in/"+interface+"/rules/"+object

	requests.patch(url, headers=header, data=json.dumps(payload), verify=False)



def main():
	print("log")
	#getACLS(SERVER,"LAN","2605530362")
	#enableACL(SERVER,"2605530362","LAN")
	#disableACL(SERVER,"2605530362","LAN")
	#getACLS(SERVER,"LAN","2605530362")
	getACLS(SERVER,"LAN","3123348233")


if __name__ == '__main__':
	main()

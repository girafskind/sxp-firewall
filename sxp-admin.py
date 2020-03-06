import json
import sys
import urllib3
import requests

from urllib3.exceptions import InsecureRequestWarning

from config import TOKEN, SERVER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


# find_obj_in_acl find object id in access-list containing SGT
def find_acl_sgt(sgt, server, interface):
	return_data = []
	raw_data = get_acls(server, interface)
	data = raw_data['items']
	for i in data:
		if 'srcSecurity' in i or 'dstSecurity' in i:
			if sgt == (i['srcSecurity']['value'] or i['srcSecurity']['value']):
				return_data.append(i['objectId'])

	return return_data


# get_acls function returns access-lists on a interface. ObjectID is optional to get one specific ACL."""
def get_acls(server, interface, object_id=""):
	header = {'content-type': 'application/json', 'User-agent': 'REST API Agent', 'X-Auth-Token': TOKEN}
	url = server + "/api/access/in/" + interface + "/rules/" + object_id
	response = requests.get(url, headers=header, verify=False)
	json_data = response.json()
	#print(json.dumps(json_data, indent=2))
	return json_data


# Enables a line in the access-list, given obecjtId and interfacename.
def enable_acl(server, object_id, interface):
	req = urllib3.PoolManager()
	header = {'content-type': 'application/json', 'User-agent': 'REST API Agent', 'X-Auth-Token': TOKEN}

	payload = {"active" : True}

	url = server + "/api/access/in/" + interface + "/rules/" + object_id

	requests.patch(url, headers=header, data=json.dumps(payload), verify=False)


# Disables a line in the access-list, given objectId and interface name.
def disable_acl(server, object_id, interface):
	req = urllib3.PoolManager()
	header = {'content-type': 'application/json', 'User-agent': 'REST API Agent', 'X-Auth-Token': TOKEN}
	print(object_id)
	payload = {"active": False}

	url = server + "/api/access/in/" + interface + "/rules/" + object_id

	requests.patch(url, headers=header, data=json.dumps(payload), verify=False)

def main():
	print("Starting")
	#getACLS(SERVER,"LAN","2605530362")
	#enableACL(SERVER,"2605530362","LAN")
	#disableACL(SERVER,"2605530362","LAN")
	#getACLS(SERVER,"LAN","2605530362")
	#get_acls(SERVER, "LAN")
	list = find_acl_sgt("Bo", SERVER, "LAN")
	for i in list:
		disable_acl(SERVER, i, "LAN")


if __name__ == '__main__':
	main()

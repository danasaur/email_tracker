# checks a users gmail and sends the count in the inbox to a text file

import json
import requests
import time

def main():
 
	config_dict = get_account_info()

	inbox_count = get_email_count(config_dict)

	post_feedback = create_datapoint(config_dict, inbox_count)


def get_account_info():
	# retrieve account info as a dict from json file
	json_config = open('email_tracker_config.json')
	config_dict = json.load(json_config)

	# json config dictionary containts the following keys:
	# email_address, email_pass, bm_username, bm_goal, bm_auth_token
	return config_dict

	# prompt user for email and password
	# email_address = raw_input("email address: ")
	# password = raw_input("password: ")
	# imap_server = email_address.split('@')[1]

def get_email_count(config_dict):
	import imaplib

	# unpack email_address, email_pass, and email_server 
	email_address = config_dict["email"]
	email_pass = config_dict["email_pass"]
	email_server = email_address.split('@')[1]

	imap_server = "imap."+ email_server
	mail = imaplib.IMAP4_SSL(imap_server)

	# log in
	mail.login(email_address, email_pass)
	mail.list()

	# connect to inbox.
	mail.select("inbox") 

	# search and return uids (unique ids for each email)
	result, data = mail.uid('search', None, "ALL") 	

	inbox_count = len(data[0].split());

	return inbox_count

def get_time_now():
	timestamp = int(time.time())
	return timestamp

# create a datapoint, send it to beeminder
def create_datapoint(config_dict, inbox_count):

	# get data point info
	timestamp = get_time_now()
	bm_auth_token = config_dict["bm_auth_token"]
	
	# gather datapoint info for requests.post params
	datapoint = {
	    'auth_token': bm_auth_token,
	    'timestamp': timestamp,
	    'value': inbox_count 
	}

	bm_url_template = "https://www.beeminder.com//api/v1/users/{bm_username}/goals/{bm_goal}/datapoints.json"
	bm_url = bm_url_template.format(**config_dict)

	post_feedback = requests.post(bm_url, params=datapoint)

	return post_feedback

if __name__ == '__main__':
	main()
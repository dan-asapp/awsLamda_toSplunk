from botocore.vendored import requests
import json
import os

def gen_post_request(payload):
	token = "Splunk " + os.environ['HTTP_TOKEN']
	return requests.post(url=os.environ['URL'], 
			     data=payload, 
			     headers={'Authorization': token })

def package_and_post(payload):
	response = gen_post_request(json.dumps({'event' : payload}))
	return response.status_code

def lambda_handler(event, context):
	body = json.loads(event['body'])
	return [package_and_post(alert) for alert in body['alerts']]

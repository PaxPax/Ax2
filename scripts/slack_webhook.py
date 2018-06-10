import requests
import configparser
import json

def read_slack_config():
    config = configparser.ConfigParser()

    try:
        with open('../config_folder/slack_config.cfg') as fp:
            config.readfp(fp)
    except IOError:
        print('An error has occured in reading in slack_webhook')
    
    return config['webhook']['slack_webhook']

def get_message():

    try:
        with open('../message/user_message.txt', 'r') as out_file:
            return out_file.read()
    except IOError:
        print('An error has occured reading user message file')

def create_payload():
    webhook_url = read_slack_config()
    slack_message = {'text', get_message()}

    send_message = requests.post(webhook_url, data=json.dumps(slack_message),
    headers={'Content-Type': 'application/json'})
    
    if send_message.status_code != 200:
        raise ValueError(
            'Sending slack message error, response not 200'
        )

create_payload()
import requests
import configparser

#first import settings
def read_discord_config():
    config = configparser.ConfigParser()
    temp = {}
    try:
        with open('../config_folder/discord_config.cfg') as fp:
            config.readfp(fp)
    except IOError:
        print('An error has occured reading the file')
    
    for key in config['discord']:
        temp[key] = config['discord'][key]

    return temp

#next import the message
def read_message():
    try:
        with open('../message/user_message.txt', 'r') as out_file:
            return out_file.read()
    except IOError:
        print('An error has occurred reading the files')

def get_webhook():
    temp = {}
    config = configparser.ConfigParser()
    try:
        with open('../config_folder/discord_config.cfg') as fp:
            config.readfp(fp)
    except IOError:
        print('An error has occured reading the file')
    
    for key in config['webhook']:
        temp[key] = config['discord'][key]

    return temp

#create the payload
def create_payload():
    payload = {}
    config_values = read_discord_config()
    webhookurl = get_webhook()

    for key in config_values:
        payload[key] = config_values[key]
    payload['content'] = read_message()
    
    send_message = requests.post(webhookurl, data=payload)

create_payload()
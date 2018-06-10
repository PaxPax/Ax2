import threading
import configparser
import discord_webhook, user_email, slack_webhook, text, twitter

def get_selected_options():
    tokens = {}
    config = configparser.ConfigParser()
    with open ('../config_folder/selected_options.cfg') as fp:
        config.readfp(fp)
    
    for key in config['selected']:
        tokens[key] = config['selected'][key]

    return tokens
    
        

get_selected_options()
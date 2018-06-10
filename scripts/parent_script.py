from threading import Thread
import configparser
import discord_webhook, user_email, slack_webhook,send_sms, send_twitter

def get_selected_options():
    temp = {}
    config = configparser.ConfigParser()
    try:
        with open ('../config_folder/selected_options.cfg') as fp:
            config.readfp(fp)
    except IOError:
        print('An error has occurred reading the file.')

    for key in config['selected']:
        temp[key] = config['selected'][key]

    return temp

def check_selected_options():
    selected_values = get_selected_options()
    imported_values = [discord_webhook, user_email, slack_webhook, send_sms, send_twitter]
    tmp_value = []
    for key in selected_values:
        if selected_values[key] == "False":
            for values in imported_values:
                if key in str(values):
                    tmp_value.append(values)
    return tmp_value

def begin_threads():
    modules_to_start = check_selected_options()
    for tt in modules_to_start:
        Thread(target=tt).start()

begin_threads()
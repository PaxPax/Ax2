from twilio.rest import Client
import configparser

def get_sms_config():
    config = configparser.ConfigParser()
    temp = {}

    try:
        with open('../config_folder/text.cfg') as fp:
            config.readfp(fp)
    except IOError:
        print('Failed to read text.cfg')
    for key in config['text']:
        temp[key] = config['text'][key]
    return temp

def get_message():
    try:
        with open('../message/user_message.txt') as out_file:
            return out_file.read()
    except IOError:
        print('An error has occured reading the message file')

def get_recips():
    try:
        with open('../contact_information/phone_numbers') as out_file:
            temp = out_file.read()
            return temp.split('\n')
    except IOError:
        print('An error has occured reading phone numbers')

def create_sms():
    list_receipeints = get_recips()
    auth_tokens = get_sms_config()
    _sid = auth_tokens['accountSID']
    _auth = auth_tokens['authToken']
    _sender = auth_tokens['phoneNumber']
    message = get_message()

    client = Client(_sid, _auth)
    for reciever in list_receipeints:
        message = client.messages.create(
            to=reciever,
            from_=_sender,
            body= message
        )

create_sms()
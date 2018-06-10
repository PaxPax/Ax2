import configparser
import smtplib

def get_email_config():
    config = configparser.ConfigParser()
    temp = {}
    try:
        with open('../config_folder/email.cfg') as fp:
            config.readfp(fp)
    except IOError:
        print('An error has occured opening email.cfg')

    for key in config['email']:
        temp[key] = config['email'][key]
    return temp

def read_message():
    try:
        with open('../message/user_message.txt', 'r') as out_file:
            return out_file.read()
    except IOError:
        print('An error has occurred reading the files')

def create_connection():
    email_config = get_email_config()

    try:
        if email_config['port'] == '465':
            message_creation = smtplib.SMTP_SSL(email_config['host'],email_config['port'])
            create_email(message_creation, True,email_config)
        else:
            message_creation = smtplib.SMTP(email_config['host'], email_config['port'])
            create_email(message_creation, False, email_config)
    except:
        print('Connection faild, make sure you are connected to the internet')

def get_email_addresses():
    try:
        with open('../contact_information/email_addresses', 'r') as out_file:
            temp = out_file.read()
            return temp.split('\n')
    except IOError:
        print('An error has occured reading email_address file')
    
def create_email(email_object,special_connection, email_config):
    email_content = read_message()
    if special_connection:
        email_object.ehlo()
    else:
        email_object.ehlo()
        email_object.starttls()
    email_object.login(email_config['address'], email_config['password'])

    email_recep = get_email_addresses()
    for recipeint in email_recep:
        failed_messages = email_object.sendmail(email_config['address'], recipeint, 'Subject: Announcement \n' +email_content)
    print(failed_messages)
    email_object.quit()

create_connection()
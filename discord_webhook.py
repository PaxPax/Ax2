import requests

payload = {'username': 'timmy', 'content': 'hey ugly'}
send_message = requests.post('https://discordapp.com/api/webhooks/366068895024545795/qwLLhENE5sWUvGK2W9I0K1i83P0qKtugXGyZNyiGap3zpgRJD5-nWGGXkIKbGSve9-8P',data=payload)
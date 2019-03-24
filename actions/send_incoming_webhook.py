import requests

incoming_webhook = ""

headers = {'Content-Type': 'application/json'}
data = '''{
    "text": "Hello world!"
}
'''

response = requests.post(incoming_webhook, data=data, headers=headers)

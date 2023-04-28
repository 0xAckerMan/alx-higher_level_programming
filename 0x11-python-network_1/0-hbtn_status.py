#!/usr/bin/python3
'''
Fetch from intranet/status
'''
import urllib.request

alx_url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(alx_url) as response:
    body_response = response.read()

print('Body response:\n\t- type: {}'.format(type(body_response)))
print('\t- content: {}'.format(body_response))
print('\t- utf8 content: {}'.format(body_response.decode('utf-8')))

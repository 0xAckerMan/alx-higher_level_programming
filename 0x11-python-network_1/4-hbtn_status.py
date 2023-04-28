#!/usr/bin/python3
'''
use request package and get a response
'''
import requests
link = "https://alx-intranet.hbtn.io/status"

if __name__ == '__main__':
    req = requests.get(link)
    response = req.text
    print("Body response")
    print("\t- type:{}".format(type(response)))
    print("\t- content: {}".format(response))

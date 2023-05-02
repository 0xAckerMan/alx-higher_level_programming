#!/usr/bin/python3
"""
lists 10 commits of a given repo
in order of latest to oldest
"""
import sys
import requests

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    req = requests.get(url=url)
    if req.status_code >= 400:
        print("None")
    else:
        for commit in req.json()[:10]:
            print("{}: {}".format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')
                ))

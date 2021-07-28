import requests
from pprint import pprint
import json
import os
username = 'geekbreans'
# token = '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'
token = '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'




repos = requests.get('https://api.github.com/user/repos', auth=(username, token))


json_data = repos.json()
for repo in repos.json():
    if not repo['private']:
        print(repo["full_name"], ' ', repo['html_url'])

with open('user_repos.json','w') as f:
    json.dump(json_data, f)
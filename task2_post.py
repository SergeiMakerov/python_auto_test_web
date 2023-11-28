import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def new_post(token):
    response = requests.post(data['url_posts'], headers={'X-Auth-Token': token},
                             params={'title': data['title'],
                                     'description': data['description'],
                                     'content': data['content']})
    response.encoding = 'utf-8'
    return response.json()


def my_descr(token):
    response = requests.get(data['url_posts'], headers={'X-Auth-Token': token})
    description_list = []
    for i in response.json()['data']:
        description_list.append(i['description'])
    return description_list

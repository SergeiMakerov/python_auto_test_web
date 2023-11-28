import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    response = requests.post(data['url'], data={'username': data['login'], 'password': data['password']})
    response.encoding = 'utf-8'
    return response.json()['token']


@pytest.fixture()
def description():
    return 'Create new post'
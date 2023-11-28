import requests
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)

   
url = data["url"]
url_post = data["url_posts"]
login = data["login"]
password = data["password"]

result = requests.post(url=url, data={"username": login, "password": password})
token = result.json()["token"]
print(token)
res_get = requests.get(url=url_post, headers={"X-Auth-Token": token})
print(res_get)
data = res_get.json() 
print(data)




import requests

#req = requests.post('http://127.0.0.1:5000/user', json = {"name":"test","pass":"PASSWORD"})
#req = requests.get('http://127.0.0.1:5000/users')
#req = requests.post('http://127.0.0.1:5000/auth', json = {"name":"test","pass":"PASSWORD"})
req = requests.post('http://127.0.0.1:5000/user/test', json = {"name":"New"},headers = {"auth":"2448A5"})


print(req.text)
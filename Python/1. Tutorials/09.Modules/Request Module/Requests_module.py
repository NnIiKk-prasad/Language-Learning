# -----Requests Module For HTTP Requests-----
import requests

# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc)
r = requests.get('https://w3schools.com/python/demopage.htm')
print(r.text)
print(r.status_code)
print(r.elapsed)

x = requests.head('https://www.w3schools.com/python/demopage.php')
print(x.headers)

y = requests.get('https://www.w3schools.com/python/demopage.js')
print(y.json())

# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}
# r2 = requests.post(url=url, data=myobj)
# print(r2.text)

# d = requests.delete('https://w3schools.com/python/demopage.php')
# print(d.text)

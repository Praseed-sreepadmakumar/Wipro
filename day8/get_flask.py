import requests

geturl="http://127.0.0.1:5000/users"

response=requests.get(geturl)
print(response.status_code)
print(response.json())

posturl="http://127.0.0.1:5000/users/add"

post_body={
    "name":"david",
}
r1=requests.post(posturl,json=post_body)
print(r1.status_code)
print(r1.json())

put_url="http://127.0.0.1:5000/users/2"

put_body={
    "name":"John"
}
r2=requests.put(put_url,json=put_body)
print(r2.status_code)
print(r2.json())
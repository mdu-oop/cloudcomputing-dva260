import urllib.parse
import urllib.request
import random
from time import sleep

base = "http://127.0.0.1:8080/store"
params = {"data": "25"}

url = base + "?" + urllib.parse.urlencode(params)

req = urllib.request.Request(
    url,
    headers={"User-Agent": "MyClient/1.0"},
    method="GET",
)

while True:
    temp_rand = random.randint(1, 10) 
    params = {"data": str(temp_rand)}
    url = base + "?" + urllib.parse.urlencode(params)

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MyClient/1.0"},
        method="GET",
    )
    sleep(1)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode("utf-8")
        print(resp.status, body)
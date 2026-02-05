import urllib.parse
import urllib.request
import random
from time import sleep

base = 'http://127.0.0.1:8080/store'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

while True:
    temp_rand = random.randint(-30, 30)
    values = {'data': str(temp_rand)}
    
    url = base + '?' + urllib.parse.urlencode(values)
    req = urllib.request.Request(url, headers=headers)
    
    sleep(1)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(response.status, the_page.decode('utf-8'))
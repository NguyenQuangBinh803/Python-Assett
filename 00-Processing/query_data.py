import time
t= time.time()
import requests as session
import bs4
import os
print(time.time()-t)




t= time.time()
url = 'https://cophieu68.vn/snapshot.php?id=GAS'
res = session.get(url)
code_1 = res.text[res.text.find('id="stockname_close"'):res.text.find('id="stockname_close"')+50]
print(code_1[code_1.find('>')+1:code_1.find('<')])
print(time.time()-t)
t= time.time()

url = 'https://cophieu68.vn/snapshot.php?id=MWG'
# os.environ['NO_PROXY'] = url
res = session.get(url)
code_1 = res.text[res.text.find('id="stockname_close"'):res.text.find('id="stockname_close"')+50]
print(code_1[code_1.find('>')+1:code_1.find('<')])
print(time.time()-t)


t= time.time()
url = 'https://cophieu68.vn/snapshot.php?id=MWG'
# os.environ['NO_PROXY'] = url
res = session.get(url)
code_1 = res.text[res.text.find('id="stockname_close"'):res.text.find('id="stockname_close"')+50]
print(code_1[code_1.find('>')+1:code_1.find('<')])
print(time.time()-t)

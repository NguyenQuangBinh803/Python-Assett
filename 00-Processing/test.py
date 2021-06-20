import time

import grequests


urls = ['https://cophieu68.vn/snapshot.php?id=GAS', 'https://cophieu68.vn/snapshot.php?id=MWG', 'https://cophieu68.vn/snapshot.php?id=VRE']  
while(1):
    t= time.time()
    price = []
    changes = []    
    unsent_request = (grequests.get(url) for url in urls)
    results = grequests.map(unsent_request)
    for i in range(len(results)):
        temp = results[i].text[results[i].text.find('id="stockname_close"'):results[i].text.find('id="stockname_close"')+50]
        price.append(temp[temp.find('>')+1:temp.find('<')])
        temp = results[i].text[results[i].text.find('id="stockname_change"'):results[i].text.find('id="stockname_change"')+100]
        changes.append(temp[temp.find('span>')+5:temp[temp.find('span>'):].find('<')].replace('\t','').replace('\r','').replace('\n','').replace('&nbsp;',''))

    print(time.time()-t)
    print(price,changes)
print(time.time()-t)
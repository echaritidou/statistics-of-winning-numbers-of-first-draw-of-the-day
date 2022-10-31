import requests
import json
import datetime
import collections
lst4=[]
lst3 = []
wn = []
lst = []
tmp = []
lst2 = []
cur_date = datetime.datetime.now()
for i in range(31):
    num=i
    cur_date = cur_date - datetime.timedelta(days=1)
    date_str = cur_date.strftime("%Y-%m-%d")
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/"+date_str + "/" + date_str
    r = requests.get(url)
    html = r.text
    data = json.loads(html)

    for scan in data['content']:
        wn = scan.get('winningNumbers')
        lst.append(scan["winningNumbers"])

    for scan in lst:
        tmp = scan.get('list')
        lst2.append(scan['list'])

    lst3.extend(lst2.pop())
print(lst3)
print(len(lst3))
counter=collections.Counter(lst3)
print(counter.most_common())









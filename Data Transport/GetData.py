import urllib.request
import json
from datetime import datetime

from confluent_kafka import Producer, KafkaError


fileName = datetime.now().strftime("%Y-%m-%d.json")
url = 'http://www.psudataeng.com:8000/getBreadCrumbData'
response = urllib.request.urlopen(url)

data1 = json.loads(response.read())
# data2 = json.dumps(data1, indent = 4)
print(data1[0])
print(data1[1])
# with open(fileName, 'w') as f:
#     f.write(data2)
#     f.close()

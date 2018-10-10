import requests
from requests.auth import HTTPBasicAuth

import urllib3
urllib3.disable_warnings()


auth=HTTPBasicAuth('hexer', 'bratvax37w1988')

url = "https://localhost:9200/herbert-*/_count"
data = {}
req = requests.get(url, data=data,auth=auth , verify=False)


print req.text




math = "5*10+9"


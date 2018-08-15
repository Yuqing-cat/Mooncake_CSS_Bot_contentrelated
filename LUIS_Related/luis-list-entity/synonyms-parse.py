# synonym for ms.service

import json

with open('ms_service_v4.json','r',encoding='utf-8') as f:
    ms_service = json.load(f)

for service in ms_service:
    print(service['list'],'=>',service['canonicalForm'])

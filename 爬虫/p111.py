import json
# data={'Tom':{'Weight':'汉语','Scpre':90,'heoght':170}}
# with open('data.json','w') as f:
#     data = json.dumps(data, ensure_ascii=False, indent=4)
#     json.dump(data,f)
#
#     print(data)

data={2:'Tom',1:'Ada',3:'Sam'}
print(json.dumps(data))
print(json.dumps(data,sort_keys=True))
print(json.dumps(data,indent=4,sort_keys=True))
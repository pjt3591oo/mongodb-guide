'''
pip install pymongo
'''

from pymongo import MongoClient
from bson.son import SON

# 방법1 - URI
mongodb_URI = "mongodb://admin:admin@127.0.0.1:27017"
client = MongoClient(mongodb_URI)

db = client['testdb'] # 데이터베이스 선택
post_collection = db['post'] # 콜렉션 선택

def show(data) :
  for row in data:
    print(row)
  print()

result = post_collection.aggregate([
  {"$match": {"title": "title3"}},
])

show(result)

result = post_collection.aggregate([  
  {"$group": {
    "_id": "$author",
    "count": { "$count": { } }
  }}
])

show(result)

result = post_collection.aggregate([  
  {"$group": {
    "_id": "$author",
    "count": { "$count": { } }
  }},
  {
    "$match": { "count": { "$gte": 5 } }
  }
])

show(result)

result = post_collection.aggregate([  
  {"$group": {
    "_id": {"author": "$author"},
    "count": { "$count": { } }
  }},
  {
    "$match": { "count": { "$gte": 5 } }
  }
])

show(result)

result = post_collection.aggregate([  
  {"$group": {
    "_id": "$author",
    "count": { "$count": { } }
  }},
  {
    "$match": { "count": { "$gte": 5 } }
  },
  {
    "$sort" : { "count": -1 }
  }
])

show(result)

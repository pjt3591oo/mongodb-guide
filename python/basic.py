'''
pip install pymongo
'''

from pymongo import MongoClient

# 방법1 - URI
mongodb_URI = "mongodb://admin:admin@127.0.0.1:27017"
client = MongoClient(mongodb_URI)

# 방법2 - HOST, PORT
# client = MongoClient(host='localhost', port=27017)

# 데이터베이스 목록
print(client.list_database_names())

# 데이터베이스 선택
db = client['testdb']

# 콜랙션 목록
print(db.list_collection_names())

# collection 선택
post_collection = db['post']

# 데이터 추가
post_collection.insert_one({"title": "title4", "author": "mung4"})
post_collection.insert_many([
  {"title": "title5", "author": "mung5"},
  {"title": "title55", "author": "mung55"},
  {"title": "title555", "author": "mung555"},
])

# 데이터 조회
print(post_collection.find_one({}))

for row in post_collection.find({}):
  print(row)

# document 수 조회

print(post_collection.count_documents({}))
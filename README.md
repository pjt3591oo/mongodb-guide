# mongodb 

## 준비

* 컨테이너 생성

```sh
$ docker run --name mongodb.test.com -v data:/data/db -d -p 27017:27017 mongo
```

* 컨테이너 접속

```sh
$ docker exec -it mongodb.test.com bash

root@12sd924:/$ mongo
```

* 계정생성

```
> use admin

> db.createUser({user: "admin", pwd: "admin", roles: ["root"]})
Successfully added user: { "user" : "admin", "roles" : [ "root" ] }

> exit

# 추가한 계정으로 접속
root@12sd924:/$ mongo -u admin -p admin
```

* connect url schema

```
mongodb://admin:admin@127.0.0.1:27017
```

## 디비쿼리 (CRUD)

몽고디비 단위 database -> collection(table) -> document(row)

* 데이터베이스 생성

```
> use [데이터베이스 이름]
```

1개 이상의 collection이 있어야 데이터베이스 리스트에서 보임

* 디비, 콜렉션 조회

```
> show databases // 데이터베이스 리스트 조회

> show dbs // 데이터베이스 리스트 조회 

> db // 현재 사용중인 데이터베이스 확인

> db.stats() // 데이터베이스 정보 조회

> show collections // collection 조회
```

* collection(table) 생성

```
> db.createCollection(name, [options])
```

options는 해당 컬렉션의 설정값을 정의하는 객체. options는 다음과 같은 속성을 가진다.

```js
{
  capped: <boolean>,
  timeseries: {                  // Added in MongoDB 5.0
    timeField: <string>,        // required for time series collections
    metaField: <string>,
    granularity: <string>
  },
  expireAfterSeconds: <number>,
  autoIndexId: <boolean>,
  size: <number>,
  max: <number>,
  storageEngine: <document>,
  validator: <document>,
  validationLevel: <string>,
  validationAction: <string>,
  indexOptionDefaults: <document>,
  viewOn: <string>,              // Added in MongoDB 3.4
  pipeline: <pipeline>,          // Added in MongoDB 3.4
  collation: <document>,         // Added in MongoDB 3.4
  writeConcern: <document>
}
```

* collections 삭제

```
> db.컬렉션이름.drop()
```

* collections 이름변경

```
> db.컬렉션이름.renameCollection("바꿀 컬렉션 이름")
```

* document(row) 생성

```
> db.컬렉션이름.insert({})

> db.컬렉션이름.insert([{}, {}, {}])
```

```
> db.post.insert({title: "title1", author: "mung1"})
WriteResult({ "nInserted" : 1 })

> db.post.insert({title: "title2", author: "mung2"})
WriteResult({ "nInserted" : 1 })

> db.post.insert({title: "title3", author: "mung3"})
WriteResult({ "nInserted" : 1 })

> db.post.insert({title: "title3", author: "mung3"})
WriteResult({ "nInserted" : 1 })

> db.post.insert({title: "title2", author: "mung2"})
WriteResult({ "nInserted" : 1 })

> db.post.insert({title: "title1", author: "mung1"})
WriteResult({ "nInserted" : 1 })
```

* document(row) 조회

```
> db.컬렉션이름.find(query, projection)

> db.컬렉션이름.find(query, projection).pretty()
```

```
> db.post.find()
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1", "author" : "mung1" }
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57732dbdd01d1ee9b12"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57b32dbdd01d1ee9b13"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1", "author" : "mung1" }

> db.post.find({}, {title: true})
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1" }
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2" }
{ "_id" : ObjectId("6226b57732dbdd01d1ee9b12"), "title" : "title3" }
{ "_id" : ObjectId("6226b57b32dbdd01d1ee9b13"), "title" : "title3" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1" }

> db.post.find({title: "title1"}, {title: true})
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1" }
```

* 비교 연산자 , 논리 연산자

```
$eq : (equals) 주어진 값과 일치하는 값
$gt : (greater than) 주어진 값보다 큰 값
$gte : (greather than or equals) 주어진 값보다 크거나 같은 값
$lt : (less than) 주어진 값보다 작은 값
$lte : (less than or equals) 주어진 값보다 작거나 같은 값
$ne : (not equal) 주어진 값과 일치하지 않는 값
$in : 주어진 배열 안에 속하는 값
$nin : 주어빈 배열 안에 속하지 않는 값
```

```
> db.post.find( { likes: { $gt: 10, $lt: 30 } } )
```

```
$or
$and
$not
$nor
```

```
> db.post.find({ $or: [ { title: "title2" }, { title: "title3" } ] })
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57732dbdd01d1ee9b12"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57b32dbdd01d1ee9b13"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2", "author" : "mung2" }
```

* regexp

다음과 같은 형태로 정규식을 이용할 수 있다.

```
{ <field>: /pattern/<options> }
```

```
> db.post.find( { "title" : /title[1-2]/ } )
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1", "author" : "mung1" }
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1", "author" : "mung1" }
```

* where

where절을 이용하면 javascript 표현식 사용가능

```
> db.post.find( { $where: "this.title === 'title1'" } )
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1", "author" : "mung1" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1", "author" : "mung1" }
```

* sort, limit, skip

find()는 cursor를 반환한다. 커서는 sort, limit, offset을 사용할 수 있다.

```
> db.post.find().sort({_id: 1}) // 오름차순
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1", "author" : "mung1" }
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57732dbdd01d1ee9b12"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57b32dbdd01d1ee9b13"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1", "author" : "mung1" }

> db.post.find().sort({_id: -1}) // 내림차순
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1", "author" : "mung1" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57b32dbdd01d1ee9b13"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57732dbdd01d1ee9b12"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1", "author" : "mung1" }
```

```
> db.post.find().limit(2)
{ "_id" : ObjectId("6226b56f32dbdd01d1ee9b10"), "title" : "title1", "author" : "mung1" }
{ "_id" : ObjectId("6226b57332dbdd01d1ee9b11"), "title" : "title2", "author" : "mung2" }
```

```
> db.post.find().skip(2)
{ "_id" : ObjectId("6226b57732dbdd01d1ee9b12"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57b32dbdd01d1ee9b13"), "title" : "title3", "author" : "mung3" }
{ "_id" : ObjectId("6226b57c32dbdd01d1ee9b14"), "title" : "title2", "author" : "mung2" }
{ "_id" : ObjectId("6226b57d32dbdd01d1ee9b15"), "title" : "title1", "author" : "mung1" }
```

* document(row) 갯수 조회

```
> db.post.find().count()
```

* document(row) 삭제

```
> db.컬렉션이름.remove(criteria, justOne)

> db.컬렉션이름.remove({}, true)
```

justOne이 true로 설정되면 criteria와 일치하는 데이터 하나만 삭제 false일 경우 전부 삭제 기본값은 false이다.

## aggregate

몽고디비의 연산지 및 stage는 공식문서에서 확인할 수 있다.

https://docs.mongodb.com/manual/meta/aggregation-quick-reference

* stage operator

```
$match

$group

$project

$unwind

$out, $lookup

$bucket, $bucketAuto

$sort, $sortByCount

$limit, $skip

$merge
```

* operator

```
$eq : (equals) 주어진 값과 일치하는 값
$gt : (greater than) 주어진 값보다 큰 값
$gte : (greather than or equals) 주어진 값보다 크거나 같은 값
$lt : (less than) 주어진 값보다 작은 값
$lte : (less than or equals) 주어진 값보다 작거나 같은 값
$ne : (not equal) 주어진 값과 일치하지 않는 값
$in : 주어진 배열 안에 속하는 값
$nin : 주어빈 배열 안에 속하지 않는 값
$exists : 주어진 값이 존재하는지 여부

$or
$and
$not
$nor
```

### 통계 집계

$count, $max, $mix, $avg, $sum, $mul, $dateToString, $multiply, $accumulator

```
> db.post.aggregate([
  {$match: {title: "title3"}},
])
```

$match는 조건에 맞는 데이터만 추출하는 역할을 한다.

```
>  db.post.aggregate([  
  {$group: {
    _id: "$author",
    count: { $count: { } }
  }}
])

{ "_id" : "mung3", "count" : 2 }
{ "_id" : "mung55", "count" : 5 }
{ "_id" : "mung555", "count" : 5 }
{ "_id" : "mung4", "count" : 8 }
{ "_id" : "mung2", "count" : 2 }
{ "_id" : "mung5", "count" : 5 }
{ "_id" : "mung1", "count" : 2 }
```

_id를 기준으로 그룹핑 작업을 진행한다. $컬럼명 형태로 조회된 document(row)에서 컬럼을 접근할 수 있다. "$컬럼"은 조회 결과에서 해당 컬럼값을 가져오는 것을 의미한다.

$count는 document(row)의 수를 카운팅한다.

$group은 다음과 같은 포맷으로 작성한다.

***`{결과컬럼: 연산: 연산대상}`***

```
>  db.post.aggregate([  
  {$group: {
    _id: "$author",
    count: { $count: { } }
  }},
  {
    $match: { "count": { $gte: 5 } }
  }
])

{ "_id" : "mung55", "count" : 5 }
{ "_id" : "mung4", "count" : 8 }
{ "_id" : "mung555", "count" : 5 }
{ "_id" : "mung5", "count" : 5 }

> db.post.aggregate([  
  {$group: {
    _id: {author: "$author"},
    authorCount: { $count: { } }
  }},
  {
    $match: { "authorCount": { $gte: 5 } }
  }
])

{ "_id" : { "author" : "mung55" }, "authorCount" : 5 }
{ "_id" : { "author" : "mung4" }, "authorCount" : 8 }
{ "_id" : { "author" : "mung555" }, "authorCount" : 5 }
{ "_id" : { "author" : "mung5" }, "authorCount" : 5 }
```

$group는 _id에 여러 컬럼을 명시하여 여러 컬럼을 기준으로 그룹핑이 가능하다.

```
> db.post.aggregate([  
  {$group: {
    _id: "$author",
    count: { $count: { } }
  }},
  {
    $match: { "count": { $gte: 5 } }
  },
  {
    $sort : { count: -1 }
  }
])

{ "_id" : "mung4", "count" : 8 }
{ "_id" : "mung55", "count" : 5 }
{ "_id" : "mung555", "count" : 5 }
{ "_id" : "mung5", "count" : 5 }
```

```
> db.post.aggregate([  
  {$group: {
    _id: {author: "$author"},
    count: { $count: { } }
  }},
  {
    $match: { "count": { $gte: 5 } }
  }
]).map(item => item.count * 10)

[
	{
		"count" : 50
	},
	{
		"count" : 50
	},
	{
		"count" : 80
	},
	{
		"count" : 50
	}
]
```

sql을 aggregate 표현하는 것은 아래와 같다.

https://docs.mongodb.com/manual/reference/sql-aggregation-comparison/

몽고디비는 BSON(Binary JSON) 형태로 row를 관리한다.

## 인덱스

인덱스타입: 고유인덱스, 희소인덱스, 다중키 인덱스, 해시 인덱스, 지리 공간적 인덱스, 단일컬럼 인덱스

* 단일컬럼인덱스(Single Field Index)

```
> db.콜렉션이름.createIndex({컬럼명: 정렬방향})
```

```
> db.post.createIndex({title: 1})
```

1은 오름차순, -1은 내림차순

* 복합인덱스(Compound Index)

```
> db.콜렉션이름.createIndex({컬럼명: 정렬방향, 컬럼명: 정렬방향})
```

복합 인덱스 시 주의사항

```
> db.user.createIndex({userid:1, score:-1})

# 실행 시 문제 없이 진행 
> db.user.find({}).sort({ userid:1,score:-1})
> db.user.find({}).sort({ userid:-1,score:1})

# RAM exceeded error 발생
> db.user.find({}).sort({ userid:1,score:1})
> db.user.find({}).sort({ score:-1,userid:1})
```

복합 인덱스는 정렬 시 다른 정렬방향을 사용할 경우 문제발생

* 고유 인덱스(Unique Index)

```
> db.post.createIndex({컬럼명: 정렬방향}, {unique: true})
```

특정 필드가 유니크한 속성을 추가함

* 해시 인덱스(Hashed Index)

```
> db.post.createIndex({컬럼명: "hashed"})
```

해시 된 샤드 키를 사용하여 샤딩 컬렉션을 지원

필드의 해시 인덱스를 샤딩된 클러스터에서 데이터를 분할하기 위한 샤딩키로 사용

해시 된 샤드 키를 사용해서 컬렉션을 샤딩하면 데이터를 더 고르게 분산

다중 키 해시 인덱스는 허용하지 않음

* 희소 인덱스(Sparse Index)

```
> db.post.createIndex({컬럼명:1}, {sparse: true, unique: false})
```

null값을 가질 수 있는 엔티티가 있을 때

많은 document가 인덱스 키를 가지고 있지 않은데 키를 가진 대상으로 질의를 하는경우


* 인덱스 조회

```
> db.post.getIndexes()
[
	{
		"v" : 2,
		"key" : {
			"_id" : 1
		},
		"name" : "_id_"
	},
	{
		"v" : 2,
		"key" : {
			"title" : 1
		},
		"name" : "title_1"
	},
	{
		"v" : 2,
		"key" : {
			"title" : -1
		},
		"name" : "title_-1"
	}
]
```

* 인덱스에 대한 통계정보 조회

```
> db.post.aggregate( [ { $indexStats: { } } ] ).pretty()

{
	"name" : "_id_",
	"key" : {
		"_id" : 1
	},
	"host" : "040bcda7f541:27017",
	"accesses" : {
		"ops" : NumberLong(4),
		"since" : ISODate("2022-03-08T01:05:34.892Z")
	},
	"spec" : {
		"v" : 2,
		"key" : {
			"_id" : 1
		},
		"name" : "_id_"
	}
}
```

* 쿼리결과 분석

```
> db.post.find({author: "mung3"}).explain("executionStats").executionStats
```

explain("queryPlanner"): 가장 효율적인 쿼리를 찾기 위해 쿼리 최적화를 제공합니다.

explain("executionStats"): 특정 질의에서 실제로 실행한 결과의 세부사항을 제공합니다.

explain("allPlansExecution mode"): queryPlanner + executionStats 내용 모두 포함

***`totalDocsExamined`***는 참조된 document 횟수를 의미한다.

***`executionStages`***는 쿼리 수행 상세 정보를 의미한다. 상세 정보는 여러 단계에 나눠 진행되는 쿼리의 상세를 표시한다. executionStages의 stage는 ***COLLSCAN***, ***IXSCAN***이 있으며 ***COLLSAN***은 전체스캔, IXSCAN은 인덱스 스캔을 의미한다.

* 인덱스 사이즈

인덱스도 저장 공간을 차지함

```
> db.[콜렉션이름].totalIndexSize()
```

* 인덱스 제거

```
> db.[콜렉션이름].dropIndex(필드이름)
```


* 주의사항

```
1. 한 컬렉션에 2~3개의 인덱스를 가지지 않는것이 좋다. 만약 여러 컬럼의 쿼리라면 복합 인덱스를 사용

2. 최적화는 스캔(참조)한 document 수를 줄임으로써 가능. explain()의 nscanned 확인

3. 인덱스 구축이 완료될 때까지 데이터베이스는 모든 read/write 작업중단한다. background 옵션을 이용한다면 인덱스 작업을 백그라운드에서 동작시킬 수 있다.
```

* 인덱스 작동방식

index prefix, index intersection

index prefix란 왼쪽 인덱스부터 적용되는 부분집합 인덱스를 의미

```
생성된 인덱스:  { "item": 1, "location": 1, "stock": 1 }
```

만약 item, location, stock이 인덱스로 적용되는 경우

```
- 지원되는 쿼리: { item: 1 }
- 지원되는 쿼리: { item: 1, location: 1 }

- 지원하지 않는 조회 쿼리: "item" 필드 없이 "location" 필드만 존재 혹은 "stock" 필드만 존재 
- 지원하지 않는 조회 쿼리: "item" 필드 없이 "location", "stock" 필드만 존재 
```

item이 없을경우 location, stock은 인덱싱이 적용되지 않는다.

sort 연산은 prefix 조건에 맞지 않아도 지원함. 하지만 find에 포함하는 쿼리는 equality 조건에서 prefix를 포함해야 함

```
생성된 인덱스: { a:1, b: 1, c: 1, d: 1 }
```

a, b, c, d 인덱스가 생성되었을 경우

```
> db.data.find( { a: { $gt: 2 } } ).sort( { c: 1 } ) # 인덱스 적용 X: find(쿼리)쿼리에 equality 조건이 없음
> db.data.find( { c: 5 } ).sort( { c: 1 } )          # 인덱스 적용 X: find(쿼리)쿼리에 prefix 만족하지 않음
```

다음으로 index intersection이 있다. 인덱스가 교차해서 쿼리에 자동으로 적용되는 것을 의미한다.

```
- 인덱스 1: { qty: 1 }
- 인덱스 2: { item: 1 }

> db.orders.find( { item: "abc123", qty: { $gt: 15 } } )
```

index prefix는 복합 인덱스에서 동작하지만 index intersection은 단일 인덱스에서 적용된다. index intersection이 이루어지면 explain() 결과에서 AND_SORTED 또는 AND_HASH를 발견할 수 있다. 이 둘이 존재한다면 교차 인덱스가 작동된것이다.

## 백업(dump), 복구(restore)

* 전체백업

```bash
$ mongodump --out [dump data path] --host 127.0.0.1 --port 27017 -u [username] -p [password]
```

* 특정 디비 백업

```bash
$ mongodump --out [dump data path] --host 127.0.0.1 --port 27017 -u [username] -p [password] --db [덤프할 db명]
```

* 특정 디비의 컬렉션 백업

```bash
$ mongodump --out [dump data path] --host [dbhost] --port 27017 -u [username] -p [password] --db [dbname] --collection [collectionName]
```

* example

```bash
$ mongodump --out t --host 127.0.0.1 --port 27017 -u admin -p admin

2022-03-08T06:11:03.507+0000	writing admin.system.users to t/admin/system.users.bson
2022-03-08T06:11:03.509+0000	done dumping admin.system.users (1 document)
2022-03-08T06:11:03.509+0000	writing admin.system.version to t/admin/system.version.bson
2022-03-08T06:11:03.511+0000	done dumping admin.system.version (2 documents)
2022-03-08T06:11:03.512+0000	writing testdb.post to t/testdb/post.bson
2022-03-08T06:11:03.514+0000	done dumping testdb.post (29 documents)
2022-03-08T06:11:03.515+0000	writing testdb.collections to t/testdb/collections.bson
2022-03-08T06:11:03.517+0000	done dumping testdb.collections (2 documents)

$ ls
t

$ cd t
$ ls
admin  testdb

$ cd testdb
$ ls
collections.bson  collections.metadata.json  post.bson  post.metadata.json
```

* 복구(restore) 명령어 구조

```bash
$ mongorestore --host 127.0.0.1 --port 27017 -u [username] -p [password --drop [drop db name] --db [복구할 db name] [복구할 덤프데이터가 있는 디렉토리]
```

* 전체 복구(restore)

```bash
$ mongorestore --host 127.0.0.1 --port 27017 [dump data가 있는 디렉토리]
```

* 특정 컬렉션 복구(restore)

```bash
$ mongorestore --host <dbhost> --port 27017 --db [dbname] --collection [collectionName] [data-dump-path/dbname/collection.bson] --drop [drop db name]
```

컬렉션 단위로 복구하기 위해 --collection 옵션을 사용하여 collection.bson까지 경로를 입력해야한다.

## 맵 리듀스
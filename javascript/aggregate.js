const Client = require('mongodb').MongoClient;

Client.connect('mongodb://admin:admin@127.0.0.1:27017', function(error, db){
  if(error) {
    console.log(error);
  } else {
    const pipeline = [
      {$group: {
        _id: "$author",
        count: { "$count": { } }
      }},
      {
        $match: { "count": { "$gte": 5 } }
      }
    ]
    const aggCursor =  db.collection('student').aggregate(pipeline);
    for await (const doc of aggCursor) {
      console.log(doc);
  }
    db.close();
  }
});
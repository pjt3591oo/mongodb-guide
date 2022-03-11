const Client = require('mongodb').MongoClient;

Client.connect('mongodb://admin:admin@127.0.0.1:27017/testdb', function (error, db) {
  if (error) {
    console.log(error);
  } else {
    const doc = { title: 'title1', author: 'mung1' };
    db.collection('post').insert(doc);
    db.collection('post').insertMany([
      doc,
      doc,
      doc,
    ]);
    db.close();
  }
});

Client.connect('mongodb://admin:admin@127.0.0.1:27017/testdb', function (error, db) {
  if (error) {
    console.log(error);
  } else {
    const cursor = db.collection('post').find();
    cursor.each(function (err, doc) {
      if (err) {
        console.log(err);
      } else {
        console.log(doc);
      }
    });
    db.close();
  }
});

Client.connect('mongodb://admin:admin@127.0.0.1:27017/testdb', function (error, db) {
  if (error) {
    console.log(error);
  } else {
    const cursor = db.collection('post').update(
      {title: 'title1'},
      {title: 'title1111'}
    ); // title이 title1인 document를 전부 찾아서 title을 title1111로 바꿔줌
    cursor.each(function (err, doc) {
      if (err) {
        console.log(err);
      } else {
        console.log(doc);
      }
    });
    db.close();
  }
});

Client.connect('mongodb://admin:admin@127.0.0.1:27017/testdb', function (error, db) {
  if (error) {
    console.log(error);
  } else {
    const cursor = db.collection('post').remove(
      {title: 'title1'}
    ); // title이 title1인 document를 전부 찾아서 title을 title1111로 바꿔줌
    cursor.each(function (err, doc) {
      if (err) {
        console.log(err);
      } else {
        console.log(doc);
      }
    });
    db.close();
  }
});
#!/bin/bash

#insert
echo "INSERT"
curl --data "title=sample1&content=sample content" -X POST http://127.0.0.1:5000/info
echo
curl --data "title=sample2&content=sample content" -X POST http://127.0.0.1:5000/info
echo

#read
echo "READ"
curl -X GET http://127.0.0.1:5000/info
echo
curl -X GET http://127.0.0.1:5000/info/1
echo
curl -X GET http://127.0.0.1:5000/info/title/sample1
echo

#delete
echo "DELETE"
curl -X GET http://127.0.0.1:5000/info/delete/1
echo
curl -X GET http://127.0.0.1:5000/info/delete/2
echo

#read
#curl -X GET http://127.0.0.1:5000/info/1

echo "READ"
curl -X POST -F "title=GoodSearch" -F "file=@files/tests/good-search.png" http://127.0.0.1:5000/image
echo
curl -X GET http://127.0.0.1:5000/image
echo
curl -X GET http://127.0.0.1:5000/image/delete/1

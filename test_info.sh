#!/bin/bash

#insert
curl --data "title=sampe&content=sample content" -i -X POST http://127.0.0.1:5000/info

#read
curl -X GET http://127.0.0.1:5000/info/1

#delete
curl -X GET http://127.0.0.1:5000/info/delete/1

#read
#curl -X GET http://127.0.0.1:5000/info/1

curl -X POST -F "file=@files/tests/good-search.png" http://127.0.0.1:5000/image

curl -X GET http://127.0.0.1:5000/image/delete/1

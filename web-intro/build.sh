#!/bin/bash

docker build -t web-intro .
docker run -d -p 5000:5000 --name web-intro web-intro
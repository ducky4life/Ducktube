#!/bin/bash

# for my development use
git pull
docker stop ducktube
docker build -t ducktube:latest -f Dockerfile .
docker run --rm -p 8080:8080 --name ducktube ducktube:latest

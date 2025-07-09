#!/bin/bash

# for my development use
git pull
docker stop ducktube
docker build -t ducktube:latest -f arm64.Dockerfile .
docker run --rm -p 8080:8080 --name ducktube ducktube:latest

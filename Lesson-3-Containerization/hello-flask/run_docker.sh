#!/usr/bin/env bash

# Build image
docker build -t hello-flask .

# List docker images
docker image ls

# Run flask app
# docker run -p 5000:5000 hello-flask
# docker run -it -p 5000:5000 --rm --name hello-flask-instance hello-flask
docker run -p 5000:5000 --rm --name hello-flask-instance hello-flask
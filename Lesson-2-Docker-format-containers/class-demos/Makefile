setup:
	python3 -m venv ~/.udacity-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

validate-circleci:
	# See https://circleci.com/docs/2.0/local-cli/#processing-a-config
	circleci config process .circleci/config.yml

# get the current working directory of this makefile (on any machine)
# ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

run-circleci-local:
	# See https://circleci.com/docs/2.0/local-cli/#running-a-job
	# Failing attempts to fix this, it seems like they broke it and never fixed it! 
	circleci local execute
	# circleci local execute -v $(ROOT_DIR):/workdir
	# circleci build -v $(ROOT_DIR):/workdir

lint:
	hadolint demos/flask-sklearn-student-starter/Dockerfile
	pylint --disable=R,C,W1203 demos/**/**.py

all: install lint test

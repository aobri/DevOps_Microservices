setup:
	python3 -m venv ~/.hello-flask

env:
	#Show information about environment
	which python3
	python3 --version
	which pytest
	which pylint

install:
	pip install -r requirements.txt
	
lint: 
	pylint --load-plugins pylint_flask --disable=R,C *.py

run: 
	flask run
	
all: install lint
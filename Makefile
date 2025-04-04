start-venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

migrate:
	venv/bin/python3 src/manage.py makemigrations
	venv/bin/python3 src/manage.py migrate

start-app: start-venv migrate

freeze:
	venv/bin/pip freeze > requirements.txt
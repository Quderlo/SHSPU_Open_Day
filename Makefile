start-venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

migrate:
	venv/bin/python3 src/manage.py makemigrations game player user
	venv/bin/python3 src/manage.py migrate

entrypoint:
	venv/bin/python3 src/entrypoint.py

start-app: start-venv migrate entrypoint

freeze:
	venv/bin/pip freeze > requirements.txt
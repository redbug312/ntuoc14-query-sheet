ENV ?= . ../venv/bin/activate; \
	   PYTHONPATH=$(shell realpath ..)

.PHONY: start
start: app/db.sqlite
	$(ENV) gunicorn --bind 0.0.0.0:5000 run:app

.PHONY: debug
debug: app/db.sqlite
	# lsof -t -i:5000 to check pids
	$(ENV) FLASK_ENV=development flask run --port=5000

app/db.sqlite: app/instance/sheet.csv
	$(RM) $@
	echo ".mode csv\n.import $^ people" | sqlite3 $@

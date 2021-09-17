ENV ?= . ../env/bin/activate; \
	   PYTHONPATH=$(shell realpath ..)

.PHONY: start
start: app/db.sqlite
	$(ENV) gunicorn --bind 0.0.0.0:5000 run:app

app/db.sqlite: app/instance/sheet.csv
	$(RM) $@
	echo ".mode csv\n.import $^ people" | sqlite3 $@

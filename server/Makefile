ENV ?= . ../env/bin/activate; \
	   PYTHONPATH=$(shell realpath ..)
MIXINS = $(shell realpath app/templates/mixins/)

.PHONY: start
start: app/db.sqlite
	$(ENV) FLASK_APP=run.py FLASK_ENV=development \
		flask run --port=5000 --host=0.0.0.0 --extra-files=$(MIXINS)

app/db.sqlite: app/instance/sheet.csv
	$(RM) $@
	echo ".mode csv\n.import $^ people" | sqlite3 $@

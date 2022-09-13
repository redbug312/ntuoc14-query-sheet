PARALLEL := parallel --tag --lb
PYTHON3 ?= python3
ENV ?= . $(shell pwd)/venv/bin/activate; \
    PYTHONPATH=$(shell pwd)

.PHONY: start
start: venv
	$(ENV) make start -C server

.PHONY: debug
debug: venv
	$(ENV) make debug -C server

venv: requirements.txt
	$(PYTHON3) -m venv venv
	for requirement in $^; do \
		$(ENV) $(PYTHON3) -m pip install -r $$requirement; \
	done
	touch $@  # update timestamp

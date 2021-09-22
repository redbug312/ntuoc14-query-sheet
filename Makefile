PARALLEL := parallel --tag --lb
PYTHON3 ?= python3
ENV ?= . $(shell pwd)/env/bin/activate; \
    PYTHONPATH=$(shell pwd)

.PHONY: start
start: env
	$(ENV) make start -C server

.PHONY: debug
debug: env
	$(ENV) make debug -C server

env: requirements.txt
	$(PYTHON3) -m venv env
	for requirement in $^; do \
		$(ENV) $(PYTHON3) -m pip install -r $$requirement; \
	done
	touch $@  # update timestamp

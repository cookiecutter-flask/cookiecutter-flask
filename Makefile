# match default value of app_name from cookiecutter.json
COOKIE := myflaskapp
COOKIE_JAR := {{cookiecutter.app_name}}
COOKIE_CRUMBS := $(shell find $(COOKIE_JAR))

.PHONY: all
all: test

.PHONY: test
test: $(COOKIE)
	cd $(COOKIE); pip install -r requirements/dev.txt
	cd $(COOKIE); coverage run --source $(COOKIE) manage.py test
	cd $(COOKIE); coverage report -m

$(COOKIE): Makefile cookiecutter.json $(COOKIE_CRUMBS)
	cookiecutter . --no-input

.PHONY: clean
clean:
	rm -r $(COOKIE)

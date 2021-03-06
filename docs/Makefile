NPM    ?= npm
RUNNER ?= $(NPM) run
PORT   ?= 6015
CF     ?= cf
APP    ?= notify-docs
STG    ?= dev

SRC     = $(shell find src -type f)

# A help target including self-documenting targets (see the awk statement)
define HELP_TEXT
Usage: make [TARGET]... [MAKEVAR1=SOMETHING]...

Available targets:
endef
export HELP_TEXT
help: ## List common commands and their usage
	@echo "notify-docs"
	@echo
	@echo "$$HELP_TEXT"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / \
		{printf "\033[36m%-30s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:
	$(NPM) install

install-dev:
	$(MAKE) install

test:
	$(RUNNER) test

fmt:
	$(RUNNER) fmt

run:
	$(RUNNER) develop

build: public/index.html

public/index.html: export GATSBY_NOTIFY_BASE_URL ?= https://notify-$(STG).apps.y.cld.gov.au	
public/index.html: $(SRC)
	$(RUNNER) build

manifest-vars-%.yml:
	echo "stg: $*" > $@

deploy: build
	$(CF) zero-downtime-push $(APP) -f manifest.yml

deploy-dev: manifest-vars-$(STG).yml build
	$(CF) push $(APP)-$(STG) -f manifest-dev.yml --vars-file $<

clean:
	-rm -r public
	-rm -r .cache
	-rm manifest-vars-*

clean-full: clean
	-rm -rf node_modules

check-vulnerabilities:

.PHONY:
	help clean clean-full check-vulnerabilities \
	install install-dev \
	fmt test run \
	deploy deploy-dev

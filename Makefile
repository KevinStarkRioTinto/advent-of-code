#!/usr/bin/env make

default: help
help: ## Show help for each of the Makefile recipes.
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

env: environment.yml 	## Conda environment
	-conda env create --file environment.yml
	conda env update --file environment.yml --prune

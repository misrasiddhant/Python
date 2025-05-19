
PROJECT_NAME=

validate:
	if [ -z "$(PROJECT_NAME)" ]; then echo "PROJECT_NAME not defined"; exit 1; fi

directory:
	# Create project directory
	mkdir -p $(PROJECT_NAME)

venv:
	# Create virtual environment
	cd $(PROJECT_NAME) && \
	if [ -d ".venv" ]; then echo "Virtual environment already exists"; else echo "Creating virtual environment"; python3 -m venv .venv; fi

bootstrap: validate directory venv
	cd $(PROJECT_NAME) && \
	source .venv/bin/activate && \
	pip install poetry && \
	poetry init
	
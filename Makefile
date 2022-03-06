.PHONY:
test:
	tox -e pyt39

test_all:
	pytest --cov-report term-missing --cov makewords tests/makewords/ --cov data tests/data/

test_data:
	pytest --cov-report term-missing --cov data tests/data/

black:
	black src
	black tests

flake8:
	flake8 --ignore=E501 src

lint:
	tox -e linter

clean:
	rm -rf src/*.egg-info
	python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

dataflow:
	export PREFECT__FLOWS__CHECKPOINTING=true
	python -m data.flow.run

init:
	sh venv/bin/activate
	python -m piptools sync requirements-dev.txt
	pip install -e .

init-full:
	rm -rf venv
	python -m venv venv
	sh venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	python -m piptools compile --extra data --extra lint --extra notebooks --extra tests -o requirements-dev.txt

publish:
	pip install 'twine>=1.5.0'
	twine upload --repository testpypi dist/*
	rm -rf build dist src/*.egg-info

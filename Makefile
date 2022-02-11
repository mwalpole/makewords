.PHONY:
init:
	sh venv/bin/activate
	pip install -r requirements.txt

test:
	tox -e pyt39

coverage:
	pytest --cov-report term-missing --cov makewords tests/

lint:
	tox -e linter

black:
	black src
	black tests

flake8:
	flake8 --ignore=E501 src

publish:
	pip install 'twine>=1.5.0'
	twine upload --repository testpypi dist/*
	rm -rf build dist src/*.egg-info

nltk:
	sh getdata.sh

clean:
	rm -rf src/*.egg-info
	python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

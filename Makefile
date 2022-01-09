VENV = venv
PYTHON = $(VENV)/bin/python
NLTK_DATA = src/makewords/nltk_data/

.PHONY: nltk clean test lint black
nltk:
	sh $(VENV)/bin/activate
	$(PYTHON) -m nltk.downloader -d $(NLTK_DATA) words

clean:
	rm -rf $(NLTK_DATA)

test:
	tox -e pyt38

lint:
	tox -e linter

black:
	black src
	black tests
NLTK_DATA = src/makewords/nltk_data/
SYSPY = /usr/bin/env python3
VENV = venv/
VENVPY = $(VENV)bin/python

.PHONY: nltk clean test lint black
nltk:
	sh $(VENV)bin/activate
	$(VENVPY) -m nltk.downloader -d $(NLTK_DATA) words

clean:
	rm -rf $(NLTK_DATA)
	rm -rf $(VENV)
	$(SYSPY) -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	$(SYSPY) -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

test:
	tox -e pyt38

lint:
	tox -e linter

black:
	black src
	black tests
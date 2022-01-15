import collections
import textwrap


def count_letters(word):
    return dict(collections.Counter(word))


def print_message(s):
    """Handle terminal output consistently with NLTK."""
    prefix = "[makewords] "
    print(textwrap.fill(s, initial_indent=prefix))

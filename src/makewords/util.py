import textwrap


def count_letters(word):
    letter_count = {}
    for i in word:
        letter_count[i] = letter_count.get(i, 0) + 1
    return letter_count


def print_message(s):
    """Handle terminal output consistently with NLTK."""
    prefix = "[makewords] "
    print(textwrap.fill(s, initial_indent=prefix))

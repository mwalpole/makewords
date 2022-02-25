import collections
import os
import pendulum
from slugify import slugify

import nltk as nltklib
import nltk.corpus
import prefect
from prefect.engine.results import LocalResult
from prefect.engine.serializers import Serializer

import makewords.filters as filters

LANGUAGES = ("en", "ga")

CORPORA = {
    "Brown": nltk.corpus.brown,
    "Gutenberg": nltk.corpus.gutenberg,
    "Words": nltk.corpus.words,
}

RAW_DIR = "01-raw/en"
PROCESSED_DIR = "02-processed/en"
CLEAN_DIR = "03-clean/en"

logger = prefect.context.get("logger")


class ListToLinesSerializer(Serializer):
    def deserialize(self, value: bytes):
        return value.decode().split("\n")

    def serialize(self, value: bytes):
        return "\n".join(value).encode()


class CounterToCSVSerializer(Serializer):
    def deserialize(self, value: bytes):
        return value.decode().split("\n")

    def serialize(self, value: bytes):
        return "\n".join(("{},{}".format(w, n) for w, n in value.items())).encode()


def format_nltk_dir():
    return f"{os.path.dirname(__file__)}/{RAW_DIR}/nltk_data"


def format_location(task_name, **kwargs):
    suffix = slugify(pendulum.now("utc").isoformat())
    return f"{os.path.dirname(__file__)}/{PROCESSED_DIR}/{task_name}_{suffix}.prefect"


@prefect.task
def import_words_en():
    nltklib.download("words", download_dir=format_nltk_dir(), quiet=False)

    all_words = []
    for name, corpus in CORPORA.items():
        words = corpus.words()
        logger.info(f"{name} # words: {len(words):,}")
        all_words += words
        del words

    words = set(all_words)
    logger.info(f"Total unique words: {len(words):,}")
    return words


@prefect.task
def clean_words(words):
    words = list(filter(filters.word_is_ascii_lowercase, words))
    logger.info(f"Lower-case ascii words: {len(words):,}")
    return words


@prefect.task(
    result=LocalResult(location=format_location, serializer=ListToLinesSerializer())
)
def store_words(words):
    logger.info(f"Storing {len(words):,} words")
    return words


@prefect.task(
    result=LocalResult(location=format_location, serializer=CounterToCSVSerializer())
)
def store_counts(words):
    wfreq = collections.Counter(words)
    logger.info(f"Storing {len(wfreq):,} unique word counts")
    return wfreq


def main():
    with prefect.Flow("words") as flow:
        all_words = import_words_en()
        words = clean_words(all_words)
        store_words(words)
        store_counts(words)

    flow.run()


if __name__ == "__main__":
    main()

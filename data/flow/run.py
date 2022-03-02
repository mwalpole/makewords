import collections

import nltk
import nltk.corpus as nltk_corpus
import prefect
from prefect import task
from prefect.engine.results import LocalResult

import makewords.filters as filters
from data.flow.util import format_loc, format_dir, ReadableListSerializer, ReadableDictSerializer

LANGUAGES = ("en", "ga")

CORPORA = {
    "Brown": nltk_corpus.brown,
    "Gutenberg": nltk_corpus.gutenberg,
    "Words": nltk_corpus.words,
}

logger = prefect.context.get("logger")


@task
def import_words_en():
    nltk.download("words", download_dir=format_dir("nltk_data"), quiet=False)

    all_words = []
    for name, corpus in CORPORA.items():
        words = corpus.words()
        logger.info(f"{name} # words: {len(words):,}")
        all_words += words

    words = set(all_words)
    logger.info(f"Total unique words: {len(words):,}")
    return list(words)


@task
def clean_words(words):
    words = list(filter(filters.word_is_ascii_lowercase, words))
    logger.info(f"Lower-case ascii words: {len(words):,}")
    return words


@task(result=LocalResult(location=format_loc, serializer=ReadableListSerializer()))
def store_words(words):
    logger.info(f"Storing {len(words):,} words")
    return words


@task(result=LocalResult(location=format_loc, serializer=ReadableDictSerializer()))
def store_counts(words):
    wfreq = collections.Counter(words)
    logger.info(f"Storing {len(wfreq):,} unique word counts")
    return dict(wfreq)


def main():
    with prefect.Flow("words") as flow:
        all_words = import_words_en()
        words = clean_words(all_words)
        store_words(words)
        store_counts(words)

    flow.run()


if __name__ == "__main__":
    main()

import collections

import nltk

import makewords.filters as filters

# os.environ['NLTK_DATA'] = NLTK_DIR not working so append path directly
# nltk.data.path.append("/nltk_data")


message = "Full corpus discrete text:"
words = nltk.corpus.brown.words()
words += nltk.corpus.words.words()
words += nltk.corpus.gutenberg.words()
print(f"{message:26}{len(words):12,}")

message = "Lowercase alpha words:"
words = list(filter(filters.word_is_ascii_lowercase, words))
print(f"{message:26}{len(words):12,}".format(len(words)))

message = "Distinct words:"
with open("data/processed/words.txt", "w") as f:
    f.writelines("\n".join(set(words)))

wfreq = collections.Counter(words)
with open("data/processed/wordcount.csv", "w") as f:
    f.writelines("{},{}\n".format(w, n) for w, n in wfreq.items())
print(f"{message:26}{len(wfreq):12,} ")

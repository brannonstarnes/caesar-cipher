import nltk


nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

real_words = words.words()
real_names = names.names()

import re
from nltk.corpus import words, names

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)


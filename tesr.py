import re
from collections import Counter
import spacy
word2vec = spacy.load("en_core_web_sm")
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))


#!/usr/bin/python3

import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def clean_text(text):
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    return cleaned_text

def word_count(text):
    word_frequency = {}
    words = text.split()

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

text = """
Python is a widely used high-level interpreted language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.
"""

from wordcloud import WordCloud

import matplotlib.pyplot as plt

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('books_read.png')

text = "this. is, it. This is it.".lower()
print(word_count(clean_text(text)))

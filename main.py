import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Natural language processing

nltk.download("stopwords")
nltk.download('vader_lexicon')

english_stopwords = stopwords.words("english")
print(len(english_stopwords))

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1
d = [(value, key) for (key, value) in d.items()]

d = sorted(d, reverse=True)
filtered_words = []
for count, word in d:
    if word not in english_stopwords:
        filtered_words.append((word, count))

print(filtered_words[:5])

# Sentiment Analysis: What is the most positive and the most negative chapter?


import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Natural language processing
nltk.download("stopwords")

# Loading english stopwords
english_stopwords = stopwords.words("english")
print(len(english_stopwords))

# Load the book
with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

# Find all words
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}

# Counting words
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d = [(value, key) for (key, value) in d.items()]
d = sorted(d, reverse=True)

filtered_words = []

# Count without stopwords
for count, word in d:
    if word not in english_stopwords:
        filtered_words.append((word, count))

print(filtered_words[:5])

# Sentiment Analysis: What is the most positive and the most negative chapter?
analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(book)

if scores["pos"] > scores["neg"]:
    print("It is a positive book!")
else:
    print("It is a negative book")

print(scores)

# Analyze chapters sentiment analysis
pattern = re.compile("Chapter [0-9]+")
findings = re.split(pattern, book)
findings = findings[1:]
print(len(findings))

for nr, chapter in enumerate(findings):
    scores = analyzer.polarity_scores(chapter)
    print(nr + 1, scores)



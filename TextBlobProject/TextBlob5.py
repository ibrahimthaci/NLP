
from textblob import TextBlob

gfg = TextBlob("Python is a high-level language ")
gfg = gfg.noun_phrases

print(gfg)
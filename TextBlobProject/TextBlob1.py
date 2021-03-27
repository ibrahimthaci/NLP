from textblob import TextBlob
text = ("Codespeedy is a programming blog. "
       "Blog posts contain articles and tutorials on Python, CSS and even much more")
tb = TextBlob(text)
print(tb.tags)


# C: conjunction, coordinating
# CD: numeral, cardinal
# DT: determiner
# IN: preposition or conjunction, subordinating
# JJ: adjective or numeral, ordinal
# NNP: noun, proper, singular
# List of the tags:
# DT-determiner
# EX-existential there (like: “there is” … think of it like “there exists”)
# FW-foreign word
# IN-preposition/subordinating conjunction
# JJ-adjective ‘big’
# JJR-adjective, comparative ‘bigger’
# JJS-adjective, superlative ‘biggest’
# LS-list marker 1)
# MD-modal could, will
# NN-noun, singular ‘desk’
# RBR-adverb, comparative better
# RBS-adverb, superlative best
# NNS-noun plural ‘desks’
# NNP-proper noun, singular ‘Harrison’
# NNPS-proper noun, plural ‘Americans’
# PDT-predeterminer ‘all the kids’
# POS-possessive ending parent‘s
# PRP- personal pronoun I, he, she
# PRP$-possessive pronoun my, his, hers
# RB-adverb very, silently,
# RP-particle give up
# TO- to go ‘to‘ the store.
# UH-interjection
# VB-verb, base form take
# VBD-verb, past tense, took
# CC-coordinating conjunction
# CD-cardinal digit
# VBG-verb, gerund/present participle taking
# VBN-verb, past participle taken
# VBP-verb, sing. present, non-3d take
# VBZ-verb, 3rd person sing. present takes
# WDT-wh-determiner which
# WP-wh-pronoun who, what
# WP$-possessive wh-pronoun whose
# WRB-wh-adverb where, when
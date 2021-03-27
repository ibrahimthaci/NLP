from textblob import TextBlob

gfg = TextBlob("The titular threat of The Blob has always struck me as the ulti mate movie monster: an insatiably hungry, amoeba-like mass able to penetratevirtually any safeguard, capable of--as a doomed doctor chillinglydescribes it--assimilating flesh on contact.Snide comparisons to gelatin be damned, it's a concept with the mostdevastating of potential consequences, not unlike the grey goo scenarioproposed by technological theorists fearful ofartificial intelligence run rampant.")

gfg1 = TextBlob("I amm goodd at speling mstake.")

gfg = gfg.correct()
gfg1= gfg1.correct()
print(gfg)
print(gfg1)
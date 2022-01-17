# I tried this code 16/01/2022 it didnt work
# Becasue textblob use google translate, and google changed API

#Use Googletrans to translate the text
#import googletrans from googletrans import Translator
#translater = Translator() value = translater.translate(value) print(value.src)
#To detect the language we can use this...


from textblob import TextBlob
import nltk

print("What you you want to test:\n Type 1 for translate \n Type 2 for Correction "
      "\n Type 3 for Tags \n Type 4 for Sentences \n Type 5 for Noun Phrases \n Type 6 for Plurals")
x = int(input())
file = open('File.txt', 'r').read()

if(x==1):
    #file = open('File.txt', 'r').read()
    print("")
    print("Type 1 for German\nType 2 for Espaniol")
    x = int(input())
    if(x==1):
        blob = TextBlob(file)
        print(blob.translate(to='de'))
    elif(x == 2):
        blob = TextBlob(file)
        print(blob.translate(to='es'))
    else:
        print("Type the right numbers")

if(x==2):
    CorrectFile = TextBlob(file)
    CorrectedFile = CorrectFile.correct()
    print(CorrectedFile)

elif(x==3):
    text = (file)
    tb = TextBlob(text)
    print(tb.tags)

elif(x==4):
    blob1 = TextBlob("hello theree there")
    blob1.sentences
    print(blob1)

elif(x==5):
    gfg = TextBlob(file)
    gfg = gfg.noun_phrases
    print(gfg)

elif(x==6):
    animals = TextBlob("cat dog hourse")
    animals1=animals.words
    animals2=animals.words.pluralize()

    print(animals2)







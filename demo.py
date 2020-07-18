"""import nltk
word=[]
message="i it is hello world programme"
words=nltk.word_tokenize(message)
words=sorted(word)
print(word)
import json
with open("intents.json") as file:
    data=json.load(file)
intents=data["intents"]
print(intents[2])
library={"fruites":[{"appale":"the legends food","banana":"it monkes food"},{"chicken":"it is nonveg","nighty":"it is a dreess"}]}
for fruites in library:
    for lis in fruites:
        print(lis["appale"])
import json
import nltk
word=[]
lis=[]
with open("intents.json") as fil:
    data=json.load(fil)
for lie in data["intents"]:
    for patterns in lie["tag"]:
        wrds=nltk.word_tokenize(patterns)
        word.append(wrds)
        lis.append(lie["patterns"])
print(word,lis)
word="it is friday"
for i,j in enumerate(word):
    print(i,j)"""
lis=["banana","apple","chicku"]
lis=[1,2,2,5]
out_empty=[_ for _ in range(len(lis))]
print(out_empty)



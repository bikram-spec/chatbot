import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
import numpy
import tflearn
import tensorflow
import random
import json
import pickle
with open("intents.json") as file:
    data=json.load(file)
try:
    with open("data.pickle","rb") as f:
        words,lebels,tranning,output=pickle.load(f)
except:
    words=[]
    lebels=[]
    docs_x=[]
    docs_y=[]
    for intents in data["intents"]:
        for patterns in intents["patterns"]:
            wrds=nltk.word_tokenize(patterns)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intents["tag"])
        if intents["tag"] not in lebels:
            lebels.append(intents["tag"])
    words=[stemmer.stem(w.lower()) for w in words if w !="?"]
    words=sorted(list(set(words)))

    lebels=sorted(lebels)

    output=[]
    tranning=[]
    out_empty= [0 for _ in range(len(lebels))]
    for x,doc in enumerate(docs_x):
        bag=[]
        wrds=[stemmer.stem(w.lower()) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        output_row=out_empty[:]
        output_row[lebels.index(docs_y[x])]=1
        tranning.append(bag)
        output.append(output_row)
    tranning=numpy.array(tranning)
    output=numpy.array(output)
    with open("data.pickle","wb") as f:
        pickle.dump((words,lebels,tranning,output),f)

tensorflow.reset_default_graph()
net=tflearn.input_data(shape=[None,len(tranning[0])])
net=tflearn.fully_connected(net,8)
net=tflearn.fully_connected(net,8)
net=tflearn.fully_connected(net,len(output[0]),activation="softmax")
net=tflearn.regression(net)

model=tflearn.DNN(net)
try:
    model.load("model.tflearn")
except:
    model.fit(tranning,output,n_epoch=1000,batch_size=8,show_metric=True)
    model.save("model.tflearn")
def bag_of_words(s,words):
    bag=[0 for _ in range(len(words))]
    s_word=nltk.word_tokenize(s)
    s_word=[stemmer.stem(word.lower()) for word in s_word]
    for se in s_word:
        for i,w in enumerate(words):
            if w==se:
                bag[i]=1
    return numpy.array(bag)
def chat():
    print("hello sir i am friday how can i help you")
    while True:
        inp=input("you :")
        if inp.lower()=="quit":
            break
        result=model.predict([bag_of_words(inp,words)])
        result_index=numpy.argmax(result)
        tag=lebels[result_index]
        for tg in data["intents"]:
            if tg["tag"]==tag:
                responce=tg["responce"]

        print(random.choice((responce)))
chat()
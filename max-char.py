def maxchar(sentence):
    new_sentence = sentence.replace(" ", "")
    dictio = {}
    for n in new_sentence:
        if n in dictio:
            dictio[n] = dictio[n] + 1
        else:
            dictio[n] = 1
    order = sorted(dictio.items(), key=lambda x: x[1], reverse=True)
    return order[0][0]


maxchar('hello world')
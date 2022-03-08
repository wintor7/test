def count_unique_words(data):
    data = data.lower()
    #print(data)

    word_list = data.split(" ")
    #print(type(word_list))
    #print(word_list)

    uniq_words = set(word_list)
    #print(type(uniq_words))
    #rint(uniq_words)

    result = {}
    for target in uniq_words:
        #print(target)
        count = 0
        for source in word_list:
            if target == source:
                count += 1
        #print(target, count)
        result[target] = count
    return result

data = "I have a pen a"
result = count_unique_words(data)
print(type(result))
print(result)

#========= Level 2 ============
print("## Level 2")

def make_word_list(docs):
    #print(docs)
    docs_lower = []
    for doc in docs:
        small = doc.lower()
        docs_lower.append(small)
    #print(docs_lower)

    uniq_words = set()
    for doc in docs_lower:
        words = doc.split(" ")
        uniq_words = uniq_words | set(words)
    #print(type(uniq_words))
    #print(uniq_words)

    sentence_words = []
    for doc in docs_lower:
        result = count_unique_words(doc)
        sentence_words.append(result)
        #print(type(result))
        #print(result)
    return uniq_words, sentence_words

docs = ['I have a pen', 'I have an apple']
uniq_words, sentence_words = make_word_list(docs)
print(type(uniq_words))
print(uniq_words)
print(type(sentence_words))
print(sentence_words)
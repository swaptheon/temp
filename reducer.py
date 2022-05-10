import sys
docs_words = []
for line in sys.stdin:
    word2count={}
    line=line.strip()
    word,count=line.split('\t',1)
    try:
        count=int(count)
    except ValueError:
        continue

    try:
        word2count[word]=word2count[word]+count
    except:
        word2count[word]=count
    finally:
        docs_words.append(word2count)

for word2count in docs_words:
    for word in word2count.keys():
        w='%s\t%s' % (word,word2count[word])
        print(w)
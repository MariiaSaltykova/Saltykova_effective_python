import pickle
from lab07_bagOfWords import BagOfWords

f = open('myfile.bin', 'wb')
pickle.dump(BagOfWords(open('hamlet.txt', encoding="utf8")), f)
f.close()
f = open('myfile.bin', 'rb')
classBag = pickle.load(f)

print(classBag)



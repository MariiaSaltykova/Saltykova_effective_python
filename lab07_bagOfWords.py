from io import TextIOWrapper
from collections import defaultdict
import re
import operator
import json

class BagOfWords:
        def __init__(self, string):
                self.id = -1
                self.dictionary = defaultdict(int)
                if(isinstance(string, TextIOWrapper)):
                        text = string.read()
                        words = re.findall("\w+", text)
                        words = map(lambda w: w.lower(), words)
                        for word in words:
                                self.dictionary[word]+=1

                else:
                        words = re.findall("\w+", string)
                        words = map(lambda w: w.lower(), words)
                        for word in words:
                                self.dictionary[word]+=1
        def __str__(self):
                string = ''
                for key in self.dictionary.keys():
                        string += f'{key} : {self.dictionary[key]}, '
                return string[:-2]
        
        def __iter__(self):
                return self

        def __next__(self):
                self.id += 1
                if(self.id >= len(self.dictionary.keys())): raise StopIteration
                else : return list(self.dictionary.keys())[self.id]

        def __add__(self, bag):
                for k in self.dictionary.keys():
                        bag.dictionary[k] += self.dictionary[k]
                return bag
        def __getitem__(self, key):
                return self.dictionary[key.lower()]
        
        def __setitem__(self, key, val):
                self.dictionary[key.lower()] = val

        def save_to_json(self, json_file_name, data):
                with open(json_file_name, 'w') as f:
                        json.dump(data, f)

        def load_from_json(self, file_name):
                f = open(file_name)
                return json.load(f)
                        
bag = BagOfWords(open('hamlet.txt', encoding="utf8"))
print('Count of word "hamlet"= ',bag['Hamlet'])

sorted_dictionary = dict(sorted(bag.dictionary.items(), key=operator.itemgetter(1)))

index = len(list(sorted_dictionary.keys())) - 1

for i in range(10):
    key = list(sorted_dictionary.keys())[index]
    print (f"Word is: '{key}', count = {bag.dictionary[key]}")
    index -= 1
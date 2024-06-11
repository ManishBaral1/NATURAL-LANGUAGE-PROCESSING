# import the existing word and sentence tokenizing  
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 
  
text = "Natural Language Processing is cool"
print(sent_tokenize(text)) 
print(word_tokenize(text)) 

#outputs
['Natural Language Processing is cool']
['Natural','Langauge','Processing', 'is', 'cool']


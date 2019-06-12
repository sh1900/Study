# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 08:47:17 2018

@author: Alex
ODSC Nov 1
"""


nvidia-smi
cd to directory
python perceptron.py

data format -> vectorlize
top word - word cloud visulization
clean stop words
classify problem comedian 



top word
vocabulary
amount of profanity (swear word)


step:
    visual (data, aggregation, )
    
unique word count
word per min

sentient analysis
-sklearn naive bayes, labeled data
-textblob

give comedian positive/negative score
option
 
p(spam|click&money)

topic modeling
document term matrix
bag of word format

gensim python tollkit
LDA
nltk for parts of speech tagging
output
l hidden
d prob dist 

topic a
topic b
20% topic a, 80% topic b
topic is mix of words


choose k = 2 num topics
random assign each word


input:document-term matrix, num of topic, num of iteration
gensim find best topic word dist and topic dist for document

matrix factorization - sklearn

dimensionality reduction
lsi
nmf

singular value decomposition

LSI
doc         topic   topic doc
termxdoc = termxr  rxr  r x docs


nmf
term doc = term topic  topic x doc

Text Generation
input corpus
markov chain: one state only depends on previous state
output: new comedian

markov chain
represent as data dictionary
more complex: lstm

keep punctuation
weights to hidden layer

activation function(sum(weightsxinputs))

Long short term memory
rnn, sequence task
time series, nlp

word
prior2 - prior 1
input to
prior 1 to next

rnn capturing recent occurrence
difficult for long term dependencies

rnn input+hidden -> output
lstm input+hidden+memory -> output
keras, pytorch
















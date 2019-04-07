# Similar Questions Detection for Quora Dataset

A Bidirectional LSTM model using Tensorflow to detect common features between a pair of input questions, and thus compute the cosine similarity. The model supports attention mechanism and is extended to use Gated Relevance Unit (GRU). The model accuracy is approximately 83%.

## Data corpus:

First Quora Dataset Release: Question Pairs <br>
https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs<br>
Place the downloaded corpus in "data" folder.

## Pretrained word embeddings:

Word2Vec : https://code.google.com/archive/p/word2vec/ <br>
GloVe : https://nlp.stanford.edu/projects/glove/ <br>
Place the embeddings in "embeddings" folder. 

## File Descriptions:

- data_formatter.py: a python script to split the downloaded corpus into training and testing data.
- load.py: a python script to index the input data using a vocabulary.
- lstm.py: a Tensorflow based LSTM model to train and test the data.
- gru.py: a Tensorflow based LSTM model to train and test the data.
- attention.py: a python script to achieve attention mechansim.
- matching.py: a python script to compute similarity features between a pair of questions.

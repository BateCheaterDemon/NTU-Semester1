# Q1: Spot the error line(s) in the following code? Assume you have `test_sent` and `svm_pred` data.
```python
1:  from sklearn.metrics import f1_score
2:  def get_f1_score(y_true, y_pred):
3:     micro = f1_Score(y_true, y_pred, average='micro')
4:     macro = f1_Score(y_true,y_pred, average='macro')
5:     print('F1 Micro: '+ str(micro))
6:     print('F1 Macro: '+ str(macro))
7:  print("SVM:")
8:  get_f1_Score(test_sent, svm_pred)
```
```
1. 1
2. 1, 3
3. 3, 4, 8
4. 2, 3, 4
5. 1, 8
```
# Q2: Assuming that you have output predictions from a `SVM` model as `svm_pred` and `LinearRegression` model as `lr_pred` from the same input data, which line of code would you use to calculate the AUC-ROC score of the input data?
```python
1. auc = metric.roc_auc_score(test_sent, svm_pred)
2. auc = metric.roc_auc_score(test_sent, lr_pred)
3. auc = metrics.roc_auc_score(test_sent, svm_pred)
4. auc = metrics.roc_auc_score(test_sent, lr_pred)
5. auc = metric.roc_auc_score(test_sent, (svm_pred > 0.5).astype(int))
6. auc = metrics.roc_auc_score(test_sent, (lr_pred > 0.5).astype(int))
```
# Q3: Identify the line of code that contains an error in the calculation of the BLEU score.
```python
import nltk
from nltk import word_tokenize
from nltk.translate.bleu_score import SmoothingFunction
ref = 'The guard arrived late because it was raining.'
cand = 'The guard arrived late because of the rain.'
```
```python
1. smoothie = SmoothingFunction().method8
2. BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], candidate, weights, smoothing_function=smoothie)
3. weights = (0.2, 0.3, 0.4, 0.1)
4. reference = word_tokenize(ref)
5. candidate = word_tokenize(cand)
```
# Q4: Identify the line of code that contains an error in the training or usage of the Word2Vec model in the following code.
```python
sentences = [
    "Word2Vec is a technique for word embedding.",
    "Embedding words in vector space is powerful for NLP.",
    "Gensim provides an easy way to work with Word2Vec.",
]
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=0)  
model = Word2Vec.load("word2vec.model")

word = "word"
if word in model.wv:
    embedding = model.wv[word]
    print(f"Embedding for '{word}': {embedding}")
else:
    print(f"'{word}' is not in the vocabulary.")
similarity = model.wv.similarity("word", "embedding")
```
```python
1. tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
2. model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=0)
3. model = Word2Vec.load("word2vec.model")
4. embedding = model.wv["word"]
5. similarity = model.wv.similarity("word", "embedding")
```
# Q5: Select the line of code that finds the most similar words to the word `word` using GloVe.
```python
1. similar_words = glove_model.similar(word)
2. similar_words = glove_model.most_similar(word)
3. similar_words = glove_model.similar('word')
4. similar_words = glove_model.most_similar('word')
```

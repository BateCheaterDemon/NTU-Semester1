# Q1: What is the missing code that best fits the follwing code?
```
from sklearn.decomposition import LatentDirichletAllocation

corpus = [
    "I'm designing a document and don't want to get bogged down in what the text actually says",
    "I'm creating a template for various paragraph styles and need to see what they will look like.",
    "I'm trying to learn more about some features of Microsoft Word and don't want to practice on a real document"
]

# TODO: missing code here

lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(input)
```
```
1. 
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

2.
from sklearn.feature_extraction.text import CountVectorizer 
vectorizer = CountVectorizer()
dt_matrix = vectorizer.fit_transform(corpus)

3. 
from sklearn.feature_extraction.text import CountVectorizer 
vectorizer = CountVectorizer()
input = vectorizer.fit_transform(corpus)

4. 
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
input = tfidf_vectorizer.fit_transform(corpus[0])

5. 
from sklearn.feature_extraction.text import CountVectorizer 
vectorizer = CountVectorizer()
input = vectorizer.fit_transform(corpus[0])
```
# Q2: Get the score of the word "and" in each documentfrom the corpus using BM25.
```
from rank_bm25 import BM25Okapi
corpus = [
    "I'm designing a document and don't want to get bogged down in what the text actually says",
    "I'm creating a template for various paragraph styles and need to see what they will look like.",
    "I'm trying to learn more about some features of Microsoft Word and don't want to practice on a real document"
]
tokenized_corpus = [doc.split(" ") for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)
```
```
1. print(bm25.get_scores(["and"]))
2. 
query = ["and"]
tokenized_query = query.split(" ")
doc_scores = bm25.get_scores(tokenized_query)
print([len(sent) for sent in tokenized_corpus])
print(doc_scores)

3. 
query = "and"
tokenized_query = query.split("")
doc_scores = bm25.get_scores(tokenized_query)
print([len(sent) for sent in tokenized_corpus])
print(doc_scores)

4. 
query = "and"
tokenized_query = query.split("")
doc_scores = bm25.get_scores(tokenized_query)
print([len(sent) for sent in tokenized_corpus])
print(doc_scores)

5. 
query = "and"
tokenized_query = query.split("")
doc_scores = bm25.get_score(tokenized_query)
print([len(sent) for sent in tokenized_corpus])
print(doc_scores)
```
# Q3: Fill in the missing code to print the top 5 terms for each topic in the LSA model.
```
lsa = TruncatedSVD(n_components=2, random_state=42)
lsa_matrix = lsa.fit_transform(dt_matrix)
```
```
1. 
terms = vectorizer.get_features_names_out()
for idx, topic in enumerate(lsa.components_):
    print(f"Topic {idx + 1}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:]])
2. 
terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lsa.components_):
    print(f"Topic {idx + 1}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:]])
3. 
terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lsa.components_):
    print(f"Topic {idx + 1}:")
    print([vectorizer.get_feature_names_out()[i] for i in range(topic.argsort()[-5:])])
4. 
terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lsa.components_):
    print(f"Topic {idx + 1}:")
    print(vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:])
5. 
terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lsa.components_):
    print(f"Topic {idx + 1}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.sorted()[-5:]])
```
# Q4: Which function is correct to visualize the topics? (Assume all required libraries are imported)
```
corpus = [
    "I'm designing a document and don't want to get bogged down in what the text actually says",
    "I'm creating a template for various paragraph styles and need to see what they will look like.",
    "I'm trying to learn more about some features of Microsoft Word and don't want to practice on a real document"
]
vectorizer = CountVectorizer()
dt_matrix = vectorizer.fit_transform(corpus)
lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(dt_matrix)
doc_topic_distributions = lda.transform(dt_matrix)
```
```
1. 
pyLDAvis.enable_notebook()
lda_vis = pyLDAvis.lda_mdel.prepare(lda, dt_matrix, vectorizer)
pyLDAvis.display(lda_vis)
2. 
pyLDAvis.enable_notebook()
lda_vis = pyLDAvis.gensim.prepare(lda, dt_matrix, vectorizer)
pyLDAvis.display(lda_vis)
3. 
for i, topic_dist in enumerate(doc_topic_distributions):
    plt.subplot(1, len(doc_topic_distributions)+1, i+1)
    plt.bar(range(len(topic_dist)))
    plt.xlabel("Topic")
    plt.ylabel("Probability")
    plt.title(f"Document #{i + 1}")
plt.tight_layout()
plt.show()
4. 
for i, topic_dist in enumerate(doc_topic_distributions):
    plt.subplot(1, len(doc_topic_distributions), i+1)
    plt.bar(range(len(topic_dist)))
    plt.xlabel("Topic")
    plt.ylabel("Probability")
    plt.title(f"Document #{i + 1}")
plt.tight_layout()
plt.show()
5. 
for i, topic_dist in enumerate(doc_topic_distributions):
    plt.subplot(1, len(doc_topic_distributions), i+1)
    plt.bar(range(len(topic_dist)), topic_dist)
    plt.xlabel("Topic")
    plt.ylabel("Probability")
    plt.title(f"Document #{i + 1}")
plt.tight_layout()
plt.show()
```
# Q5: Select the correct code to apply PCA to reduce the dimensionality of the TF-IDF matrix into 3 dimensions.
```
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I'm designing a document and don't want to get bogged down in what the text actually says",
    "I'm creating a template for various paragraph styles and need to see what they will look like.",
    "I'm trying to learn more about some features of Microsoft Word and don't want to practice on a real document"
]

tfidf_vectorizer = TfidfVectorizer()
tfidf_data = tfidf_vectorizer.fit_transform(corpus)
```
```
1. 
pca = PCA(svd_solver='full')
pca_result = pca.fit_transform(tfidf_data.toarray())
2.
pca = PCA(n_components=2, svd_solver='full')
pca_result = pca.fit_transform(tfidf_data.toarray())
3.
pca = PCA(svd_solver='full')
pca_result = pca.fit_transform(tfidf_data)
4.
pca = PCA(n_components=2, svd_solver='full')
pca_result = pca.fit_transform(tfidf_data)
5. 
pca = PCA(n_components=3, svd_solver='full')
pca_result = pca.fit_transform(tfidf_data)
```

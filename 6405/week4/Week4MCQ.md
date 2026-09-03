# Q1: In the following code, you are using a `MultinomialNB` model to make predictions on the test data. If you wanted to change the model to use `GaussianNB` instead, which line of code would need to be modified?
```
from sklearn.naive_bayes import MultinomialNB # Line 1
nb = MultinomialNB()                          # Line 2        
nb.fit(X_train, y_train)                      # Line 3
predictions = nb.predict(X_test)              # Line 4
```
```
1. Line 1 and 2
2. Line 1, 2 and 3
3. Line 1, 2, 3 and 4
4. Line 1, 2 and 4
5. Line 2 and 3
```
# Q2: To adjust the regularization strength of the SVM model, which parameter should be modified?
```
from sklearn import svm
svm = svm.SVC(kernel='linear')
```
```
1. svm = svm.SVC(kernel='linear', degree=2)
2. svm = svm.SVC(kernel='linear', gamma='auto')
3. svm = svm.SVC(kernel='linear', coef0=1.0)
4. svm = svm.SVC(kernel='linear', probability=True)
5. svm = svm.SVC(kernel='linear', C=0.5)
```
# Q3: To adjust the length scale of the RBF kernel in the GaussianProcessClassifier, which parameter should be modified?
```
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
gpc = GaussianProcessClassifier(kernel=RBF())
```
```
1. gpc = GaussianProcessClassifier(kernel=RBF(length_scale_bounds=(1e-2, 1e2)))
2. gpc = GaussianProcessClassifier(kernel=RBF(), length_scale_bounds=(1e-2, 1e2))
3. gpc = GaussianProcessClassifier(kernel=RBF(length_scale=1.5))
4. gpc = GaussianProcessClassifier(kernel=RBF(), length_scale=1.5)
5. gpc = GaussianProcessClassifier(kernel=RBF(length_scale=1.0))
```
# Q4: To fit the `LinearRegression` model to training data `X_train` and `y_train`, which method should be used?
```
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
```
```
1. lr.score(X_train, y_train)
2. lr.transform(X_train)
3. lr.predict(X_train)
4. lr.fit(X_train, y_train)
5. lr.compile(X_train)
```
# Q5: To change the number of clusters in the KMeans model, which parameter should be modified?
```
from sklearn.cluster import KMeans
kmeans = KMeans(random_state=42)
```
```
1. kmeans = KMeans(n_clusters=2, random_state=42)
2. kmeans = KMeans(n_init=2, random_state=42)
3. kmeans = KMeans(max_iter=3, random_state=42)
4. kmeans = KMeans(n_clusters=8, random_state=42)
5. kmeans = KMeans(n_init=8, random_state=42)
```

# Q1: Which of the following do not split into 5-fold?? 
```python
1. GridSearchCV(classifier, param_grid)
2. GridSearchCV(classifier, param_grid, cv=5)
3. cross_val_score(best_classifier, X, y, scoring='f1_macro')
4. cross_val_score(best_classifier, X, y, cv=5, scoring='f1_macro')
5. None of the above
```
# Q2: What is the missing code?
```python
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train_index, val_index in kf.split(X):
    # missing code
```
```python
1. 
X_train, X_val = X[train_index], X[train_index]
y_train, y_val = y[train_index], y[val_index]
2. 
X_train, X_val = X[val_index], X[val_index]
y_train, y_val = y[train_index], y[train_index]
3.
X_train, y_train = X[train_index], y[train_index]
X_val, y_val = X[val_index], y[val_index]
4. 
X_train, y_train = X[val_index], y[val_index]
X_val, y_val = X[train_index], y[train_index]
5. 
X_train, y_train = X[train_index], y[val_index]
X_val, y_val = X[train_index], y[val_index]
```
# Q3: Which is the best explanation for the purpose of the following code snippet?
```python
vocab_size = len(vectorizer.get_feature_names_out())
embedding_dim = 100
hidden_dim = 128
output_dim = len(np.unique(y))
```
```python
1. It calculates the length of the feature names extracted using a vectorizer.
2. It defines the dimensions for word embeddings, hidden layers, and output layers for a neural network model.
3. It computes the unique output classes from the target variable y.
4. It initializes the vocabulary size along with the embedding, hidden, and output dimensions for a machine learning algorithm.
```
# Q4: What is the purpose of the following code snippet?
```python
X_train_tensor = torch.tensor(X_train.toarray(), dtype=torch.long)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_val_tensor = torch.tensor(X_val.toarray(), dtype=torch.long)
y_val_tensor = torch.tensor(y_val, dtype=torch.long)
train_data = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_data, batch_size=4)
model = LSTMClassifier(vocab_size, embedding_dim, hidden_dim, output_dim)
```
```python
1. It converts the training and validation data into PyTorch tensors, creates a DataLoader, and initializes an LSTM classifier model.
2. It normalizes the training and validation data, performs data augmentation, and defines an LSTM classifier model.
3. It encodes the training and validation data, splits the data into batches, and trains an LSTM classifier model.
4. It preprocesses the training and validation data, performs feature selection, and trains an LSTM classifier model.
```
# Q5: Choose the correct line of code.
```python
1. torch.nn.utils.clip_grad_value_(model.parameters())
2. torch.nn.utils.clip_grad_value_(clip_value=0.5)
3. torch.nn.utils.clip_grad_value_(clip_value='0.5')
4. torch.nn.utils.clip_grad_value_(model.parameters(), clip_value='0.5')
```

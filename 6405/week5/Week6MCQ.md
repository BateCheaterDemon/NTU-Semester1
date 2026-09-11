# Q1: In the RNNModel class, what is the purpose of the `self.embedding` layer?
```python
class RNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.rnn(x)
        out = self.fc(out)
        return out
```
```python
1. To convert input sequences of indices into dense vector representations.
2. To apply a linear transformation to the output of the RNN.
3. To initialize the hidden states of the RNN for each sequence.
4. To implement the activation function for the RNN outputs.
5. To concatenate the outputs of multiple RNN layers.
```
# Q2: What needs to be adjusted in the Q1's code to implement a bidirectional RNN?
```python
1. None
2. 
self.rnn = nn.RNN(embedding_dim, hidden_dim)
self.fc = nn.Linear(hidden_dim * 2, output_size)
3. 
self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
self.fc = nn.Linear(hidden_dim * 2, output_size)
4. 
self.rnn = nn.RNN(batch_first=True, bidirectional=True)
self.fc = nn.Linear(hidden_dim * 2, output_size)
5. self.rnn = nn.RNN(bidirectional=True)
```
# Q3: What needs to be adjusted in the Q1's code to implement a LSTM?
```python
1. None
2. self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
3. self.rnn = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
4. self.fc = nn.Linear(hidden_dim * 2, hidden_dim)
5. 
self.rnn = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
self.fc = nn.Linear(hidden_dim * 2, output_size)
```
# Q4: What is the purpose of `optimizer.zero_grad()` in the training loop of the RNN model?
```python
1. It initializes the model weights for the current epoch.
2. It clears the gradients of all optimized tensors before the backward pass.
3. It calculates the loss for the current batch of data.
4. It updates the model parameters after the backward pass.
5. It sets the model to evaluation mode.
```
# Q5: To adjust the learning rate of Adam optimizer, which of the following methods works?
```python
1. optimizer = optim.Adam(model.parameters())
2. optimizer = optim.Adam(model.parameters(), lr=1e-2)
3. optimizer = optim.Adam(model.parameters(), lr=1e-3)
4. optimizer = optim.Adam(model.parameters(), eps=1e-2)
5. optimizer = optim.Adam(model.parameters(), eps=1e-3)
```

# Q1: Why `None` is returned in the `forward` method below?
```python
class DecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size):
        super(DecoderRNN, self).__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, output_size)

    def forward(self, encoder_outputs, encoder_hidden, target_tensor=None):
        batch_size = encoder_outputs.size(0)
        decoder_input = torch.empty(batch_size, 1, dtype=torch.long, device=device).fill_(0)
        decoder_hidden = encoder_hidden
        decoder_outputs = []

        for i in range(MAX_LENGTH):
            decoder_output, decoder_hidden  = self.forward_step(decoder_input, decoder_hidden)
            decoder_outputs.append(decoder_output)

            if target_tensor is not None:
                decoder_input = target_tensor[:, i].unsqueeze(1) 
            else:
                _, topi = decoder_output.topk(1)
                decoder_input = topi.squeeze(-1).detach()

        decoder_outputs = torch.cat(decoder_outputs, dim=1)
        decoder_outputs = F.log_softmax(decoder_outputs, dim=-1)
        return decoder_outputs, decoder_hidden, None
```
```
1. for evaluation in the training loop
2. for accuracy in the training loop
3. for consistency in the training loop
4. for uniformity in the training loop
5. None of the above
```
# Q2: What's the missing line(s) in the `AttnDecoderRNN` class?
```python
class AttnDecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p=0.1):
        super(AttnDecoderRNN, self).__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        # missing line(s)
        self.dropout = nn.Dropout(dropout_p)
```
```python
1. 
self.attention = BahdanauAttention(hidden_size)
2. 
self.attention = BahdanauAttention(hidden_size)
self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)
self.out = nn.Linear(hidden_size, output_size)
3. 
self.attention = BahdanauAttention(hidden_size)
self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)
self.linear = nn.Linear(hidden_size, output_size)
self.out = nn.Linear(hidden_size, output_size)
4.
self.attention = BahdanauAttention(hidden_size)
self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)
5. 
self.attention = BahdanauAttention(hidden_size)
self.out = nn.Linear(hidden_size, output_size)
```
# Q3: What's the missing line(s) in the `BahdanauAttention` class?
```python
class BahdanauAttention(nn.Module):
    def __init__(self, hidden_size):
        super(BahdanauAttention, self).__init__()
        # missing line(s)
```
```python
1. 
self.Wa = nn.Linear(hidden_size, hidden_size)
self.Ua = nn.Linear(hidden_size, hidden_size)
self.Va = nn.Linear(hidden_size, hidden_size)
2. 
self.Wa = nn.Linear(hidden_size, 1)
self.Ua = nn.Linear(hidden_size, 1)
self.Va = nn.Linear(hidden_size, 1)
3. 
self.Wa = nn.Linear(hidden_size, 1)
self.Ua = nn.Linear(hidden_size, hidden_size)
self.Va = nn.Linear(hidden_size, hidden_size)
4. 
self.Wa = nn.Linear(hidden_size, hidden_size)
self.Ua = nn.Linear(hidden_size, 1)
self.Va = nn.Linear(hidden_size, hidden_size)
5. 
self.Wa = nn.Linear(hidden_size, hidden_size)
self.Ua = nn.Linear(hidden_size, hidden_size)
self.Va = nn.Linear(hidden_size, 1)
```
# Q4: What's the missing line(s) in the `MultiHeadAttention` class?
```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        # missing line(s)
```
```python
1. 
self.W_q = nn.Linear(d_model, d_model)
self.W_k = nn.Linear(d_model, d_model)
self.W_v = nn.Linear(d_model, d_model)
self.W_o = nn.Linear(d_model, d_model)
2. 
self.W_q = nn.Linear(d_model, d_k)
self.W_k = nn.Linear(d_model, d_k)
self.W_v = nn.Linear(d_model, d_k)
self.W_o = nn.Linear(d_model, d_k)
3. 
self.W_q = nn.Linear(d_model, d_k)
self.W_k = nn.Linear(d_model, d_k)
self.W_v = nn.Linear(d_model, num_heads)
self.W_o = nn.Linear(d_model, num_heads)
4. 
self.W_q = nn.Linear(d_model, num_heads)
self.W_k = nn.Linear(d_model, num_heads)
self.W_v = nn.Linear(d_model, num_heads)
self.W_o = nn.Linear(d_model, num_heads)
5. 
self.W_q = nn.Linear(d_model, self.d_k)
self.W_k = nn.Linear(d_model, self.d_k)
self.W_v = nn.Linear(d_model, self.d_k)
self.W_o = nn.Linear(d_model, self.d_k)
```
# Q5: What's the missing line(s) in the `PositionalEncoding` class?
```python
class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        super(PositionWiseFeedForward, self).__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        super(PositionalEncoding, self).__init__()
        
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        self.register_buffer('pe', pe.unsqueeze(0))

    def forward(self, x):
        # missing line(s)
```
```python
1. return x
2. return self.pe[:x]
3. return x + self.pe
4. return x + self.pe[:, :x.size(0)]
5. return x + self.pe[:, :x.size(1)]
```

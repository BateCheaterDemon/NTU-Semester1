# Q1: What does the following code do in the context of a LLM model?
```python
model.eval()
```
```python
1. Enable evaluation mode for the model.
2. Move the model to a specified device (e.g., GPU or CPU).
3. Compile the model for training.
4. Freeze the model's parameters.
5. Initialize the model's weights.
```
# Q2: Which library is used to tokenize text and perform Masked Language Modeling in the provided code snippet?
```python
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertForMaskedLM.from_pretrained('bert-base-uncased').to(device).eval()
```
```python
1. NLTK
2. spaCy
3. transformers
4. TensorFlow
5. PyTorch
```
# Q3: Which of the following is an appropriate input sentence for the following tokenizer with the intention of generating the word of the masked token?
```python
roberta_tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
```
```python
1. sentence = "NTU's EE6405 course is an awesome [MASK]."
2. sentence = "NTU's EE6405 course is an awesome <MASK>."
3. sentence = "NTU's EE6405 course is an awesome [mask]."
4. sentence = "NTU's EE6405 course is an awesome <mask>."
5. sentence = "NTU's EE6405 course is an awesome course."
```
# Q4: Which of the following is an appropriate input for the tokenizer in the task of multiple choice question answering?
```python
question = "What does NLP stands for?"
answers = ["Computer Vision", "Natural Language Processing", "AI"]
tokenizer = AutoTokenizer.from_pretrained("xlnet/xlnet-base-cased")
```
```python
1. encoding = tokenizer(question, answers, return_tensors="pt", padding=True)
2. encoding = tokenizer([question], answers, return_tensors="pt", padding=True)
3. encoding = tokenizer([question]*2, answers, return_tensors="pt", padding=True)
4. encoding = tokenizer([question]*3, answers, return_tensors="pt", padding=True)
5. encoding = tokenizer([question]*4, answers, return_tensors="pt", padding=True)
```
# Q5: When training a model using fine-tuning techniques, which of the following steps is not typically performed?
```python
1. model.train()
2. optimizer.zero_grad()
3. torch.no_grad()
4. loss.backward()
5. outputs = model(data, target)
```

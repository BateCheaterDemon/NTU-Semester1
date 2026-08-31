# Q1: What is the output of the following code?
```
NER = spacy.load("en_core_web_sm")  # Load SpaCy's small English model
sentence = "He then moved within the same university to become the Merton Professor of English Language and Literature and Fellow of Merton College, and held these positions from 1945 until his retirement in 1959."

doc = NER(sentence)
print([f"{entity.text}[{entity.label_}]" for entity in doc.ents])
```
```
1. ['He[PERSON]', 'university[ORG]', 'English Language and Literature and Fellow of Merton College[WORK_OF_ART]', '1945[DATE]', '1959[DATE]']
2. ['He[PERSON]', 'English Language and Literature and Fellow of Merton College[WORK_OF_ART]', '1945[DATE]', '1959[DATE]']
3. ['He[PERSON]', '1945[DATE]', '1959[DATE]'] 
4. ['English Language and Literature and Fellow of Merton College[WORK_OF_ART]', '1945[DATE]', '1959[DATE]']
5. ['He[PERSON]', 'university[ORG]', '1945[DATE]', '1959[DATE]']
```
# Q2: How can we find definition of the special token `_SP` used in SpaCy by coding? What is the definition? Answer in the form: code and output
```
1. spacy.explain('_SP') and "white space"
2. spacy.explain('_SP') and "space"
3. spacy.explain('_SP') and "whitespace"
4. spacy.explains('_SP') and "whitespace"
5. spacy.explains('_SP') and "space"
```
# Q3: What is the output of `the` and `?` in the following code? Answer is in the form of (Token.pos_, Token.tag_).
```
NER = spacy.load("en_core_web_sm")  # Load SpaCy's small English model
sentence = "You know the greatest lesson of history?"

doc = NER(sentence)
for token in doc:
    print(token.pos_, token.tag_)
```
```
1. (DET, DT) and (., PUNCT)
2. (DET, DET) and (., .)
3. (DET, DET) and (PUNCT, PUNCT)
4. (DET, DT) and (., .)
5. (DET, DT) and (PUNCT, .)
```
# Q4: What is the output of `the` and `greatest` in the following code? Answer is in the form of (Token.text, Token.orth_).
```
NER = spacy.load("en_core_web_sm")  # Load SpaCy's small English model
sentence = "You know the greatest lesson of history?"

doc = NER(sentence)
for token in doc:
    print(token.text, token.orth_)
```
```
1. (the, the) and (greatest, greatest)
2. (the, a) and (greatest, great)
3. (a, the) and (great, greatest)
4. (a, a) and (great, great)
5. (the, the) and (great, great)
```
# Q5: What is the missing code in the blank below?
```
sentence = "You know the greatest lesson of history?"
doc = NER(sentence)

print('{:<15} | {:<10} | {:<15} | {:<20}'.format('Token','Relation','Head','Children'))
print('-'*70)

for token in doc:
    #Print the token, dependency nature, head and all dependents of the token
    print("{:<15} | {:<10} | {:<15} | {:<20}"
          .format(__))                 
```
```
1. str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children])
2. str(token.text), str(token.dep), str(token.head.text), str([child for child in token.children])
3. str(token), str(token.dep_), str(token.head), str([child for child in token.children])
4. str(token), str(token.dep), str(token.head), str(token.children)
5. str(token.text), str(token.dep), str(token.head.text), str(token.children)
```

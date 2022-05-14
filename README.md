# About

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

[![html](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)

In this project I have created a sentence similarity score calculator which takes two sentences as input and shows their corresponding similarity score which shows show similar the sentences are. The more close to 1 the score is the more similar the sentences are, the close to 0 the score is the more dissilimar the sentences are.

# Information on API call

The Algorithm is ready to be deployed as a API server endpoint where the Request and Response body should be in the following format:

Request body: {“text1”: ”I am new here but .......”, ”text2”: ”The movie released recently and ......”}</br>Response body: {“similarity score”: 0.6 }

Note: “text1”, “text2”, and “similarity score” keys should be kept as it is, without any change.

## Approach 1

In this approach I used word embeddings and n_similarity method provided by gensim library to calculate the cosine similarity between the sentences. Due to large size of the word2vec model, the model could not be deployed at heroku.

## Approach 2

I used all-Mini-LM-L6-v2 SBERT transformer model to embed the sentences. Then, I calculated the cosine similarity between the sentences. This approach is more refined than the previous approach. The code for this approach is written in the app_sentence_transformer.py file.

### Required Libraries
- Flask
- nltk
- gensim
- re
- tqdm
- pandas

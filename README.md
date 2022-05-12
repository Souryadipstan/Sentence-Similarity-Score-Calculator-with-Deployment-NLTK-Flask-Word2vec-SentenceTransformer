# About

In this project I have created a sentence similarity score calculator which takes two sentences as input and shows their corresponding similarity score which shows show similar the sentences are. The more close to 1 the score is the more similar the sentences are, the close to 0 the score is the more dissilimar the sentences are.

# Information on API call

The Algorithm is ready to be deployed as a API server endpoint where the Request and Response body should be in the following format:

Request body: {“text1”: ”I am new here but .......”, ”text2”: ”The movie released recently and ......”}   Response body: {“similarity score”: 0.6 }

Note: “text1”, “text2”, and “similarity score” keys should be kept as it is, without any change.

Due to large size of the word2vec model, the model could not be deployed at heroku.

### Required Libraries
- Flask
- nltk
- gensim
- re
- tqdm
- pandas

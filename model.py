import re
from tqdm import tqdm

from nltk.stem import WordNetLemmatizer  
from nltk.corpus import stopwords  
from nltk import word_tokenize 

from gensim.models import word2vec 
import gensim
import gensim.downloader as api

# wordmodelfile="/Users/sourya/Desktop/precily/GoogleNews-vectors-negative300.bin.gz"
# wordmodel= gensim.models.KeyedVectors.load_word2vec_format(wordmodelfile, binary=True)

wordmodel = api.load('word2vec-google-news-300')

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def preprocess(dataframe_column):

    preprocessed_text = []

    for sentence in tqdm(dataframe_column.values):
        sent = decontracted(sentence)
        sent = sent.replace('\\r', ' ')
        sent = sent.replace('\\"', ' ')
        sent = sent.replace('\\n', ' ')
        sent = re.sub('[^A-Za-z0-9]+', ' ', sent)

        sent = ' '.join(e for e in sent.split() if e not in stopwords.words('english'))
        preprocessed_text.append(sent.lower().strip())
    
    return preprocessed_text

def word_tokenizer(text):
            #tokenizes and stems the text
            tokens = word_tokenize(text)
            lemmatizer = WordNetLemmatizer() 
            tokens = [lemmatizer.lemmatize(t) for t in tokens]
            return tokens

def similarity(dataframe,dataframe_column_1,dataframe_column_2):

    similarity = [] # List to store similarity score



    for idx in dataframe.index:
    
        s1 = dataframe_column_1[idx]
        s2 = dataframe_column_2[idx]
        
        if s1==s2:
                 similarity.append(1.0) # 0 means highly dissimilar
                
        else:   

            s1_words = word_tokenizer(s1)
            s2_words = word_tokenizer(s2)
            
           
            
        vocab = wordmodel 
            
        if len(s1_words and s2_words) == 0:
                similarity.append(0.0)

        else:
                
            for word in s1_words.copy(): #remove sentence words not found in the vocab

                if (word not in vocab):
                           
                            
                    s1_words.remove(word)
                        
                    
            for word in s2_words.copy(): #remove sentence words not found in the vocab

                if (word not in vocab):
                           
                    s2_words.remove(word)
                            
                            
        similarity.append((wordmodel.n_similarity(s1_words, s2_words)))

    return similarity

from flask import Flask,render_template,request,jsonify
import pandas as pd
import model
from model import decontracted,word_tokenizer

app2 = Flask(__name__)

@app2.get("/")
def home():

    json_ = request.get_json()
    json_ = [json_]
    dataframe = pd.DataFrame(json_)
    print(dataframe)
    preprocessed_text_1 = model.preprocess(dataframe['text1'])
    preprocessed_text_2 = model.preprocess(dataframe['text2'])
    similarity_score = model.similarity(dataframe,dataframe['text1'],dataframe['text2'])
    return jsonify({"similarity score" : str(similarity_score[0])})

if __name__ == "__main__":

    app2.run(debug = True)

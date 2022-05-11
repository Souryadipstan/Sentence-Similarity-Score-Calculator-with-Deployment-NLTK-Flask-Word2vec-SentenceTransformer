from flask import Flask,render_template,request,jsonify
import pandas as pd
import model
from model import decontracted,word_tokenizer
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.get("/")
def home():

    return render_template("home_page.html")

@app.post("/response")
def response():

    text1 = request.form['text1']
    text2 = request.form['text2']
    df_dict = {"text1" : text1,"text2" : text2}
    dataframe = pd.DataFrame([df_dict])
    preprocessed_text_1 = model.preprocess(dataframe['text1'])
    preprocessed_text_2 = model.preprocess(dataframe['text2'])
    similarity_score = model.similarity(dataframe,dataframe['text1'],dataframe['text2'])
    return render_template("submit_page.html", s = similarity_score[0])

if __name__ == "__main__":

    app.run(debug = True)

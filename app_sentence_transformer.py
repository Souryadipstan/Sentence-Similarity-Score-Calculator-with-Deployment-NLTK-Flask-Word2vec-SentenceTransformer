from flask import Flask,request,jsonify
from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

app = Flask(__name__)

@app.get("/")
def home():

    json_ = request.get_json()
    json_ = [json_]
    dataframe = pd.DataFrame(json_)
    print(dataframe)
    embeddings1 = model.encode(dataframe['text1'], convert_to_tensor=True)
    embeddings2 = model.encode(dataframe['text2'], convert_to_tensor=True)
    cosine_scores = util.cos_sim(embeddings1, embeddings2)
    return jsonify({"similarity score" : str(cosine_scores[0][0].item())})

if __name__ == "__main__":

    app.run(debug = True)
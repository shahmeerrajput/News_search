from flask import Flask ,render_template , request , jsonify
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
app = Flask(__name__,template_folder='templates',static_folder='static')
@app.route('/', methods=['GET'])
def home():
    return render_template('search_new.html')
def predict(text):
    df1 = pd.read_excel('LiveDataSetOfNews.xlsx')
    data =df1["Headline"].values.tolist()
    documents_clean = []
    for d in data:
        # Remove Unicode
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', str(d))
        # Remove Mentions
        document_test = re.sub(r'@\w+', '', document_test)
        # Lowercase the document
        document_test = document_test.lower()
        # Lowercase the numbers
        document_test = re.sub(r'[0-9]', '', document_test)
        # Remove the doubled space
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        documents_clean.append(document_test)
    # Instantiate a TfidfVectorizer object
    vectorizer = TfidfVectorizer()
    # It fits the data and transform it as a vector
    X = vectorizer.fit_transform(documents_clean)
    # Convert the X as transposed matrix
    X = X.T.toarray()
    # Create a DataFrame and set the vocabulary as the index
    df = pd.DataFrame(X, index=vectorizer.get_feature_names())
    # Convert the query become a vector
    q = [text]
    q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0],)
    sim = {}
    # Calculate the similarity
    for i in range(len(documents_clean)):
        sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
    # Sort the values 
    sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
    # Print the articles and their similarity values
    for k, v in sim_sorted:
        if v >= 0.7 or str(q) in str(documents_clean[k]):
            p = ['News is Valid',f'similarity values: {v}', f'Headline: {documents_clean[k]}', f'Source: {df1.Link[k]}']
            break
        elif v < 0.7 or str(q) not in str(documents_clean[k]):
            p =["Remarks: News is Invalid"]
            break
    return p

@app.route('/', methods=['POST'])

def webapp():
    text = request.form['text']
    prediction = predict(text)
    return render_template('search_new.html', text=text, result=prediction)
    
@app.route('/predict/', methods=['GET','POST'])
def api():
    text = request.args.get("text")
    prediction = predict(text)
    return jsonify(prediction=prediction)
if __name__ == "__main__":
    app.run()
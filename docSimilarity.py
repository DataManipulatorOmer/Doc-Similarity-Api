from flask import Flask, request, jsonify
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
#-----------------------------------------------------------
def checkSimilarity(documents):
    #TfidfVectorizer
    vectorizer = TfidfVectorizer()
    # Fit and transform t
    tfIdfMatrix = vectorizer.fit_transform(documents)
    # Cosine similarity
    simMatrix = cosine_similarity(tfIdfMatrix, tfIdfMatrix)
    return simMatrix, documents
#-----------------------------------------------------------
def simMatrixDisplay(simMatrix, documents):
    sns.set(font_scale=1.2)
    plt.figure(figsize=(8, 6))
    sns.heatmap(simMatrix, annot=True, cmap="YlGnBu", fmt=".2f", xticklabels=range(len(documents)), yticklabels=range(len(documents)))
    plt.xlabel("Document Index")
    plt.ylabel("Document Index")
    plt.title("Cosine Similarity between Documents")
    plt.savefig("simMatrix.png")  
    plt.close()

@app.route('/api/similarity', methods=['POST'])
def get_similarity():
    data = request.json
    documents = data.get('documents', [])
    if not documents:
        return jsonify({'error': 'No documents provided'})
    simMatrix, documents = checkSimilarity(documents)
    simMatrixDisplay(simMatrix, documents)
    return jsonify({'simMatrix': simMatrix.tolist(), 'image_path': 'd:/PythonProj/APIS/static/simMatrix.png'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import re
import string
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# -----------------------------
# Download NLTK resources
# -----------------------------
nltk.download("punkt")
nltk.download("stopwords")

# If using newer NLTK versions, uncomment the next line if needed
# nltk.download("punkt_tab")

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Debug Information
# -----------------------------
print("=" * 50)
print("Current Working Directory:")
print(os.getcwd())

print("\nTemplates Folder Exists:")
print(os.path.exists("templates"))

print("\nIndex.html Exists:")
print(os.path.exists("templates/index.html"))

print("\nModel Folder Exists:")
print(os.path.exists("model"))

print("=" * 50)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model/model.pkl")
tfidf = joblib.load("model/tfidf.pkl")

# -----------------------------
# NLP Tools
# -----------------------------
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# -----------------------------
# Text Preprocessing
# -----------------------------
def preprocess(text):
    text = text.lower()

    # Remove HTML
    text = re.sub(r"<.*?>", "", text)

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    tokens = [stemmer.stem(word) for word in tokens]

    return " ".join(tokens)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Prediction Route
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    review = request.form.get("review", "")

    if review.strip() == "":
        return render_template(
            "index.html",
            prediction="Please enter a review.",
            review=""
        )

    cleaned = preprocess(review)

    vector = tfidf.transform([cleaned])

    prediction = model.predict(vector)[0]

    if prediction == "positive" or prediction == 1:
        result = "Positive 😊"
    else:
        result = "Negative 😞"

    return render_template(
        "index.html",
        prediction=result,
        review=review
    )

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
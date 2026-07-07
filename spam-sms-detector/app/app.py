from flask import Flask, render_template, request
import joblib
import nltk

from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

# -----------------------------
# Download NLTK resources
# -----------------------------
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = BASE_DIR / "app" / "templates"
STATIC_DIR = BASE_DIR / "app" / "static"
MODEL_DIR = BASE_DIR / "models"

# -----------------------------
# Debug Prints
# -----------------------------
print("=" * 50)
print("BASE_DIR       :", BASE_DIR)
print("TEMPLATE_DIR   :", TEMPLATE_DIR)
print("STATIC_DIR     :", STATIC_DIR)
print("MODEL_DIR      :", MODEL_DIR)
print("Template exists:", TEMPLATE_DIR.exists())
print("Index exists   :", (TEMPLATE_DIR / "index.html").exists())
print("Model exists   :", (MODEL_DIR / "model.pkl").exists())
print("Vectorizer     :", (MODEL_DIR / "vectorizer.pkl").exists())
print("=" * 50)

# -----------------------------
# Flask App
# -----------------------------
app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(STATIC_DIR)
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load(MODEL_DIR / "model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")

# -----------------------------
# NLP Objects
# -----------------------------
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

# -----------------------------
# Text Preprocessing
# -----------------------------
def transform_text(text):
    text = text.lower()

    words = word_tokenize(text)

    filtered = []
    for word in words:
        if word.isalnum():
            filtered.append(word)

    cleaned = []
    for word in filtered:
        if word not in stop_words:
            cleaned.append(word)

    stemmed = []
    for word in cleaned:
        stemmed.append(ps.stem(word))

    return " ".join(stemmed)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        prediction=None,
        message=""
    )
# -----------------------------
# Prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    message = request.form["message"]

    transformed_message = transform_text(message)

    # Convert sparse matrix to dense array
    vector = vectorizer.transform([transformed_message]).toarray()

    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "🚨 Spam Message"
    else:
        result = "✅ Ham Message"

    return render_template(
        "index.html",
        prediction=result,
        message=message
    )

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
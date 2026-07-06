# 🎬 Movie Review Sentiment Analysis using Machine Learning

An end-to-end Natural Language Processing (NLP) project that predicts whether a movie review expresses a **Positive** or **Negative** sentiment using Machine Learning. The project demonstrates the complete NLP workflow—from raw text preprocessing to model deployment with a Streamlit web application.

---

## 📌 Project Overview

This application analyzes movie reviews and predicts their sentiment using classical NLP techniques and Machine Learning algorithms.

The pipeline includes:

- Data Collection
- Data Cleaning
- Text Preprocessing
- Feature Extraction (TF-IDF)
- Model Training
- Model Evaluation
- Model Saving
- Streamlit Deployment

---

## 🚀 Features

- Predicts movie review sentiment
- Cleans and preprocesses text
- Uses TF-IDF Vectorization
- Trains multiple Machine Learning models
- Evaluates model performance
- Saves trained model using Pickle/Joblib
- Interactive Streamlit web interface

---

## 🧠 NLP Pipeline

```text
Raw Text
    │
    ▼
Lowercase Conversion
    │
    ▼
Tokenization
    │
    ▼
Stopword Removal
    │
    ▼
Stemming / Lemmatization
    │
    ▼
TF-IDF Vectorization
    │
    ▼
Machine Learning Model
    │
    ▼
Sentiment Prediction
```

---

## 🔄 Project Workflow

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Text Preprocessing
   │
   ▼
TF-IDF Feature Extraction
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Save Model
   │
   ▼
Streamlit Web App
   │
   ▼
User Input
   │
   ▼
Sentiment Prediction
```

---

## 📂 Dataset

**IMDb Movie Reviews Dataset**

The dataset contains thousands of movie reviews labeled as:

- Positive
- Negative

Example:

| Review | Sentiment |
|---------|-----------|
| Amazing movie | Positive |
| Worst acting ever | Negative |
| Excellent story | Positive |
| Waste of money | Negative |

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Handling | Pandas, NumPy |
| NLP | NLTK |
| Feature Extraction | CountVectorizer, TF-IDF |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Model Saving | Pickle / Joblib |

---

## 📁 Project Structure

```text
Movie-Review-Sentiment-Analysis/
│
├── data/
│   └── imdb_reviews.csv
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── models/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Review-Sentiment-Analysis.git
```

```bash
cd Movie-Review-Sentiment-Analysis
```

---

### Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train.py
```

This will:

- Load dataset
- Clean text
- Preprocess reviews
- Create TF-IDF features
- Train the classifier
- Evaluate performance
- Save the trained model

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

## 📊 Machine Learning Models

The project can be trained using:

- Multinomial Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)

---

## 📈 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 💬 Example

### Input

```
This movie was absolutely fantastic!
```

### After Preprocessing

```
movie absolut fantast
```

### Prediction

```
😊 Positive
```

---

### Input

```
The movie was boring and a waste of time.
```

### Prediction

```
😞 Negative
```

---

## 🎯 Skills Demonstrated

- Data Cleaning
- Text Preprocessing
- Tokenization
- Stopword Removal
- Stemming
- Lemmatization
- Feature Engineering
- TF-IDF
- Bag of Words
- Machine Learning
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- End-to-End NLP Pipeline

---

## 🔮 Future Improvements

- Neutral sentiment prediction
- Emotion detection
- Confidence score
- Word Cloud visualization
- Transformer models (BERT, RoBERTa)
- Explainable AI
- Docker support
- Cloud deployment (AWS, Azure, GCP)
- REST API using Flask/FastAPI

---

## 📚 Learning Outcomes

This project provides hands-on experience with the complete NLP workflow:

- Data Collection
- Data Cleaning
- Text Preprocessing
- Feature Extraction
- Machine Learning
- Model Evaluation
- Model Saving
- Streamlit Deployment

It serves as a strong foundation for advanced NLP topics such as Semantic Search, Named Entity Recognition (NER), Question Answering, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs).

---

## ⭐ If you found this project helpful, consider giving it a star on GitHub!
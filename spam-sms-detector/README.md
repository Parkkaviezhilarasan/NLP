# 📩 Spam SMS Detector using Machine Learning

A Flask-based web application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Features

- Detects whether an SMS is **Spam** or **Ham**
- Text preprocessing using NLP
- TF-IDF Vectorization
- Machine Learning classification using Support Vector Classifier (SVC)
- Interactive Flask web interface
- Real-time prediction

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib
- HTML
- CSS

---

## 📂 Project Structure

```
spam-sms-detector/
│
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── data/
│   └── spam.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── spam-sms.ipynb
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spam-sms-detector.git
```

### 2. Navigate to the project

```bash
cd spam-sms-detector
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app/app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 🧠 Machine Learning Pipeline

1. Load SMS dataset
2. Data Cleaning
3. Text Preprocessing
   - Lowercase conversion
   - Tokenization
   - Remove punctuation
   - Remove stopwords
   - Stemming
4. TF-IDF Vectorization
5. Train Support Vector Classifier (SVC)
6. Save trained model using Joblib
7. Deploy using Flask

---

## 📸 Sample Predictions

### ✅ Ham

```
Hi, I'll call you after the meeting.
```

Prediction

```
Ham Message
```

### 🚨 Spam

```
Congratulations! You have won a FREE ₹50,000 cash prize. Click here to claim now.
```

Prediction

```
Spam Message
```

---

## 📊 Dataset

SMS Spam Collection Dataset

Contains over **5,500** SMS messages labeled as:

- Spam
- Ham

---

## 📦 Libraries Used

- Flask
- pandas
- numpy
- scikit-learn
- nltk
- joblib

---

## 👨‍💻 Author

**Parkkavi**

GitHub: https://github.com/Parkkavie

---

## ⭐ Future Improvements

- Bootstrap UI
- Spam probability score
- Multiple ML model comparison
- REST API support
- Docker deployment
- Cloud deployment (Render/Railway)

---

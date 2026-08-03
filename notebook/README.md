# 📧 Email Spam Detection using Machine Learning

## 📌 Project Overview

This project is a Machine Learning and Natural Language Processing (NLP) based application that classifies Email/SMS messages as Spam or Ham (Not Spam).

The model is trained using the SMS Spam Collection Dataset and deployed using Streamlit.

---

## 🚀 Features

- Predicts whether a message is Spam or Ham
- Text preprocessing using NLP
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier
- Interactive Streamlit Web Application
- Displays Prediction Confidence

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib

---

## 📂 Project Structure

```
Email-Spam-Detection
│
├── dataset
│   └── spam.csv
│
└── notebook
    ├── SpamDetection.ipynb
    ├── app.py
    ├── spam_model.pkl
    ├── tfidf_vectorizer.pkl
    ├── requirements.txt
    └── README.md
```

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Text Preprocessing
4. TF-IDF Vectorization
5. Train-Test Split
6. Train Multinomial Naive Bayes Model
7. Evaluate Model
8. Save Model
9. Deploy using Streamlit

---

## 📊 Model Performance

- Accuracy: **96.03%**

---

## ▶️ Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 📌 Future Improvements

- Deep Learning Model (LSTM/BERT)
- Email Subject Detection
- Multiple Language Support
- Better UI Design

---

## 👩‍💻 Author

**Satyabhama Kumari**

B.Tech, Computer Science & Engineering

NIT Durgapur
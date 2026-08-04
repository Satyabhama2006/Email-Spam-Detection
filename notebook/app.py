import streamlit as st
import joblib
import string
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Load stopwords
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Page settings
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 Email Spam Detection using Machine Learning")
st.markdown("---")

st.write(
    """
This application predicts whether an Email or SMS is **Spam** or **Ham**
using **Natural Language Processing (NLP)** and **Machine Learning**.
"""
)

# Input
message = st.text_area(
    "✉️ Enter your Email or SMS Message",
    height=200,
    placeholder="Type your message here..."
)

# Button
if st.button("🔍 Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:

        clean = clean_text(message)

        vector = tfidf.transform([clean])

        prediction = model.predict(vector)

        probability = model.predict_proba(vector)

        if prediction[0] == 1:
            st.error("🚨 This is a SPAM Message")
        else:
            st.success("✅ Ham Message")

        st.subheader("Prediction Confidence")

        st.progress(float(max(probability[0])))

        st.write(
            f"{max(probability[0])*100:.2f}%"
        )
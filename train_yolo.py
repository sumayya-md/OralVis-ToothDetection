import streamlit as st
import pickle

# Load model (vectorizer + classifier)
@st.cache_resource
def load_model():
    with open("models/fake_news_model.pkl", "rb") as f:
        vectorizer, clf = pickle.load(f)  # unpack tuple
    return vectorizer, clf

vectorizer, clf = load_model()

# Streamlit app
st.title("📰 Fake News Detector")

user_input = st.text_area("Enter a news article below and the model will predict whether it's FAKE or REAL.")

if st.button("🔍 Predict"):
    if user_input.strip():
        # Transform input and predict
        input_vec = vectorizer.transform([user_input])
        prediction = clf.predict(input_vec)[0]

        if prediction == "real":
            st.success("✅ This news is predicted as REAL.")
        else:
            st.error("❌ This news is predicted as FAKE.")
    else:
        st.warning("⚠️ Please enter some text before predicting.")

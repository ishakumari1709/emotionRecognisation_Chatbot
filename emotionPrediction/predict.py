# predict.py
import joblib

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def predict_emotion(text):
    """
    Predicts emotion from input text.
    """
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    return prediction

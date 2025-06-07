
# Emotion-Aware Chatbot 🤖💬

This is a simple and interactive Emotion Detection Chatbot built using **Streamlit** and **Scikit-learn**. It predicts the emotion behind your text and responds with motivational content such as quotes, journaling prompts, and music links.

---

## 📂 Dataset Used

The model was trained on a dataset of text samples labeled with emotions:  
**happy**, **sad**, **angry**, and **fear**.  
Dataset Link: https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp

---

## ⚙️ Approach Summary

This chatbot follows a simple ML pipeline to detect emotions and respond meaningfully:

### 🔠 Text Vectorization
- Uses **TF-IDF** (`tfidf_vectorizer.pkl`) to convert user input into numerical vectors.
- Captures important emotional words while ignoring common ones.

### 🧠 Emotion Classification
- A **Logistic Regression** model (`emotion_model.pkl`) trained using scikit-learn.
- Predicts one of four emotions: `happy`, `sad`, `angry`, or `fear`.

### 🎁 Response Generation
Based on the predicted emotion, the app offers:
- 📜 A motivational quote
- 🎧 A related YouTube music link
- 📝 A journaling prompt

Together, these steps help create an interactive, supportive, and emotion-aware chatbot experience.




---

## 📦 Dependencies

Install the required libraries using:

```bash
pip install -r requirements.txt
```

**Libraries Used:**
- streamlit  
- scikit-learn  
- numpy  
- pandas  
- matplotlib  

---

## 🚀 To Run the App

Use the following commands in your terminal:

```bash
# Optional: Create and activate virtual environment
python -m venv emotion_env
source emotion_env/bin/activate  # For Windows: emotion_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

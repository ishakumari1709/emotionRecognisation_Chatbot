import streamlit as st
from predict import predict_emotion
from quote_bank import get_quote, get_music, get_prompt

# --- Page setup ---
st.set_page_config(page_title="Emotion-Aware Chatbot", layout="centered")

# --- Force custom pastel background and white text ---
st.markdown("""
    <style>
    body, .main, .block-container {
        background-color: #9B7EBD !important;
        color: #ffffff !important;
    }
    .stTextArea textarea {
        background-color: #ffffff10;
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #ffffff30;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #7F55B1;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        border: none;
    }
    .stButton>button:hover {
        background-color: #5c3d85;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Explanation ---
with st.sidebar:
    st.header("ℹ️ About this App")
    st.markdown("""
    This chatbot uses **Machine Learning** to detect emotions from your text.

    ### How it works:
    - 🧠 Text is converted into numbers using **TF-IDF**
    - 🧪 A model predicts: happy, sad, angry, or fear
    - 🎁 You receive:
      - 🌟 A quote  
      - 🎧 A music link  
      - 📝 A journaling prompt

    ---
    **Tech Used**: scikit-learn, Streamlit  
    **Model**: Loaded from emotion_model.pkl
    """)

# --- Title and Instructions ---
st.title("💬 Emotion-Aware Chatbot")
st.write("Tell me how you're feeling, and I’ll support you with something meaningful.")

# --- Input Field ---
user_input = st.text_area(
    "🧠 What's on your mind?",
    height=120,
    placeholder="Type your thoughts here..."
)

# --- Emotion Detection & Recommendations ---
if user_input:
    emotion = predict_emotion(user_input)

    st.markdown(f"""
    <div style="
        background-color:#ffffff10; 
        padding:15px; 
        border-radius:10px; 
        margin-top:20px;
        text-align:center;
        font-size:18px;
        color:#ffffff;">
        🧠 <b>Detected Emotion:</b> {emotion.capitalize()}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### What would you like to do next?")
    col1, col2, col3 = st.columns(3)
    choice = None

    with col1:
        if st.button("🌟 Get a Quote"):
            choice = "quote"
    with col2:
        if st.button("📝 Journaling Prompt"):
            choice = "prompt"
    with col3:
        if st.button("🎧 Listen to Music"):
            choice = "music"

    if choice == "quote":
        quote = get_quote(emotion)
        st.markdown(f"""
        <blockquote style="
            background-color:#ffffff10;
            padding:15px;
            border-left: 5px solid #ffffff70;
            font-style:italic;
            font-size:17px;
            color:#ffffff;">
            💬 {quote}
        </blockquote>
        """, unsafe_allow_html=True)

    elif choice == "prompt":
        prompt = get_prompt(emotion)
        st.markdown(f"""
        <div style="
            background-color:#ffffff10;
            padding:15px;
            border-radius:8px;
            font-size:16px;
            color:#ffffff;">
            🧘 <b>Journaling Prompt:</b><br><br><em>{prompt}</em>
        </div>
        """, unsafe_allow_html=True)

    elif choice == "music":
        link = get_music(emotion)
        if "youtube.com/watch?v=" in link:
            embed_url = link.replace("watch?v=", "embed/")
            st.markdown(f"""
            <iframe width="100%" height="315" 
            src="{embed_url}" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
            </iframe>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"🎵 [Listen here]({link})", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style="font-size:14px; color:#dddddd; text-align:center;">
    Made with ❤️ by Isha Bhagat using Machine Learning and Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
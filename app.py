
import streamlit as st
from gtts import gTTS
import random
from textblob import TextBlob

st.set_page_config(page_title="AI Voice Assistant", layout="centered")

# -------------------------------
# SESSION STATE
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "user_text" not in st.session_state:
    st.session_state.user_text = ""

def go_to(page):
    st.session_state.page = page

# -------------------------------
# AI RESPONSE FUNCTION
# -------------------------------
def generate_response(text):
    text = text.lower()
    
    if "hello" in text:
        return "Hello! How can I assist you today?"
    elif "project" in text:
        return "This project demonstrates speech processing and sentiment analysis."
    elif "sad" in text or "bad" in text:
        return "I'm sorry to hear that. Hope things improve!"
    elif "happy" in text or "love" in text:
        return "That's great to hear! Keep it up!"
    else:
        return "Interesting input! Tell me more."

# -------------------------------
# WELCOME SCREEN
# -------------------------------
if st.session_state.page == "welcome":
    st.title("🤖 AI Voice Assistant")
    st.subheader("Convert Speech ↔ Text")
    st.button("Start", on_click=go_to, args=("input",))

# -------------------------------
# INPUT SCREEN
# -------------------------------
elif st.session_state.page == "input":
    st.title("📥 Input Screen")

    text = st.text_input("Enter text:", value=st.session_state.user_text)

    # Always store text
    st.session_state.user_text = text

    # Text to Speech
    if st.button("🔊 Convert to Speech"):
        if text:
            tts = gTTS(text)
            tts.save("output.mp3")
            st.audio("output.mp3")

    st.button("Next", on_click=go_to, args=("process",))

# -------------------------------
# PROCESS SCREEN
# -------------------------------
elif st.session_state.page == "process":
    st.title("⚙ Processing...")
    st.info("Simulating AI processing...")

    if st.button("Generate Output"):
        st.session_state.page = "output"
        st.rerun()

# -------------------------------
# OUTPUT SCREEN
# -------------------------------
elif st.session_state.page == "output":
    st.title("📊 Output Screen")

    confidence = random.randint(85, 99)

    st.success("Text processed successfully!")
    st.write(f"Confidence Score: {confidence}%")

    user_text = st.session_state.user_text

    if user_text:
        # -------------------------------
        # SENTIMENT ANALYSIS
        # -------------------------------
        blob = TextBlob(user_text)
        sentiment = blob.sentiment.polarity

        st.subheader("🧠 Sentiment Analysis")

        if sentiment > 0:
            st.success(f"😊 Positive Sentiment ({sentiment:.2f})")
        elif sentiment < 0:
            st.error(f"😠 Negative Sentiment ({sentiment:.2f})")
        else:
            st.info(f"😐 Neutral Sentiment ({sentiment:.2f})")

        # -------------------------------
        # AI RESPONSE + VOICE
        # -------------------------------
        response = generate_response(user_text)

        st.subheader("🤖 AI Response")
        st.write(response)

        tts = gTTS(response)
        tts.save("response.mp3")
        st.audio("response.mp3")

    else:
        st.warning("⚠ Please enter text first.")

    st.button("Restart", on_click=go_to, args=("welcome",))

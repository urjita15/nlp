
import streamlit as st
from gtts import gTTS
import random

st.set_page_config(page_title="AI Voice Assistant", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "welcome"

def go_to(page):
    st.session_state.page = page

# WELCOME
if st.session_state.page == "welcome":
    st.title("🤖 AI Voice Assistant")
    st.subheader("Convert Speech ↔ Text")
    st.button("Start", on_click=go_to, args=("input",))

# INPUT
elif st.session_state.page == "input":
    st.title("📥 Input Screen")
    text = st.text_input("Enter text:")

    if st.button("🔊 Convert to Speech"):
        if text:
            tts = gTTS(text)
            tts.save("output.mp3")
            st.audio("output.mp3")

    st.button("Next", on_click=go_to, args=("process",))

# PROCESS
elif st.session_state.page == "process":
    st.title("⚙ Processing...")
    st.info("Simulating AI processing...")
    if st.button("Generate Output"):
        go_to("output")

# OUTPUT
elif st.session_state.page == "output":
    st.title("📊 Output Screen")
    confidence = random.randint(85, 99)

    st.success("Text processed successfully!")
    st.write(f"Confidence Score: {confidence}%")

    st.button("Restart", on_click=go_to, args=("welcome",))

import streamlit as st
import whisper
import os
from tempfile import NamedTemporaryFile

# Load Whisper model once
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

st.title("🗣️ STT Whisper - Speech to Text")
st.write("Upload a `.wav` or `.mp3` file to transcribe it using OpenAI's Whisper model.")

# File uploader
uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file is not None:
    with NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.audio(uploaded_file, format=f"audio/{uploaded_file.type.split('/')[-1]}")

    with st.spinner("Transcribing..."):
        result = model.transcribe(temp_path)
        transcript = result["text"]

    st.success("✅ Transcription Complete!")
    st.text_area("📝 Transcript", transcript, height=300)

    st.download_button("📥 Download Transcript", transcript, file_name="transcript.txt")

    os.remove(temp_path)


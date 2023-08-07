import streamlit as st 
import whisper

st.title("Whisper App")

audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","m4a","mp4"])

@st.cache_data
def load_whisper_model():
    model = whisper.load_model("base")
    return model

    
if st.sidebar.button("Load Whisper Model"):
    model = load_whisper_model()
    st.sidebar.success("Whisper Model Loaded")
    

if st.sidebar.button("Transcribe Audio"):
        if audio_file is not None:
            model = load_whisper_model()
            st.sidebar.success("Transcribing Audio")
            transcription = model.transcribe(audio_file)
            st.sidebar.success("transcription complete")
            st.text(transcription["text"])
        else:
            st.sidebar.error("Please upload an audio file")


import whisper
import streamlit as st
from PIL import Image

img = Image.open('devnologia-logo-fa.png')
st.set_page_config(page_title="Assistente Virtual", layout='centered', page_icon=img)

st.title(" Assistente Virtual - @devnologia")

audio_file = st.file_uploader("Carregar Audio", type=["wav", "mp3", "m4a"])
audio_path = "audios/"

model = whisper.load_model("base")
st.text("Modelo Preparado")

if st.sidebar.button("Transcrecer Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcrevendo Audio aguarde...")
        audio_path += audio_file.name
        transcription = model.transcribe(audio_path, fp16=False)
        st.sidebar.success("Transcrição realizada com sucesso")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Favor realizar o upload do audio")

st.sidebar.header("Reproduzir audio original")
st.sidebar.audio(audio_file)


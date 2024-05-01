import streamlit as st
from PIL import Image
import whisper

class StreamlitInterface:
    def __init__(self):
        # Inicializar a interface
        img = Image.open('devnologia-logo-fa.png')
        st.set_page_config(page_title="Assistente Virtual", layout='centered', page_icon=img)
        st.title("🤖 Assistente Virtual - @devnologia")
        
        # Carregar áudio
        self.audio_file = st.file_uploader("Carregar Áudio", type=["wav", "mp3", "m4a"])
        self.audio_path = "audios/"
        
        # Inicializar o modelo de transcrição
        
        
        # Inicializar o modelo Whisper
        self.whisper_model = whisper.load_model("base")
        
        # Espaço para exibir a transcrição em tempo real
        
        
        # Botões na barra lateral
        self.init_sidebar()
        
    def init_sidebar(self):
        # Seção para transcrição de áudio do microfone

        # Botão para iniciar gravação
        
        # Botão para parar gravação
       
        # Linha de separação visual

        # Seção para transcrição de áudio gravado
        st.sidebar.header("Transcrição de Áudio")    
        
        # Botão para transcrever áudio carregado com Whisper
        if st.sidebar.button("Transcrever Áudio com Whisper"):
            self.transcrever_audio_com_whisper()
        
        # Exibir o áudio carregado
        st.sidebar.header("Reproduzir arquivo de áudio original")
        st.sidebar.audio(self.audio_file)
        
    def transcrever_audio_com_whisper(self):
        # Verificar se há um arquivo carregado
        if self.audio_file is not None:
            # Obter o caminho completo para o arquivo carregado
            audio_path = self.audio_path + self.audio_file.name
            
            # Transcrever o áudio com Whisper
            st.sidebar.info("Transcrevendo áudio, aguarde...")
            transcription = self.whisper_model.transcribe(audio_path)
            
            # Exibir a transcrição na interface
            st.sidebar.success("Transcrição realizada com sucesso")
            st.markdown(transcription["text"])
        else:
            st.sidebar.error("Por favor, faça o upload do áudio")

if __name__ == "__main__":
    interface = StreamlitInterface()

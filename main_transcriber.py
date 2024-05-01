import streamlit as st
from PIL import Image
from src.audio_transcriber import AudioTranscriber
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
        vosk_model_path = "src/vosk-model-small-pt-0.3"  # Insira o caminho para o modelo Vosk
        self.transcriber = AudioTranscriber(vosk_model_path)
        
        # Inicializar o modelo Whisper
        self.whisper_model = whisper.load_model("base")
        
        # Espaço para exibir a transcrição em tempo real
        self.transcricao_text = st.empty()
        
        # Botões na barra lateral
        self.init_sidebar()
        
    def init_sidebar(self):
        # Seção para transcrição de áudio do microfone
        st.sidebar.header("Meu Assistente")

        # Botão para iniciar gravação
        if st.sidebar.button("Iniciar gravação"):
            self.transcriber.start_recording()
            self.transcriber.transcribe_audio(self.transcricao_text)
            
        # Botão para parar gravação
        if st.sidebar.button("Parar gravação"):
            self.transcriber.stop_recording()

        # Linha de separação visual
        st.sidebar.markdown("---")

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

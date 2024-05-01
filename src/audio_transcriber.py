import pyaudio
from vosk import Model, KaldiRecognizer
import json

from src.comandos import executar_comando

class AudioTranscriber:
    def __init__(self, model_path, rate=16000, chunk=4096, format=pyaudio.paInt16, channels=1):
        self.model_path = model_path
        self.rate = rate
        self.chunk = chunk
        self.format = format
        self.channels = channels
        
        # Inicializar PyAudio
        self.p = pyaudio.PyAudio()
        
        # Inicializar o modelo Vosk
        self.model = Model(model_path)
        
        # Inicializar KaldiRecognizer
        self.recognizer = KaldiRecognizer(self.model, self.rate)
        
        # Variável para controlar a gravação
        self.recorder_active = False
        
        # Stream de áudio
        self.stream = None

    def start_recording(self):
        # Iniciar a captura de áudio com PyAudio
        self.stream = self.p.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk)
        self.recorder_active = True
        print("Iniciando gravação...")

    def stop_recording(self):
        self.recorder_active = False
        # Fechar o stream de áudio
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        print("Parando gravação...")

    def transcribe_audio(self, transcricao_text):
        print("Transcrição em andamento...")
        
        while self.recorder_active:
            # Ler dados de áudio do microfone
            audio_data = self.stream.read(self.chunk)
            
            # Verificar se o reconhecimento pode ser executado com os dados de áudio lidos
            if self.recognizer.AcceptWaveform(audio_data):
                # Obter o resultado de transcrição
                result = self.recognizer.Result()
                data = json.loads(result)
                
                # Obter o texto transcrito
                texto_transcrito = data.get("text", "")
                
                # Exibir a transcrição em tempo real na interface do Streamlit
                transcricao_text.text(f"Transcrição: {texto_transcrito}")
                
                # Exibir o texto transcrito no console
                print(f"Texto transcrito: {texto_transcrito}")
                
                # Executar o comando ou fazer outra ação com o texto transcrito
                executar_comando(texto_transcrito)
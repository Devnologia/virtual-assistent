# Criando Seu Assistente de Voz com Python: Abra Programas e Transcreva Áudio com Comandos de Voz!
Este repositório acompanha o vídeo do canal Devnologia no YouTube, onde ensinamos a criar um assistente de voz para tarefas básicas utilizando Python. Com este assistente, você poderá controlar o computador por voz, executando tarefas como abrir o navegador, seu bloco de notas e muito mais. Além disso, você aprenderá a transcrever texto falado em áudio.

### Bibliotecas utilizadas:
- PyAudio
- vosk
- Streamlit
- Whisper

### Configuração do Ambiente
Para acompanhar este tutorial, siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Instale o Python (caso ainda não tenha): https://www.python.org/downloads/
2. Abra um terminal ou prompt de comando.
3. Instale as bibliotecas necessárias utilizando o comando pip:
`````
pip install pyaudio vosk streamlit
`````
4. Instale as biblioteca do Whisper usando o git+:
`````
pip install git+https://github.com/openai/whisper.git 
`````
5. Você precisa instalar o **ffmpeg** como um módulo python e também seguir o seguintes para donwload e configuração do seu computador.
`````
 pip install ffmpeg
 `````
- siga as intrunções: https://ffmpeg.org/download.html.
- caso seu sitema opreacional seja WINDOWS: [https://www.geeksforgeeks.org/how-to-install-ffmpeg -no Windows/](https://www-geeksforgeeks-org.translate.goog/how-to-install-ffmpeg-on-windows/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp)

### Como baixar um modelo Vosk

Este guia irá ajudá-lo a baixar um modelo para o Vosk, uma biblioteca de reconhecimento de voz offline de código aberto.

1. **Visite o repositório de modelos Vosk**  
   Você pode baixar diretamente o modelo que utilizamos neste projeto através do [link modelo utilizado no projeto](https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip). Neste caso você pode pular para a etapa **4. Descompacte o arquivo**
   Em caso de dúvida ou maiores informações. Acesse o [repositório de modelos Vosk](https://alphacephei.com/vosk/models) para ver a lista de modelos disponíveis.

2. **Escolha um modelo**  
   Na página do repositório, escolha o modelo que deseja baixar. Existem modelos disponíveis para diferentes idiomas e propósitos. Certifique-se de escolher um modelo adequado para suas necessidades.

3. **Baixe o modelo**  
   Clique no link para o modelo escolhido para iniciar o download. O arquivo será baixado no formato de arquivo compactado (`.zip` ou `.tar.gz`).

4. **Descompacte o arquivo**  
   Após baixar o arquivo, descompacte-o para uma pasta local em seu sistema. Você pode usar ferramentas de descompactação como `unzip` para arquivos `.zip` ou `tar` para arquivos `.tar.gz`.

5. **Use o modelo**  
   Agora que você baixou e descompactou o modelo, você pode usá-lo com a biblioteca Vosk em seus projetos de reconhecimento de voz. Ao utilizar o modelo, certifique-se de fornecer o caminho para a pasta do modelo em seus scripts para que o Vosk possa carregá-lo corretamente.

#### Considerações finais

Certifique-se de verificar a documentação oficial do Vosk para obter mais informações sobre como usar a biblioteca e os modelos de maneira eficiente.



### Sobre o Vídeo
No vídeo, você aprenderá a:

- Reconhecer comandos de voz e executar ações correspondentes.
- Implementar a transcrição de texto falado e áudio do computador.
- Criar uma interface gráfica amigável utilizando o Streamlit.

### Público Alvo
Este tutorial é ideal para:

- Desenvolvedores Python iniciantes ou intermediários.
- Usuários que buscam automatizar tarefas e aumentar a produtividade.
- Pessoas interessadas em inteligência artificial e processamento de linguagem natural.

### Termos
Os termos **CHUNK, FORMAT, CHANNELS e RATE** são configurações que definem a forma como o áudio é capturado do microfone e processado em um projeto que utiliza o PyAudio, uma biblioteca para trabalhar com áudio em Python.

**CHUNK:** É o tamanho do buffer de áudio, ou seja, quantos frames de áudio são lidos de uma vez do microfone. No seu caso, CHUNK = 8192 significa que cada vez que você lê do microfone, você está lendo 8192 frames de áudio. Um buffer maior pode permitir processamento mais eficiente, mas também pode introduzir mais latência.
**FORMAT:** Define o formato de áudio a ser usado. No seu caso, FORMAT = pyaudio.paInt16 significa que você está capturando o áudio como inteiros de 16 bits. Este é um formato comum para áudio, mas existem outros formatos disponíveis, como paFloat32 para capturar o áudio como valores de ponto flutuante.
**CHANNELS:** Define o número de canais de áudio. CHANNELS = 1 indica que você está capturando áudio mono (um único canal). Para capturar áudio estéreo, você usaria CHANNELS = 2.
**RATE:** Define a taxa de amostragem ou frequência de amostragem do áudio em Hertz (Hz). RATE = 16000 significa que o áudio está sendo capturado a 16.000 amostras por segundo. Este é um valor comum para reconhecimento de fala, mas você pode usar taxas de amostragem mais altas para outras aplicações de áudio.

### Assista ao Vídeo!
Clique aqui:[ link do vídeo do YouTube](https://youtu.be/8Jk2JI_FOjw): para assistir ao vídeo completo e começar a criar o seu assistente de voz com Python!

### Recursos Adicionais
Código fonte do projeto: [Link do repositório do Github](https://github.com/Devnologia/virtual-assistent)

Documentação do PyAudio: [Link para documentação da biblioteca PyAudio](https://pypi.org/project/PyAudio/)

Documentação do Streamlit: [Link para documentação da biblioteca Streamlit](https://streamlit.io/)

### Feedback
Se inscreva no canal Devnologia e deixe seu like para nos apoiar! Agradecemos a audiência.



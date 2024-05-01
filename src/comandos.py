import os

def executar_comando(commando):
    # Comando responsável por abrir o google
    if "abrir navegador" in commando:
        os.system("start Chrome.exe")
    
    # Comando responsável por abrir o excel
    if "abrir bloco" in commando:
        os.system("start notepad.exe")
    
    # Comando responsável por abrir ferramenta de captura
    if "ferramenta de captura" in commando:
        os.system("start SnippingTool.exe")
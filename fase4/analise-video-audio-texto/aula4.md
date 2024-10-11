# FASE 4 - ANALISE VIDEO AUDIO TEXTO - TRANSCRIÇÃO AUTOMÁTICA DE ÁUDIO E CONVERSÃO DE FALA EM TEXTO

Nesta aula, você aprenderá sobre o conceito de transcrição de áudio para texto, explorando como converter informações auditivas para o formato escrito. Você também conhecerá as bibliotecas MoviePy e SpeechRecognition, entendendo como elas podem ser utilizadas para manipular e processar mídia.

Além disso, você implementará um projeto prático que aplica esses conceitos, transformando um vídeo em áudio e, em seguida, convertendo o áudio em texto. Este projeto fornecerá uma compreensão prática e abrangente das técnicas envolvidas na transcrição de áudio, desde a extração do áudio de um vídeo até a conversão do áudio em texto legível.  
            
Nesta aula entenderemos o conceito de transcrição de vídeo em áudio e áudio em texto e realizaremos dois projetos: um para transformar vídeo em texto e outro para transformar áudio em texto. Os dois são bem parecidos, pois, para converter vídeo em texto precisamos extrair o áudio do vídeo como primeiro passo. A seguir temos as bibliotecas necessárias para rodar os projetos:

```sh
pip install moviepy SpeechRecognition pydub
```

Código do script chamado “transcribe_video.py”


transcribe_video.py
```python
import moviepy.editor as mp
import speech_recognition as sr
import os

def extract_audio_from_video(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio_to_text(audio_path, text_output_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # lê todo o áudio do arquivo
        
        try:
            # Usa o serviço de reconhecimento de fala do Google
            text = recognizer.recognize_google(audio, language="pt-BR")  # Use "en-US" para inglês
            print("Transcrição: " + text)
            
            # Salva a transcrição em um arquivo de texto
            with open(text_output_path, 'w', encoding='utf-8') as file:
                file.write(text)
                
        except sr.UnknownValueError:
            print("Google Speech Recognition não conseguiu entender o áudio")
        except sr.RequestError as e:
            print("Erro ao solicitar resultados do serviço de reconhecimento de fala do Google; {0}".format(e))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(script_dir, 'video1.mp4')  # Video de entrada
    audio_path = os.path.join(script_dir, 'audio1.wav')
    text_output_path = os.path.join(script_dir, 'transcricao1.txt')

    extract_audio_from_video(video_path, audio_path)
    transcribe_audio_to_text(audio_path, text_output_path)

if __name__ == "__main__":
    main()
```

Logo depois criaremos um projeto que faz a transcrição direta de um áudio. A seguir temos o código do script chamado “transcribe_audio.py":

transcribe_audio.py
```python
import speech_recognition as sr
import os

def transcribe_audio_to_text(audio_path, text_output_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # lê todo o áudio do arquivo
        
        try:
            # Usa o serviço de reconhecimento de fala do Google com configuração para português do Brasil
            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Transcrição: " + text)
            
            # Salva a transcrição em um arquivo de texto
            with open(text_output_path, 'w', encoding='utf-8') as file:
                file.write(text)
                
        except sr.UnknownValueError:
            print("Google Speech Recognition não conseguiu entender o áudio")
        except sr.RequestError as e:
            print("Erro ao solicitar resultados do serviço de reconhecimento de fala do Google; {0}".format(e))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(script_dir, 'audio1.wav')  # Entrada do audio em .wav
    text_output_path = os.path.join(script_dir, 'transcricao_audio.txt')

    transcribe_audio_to_text(audio_path, text_output_path)

if __name__ == "__main__":
    main()
```

Lembre-se de substituir o nome do arquivo de vídeo e de saída caso seja necessário.
          
Não deixe de praticar!
          
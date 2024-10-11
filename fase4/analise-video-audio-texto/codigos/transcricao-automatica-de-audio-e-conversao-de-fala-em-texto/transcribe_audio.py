import speech_recognition as sr # pip install SpeechRecognition - https://pypi.org/project/SpeechRecognition/
import os

# pip install pydub

def transcribe_audio_to_text(audio_path, text_output_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print('Transcrição: ', text)

            with open(text_output_path, 'w', encoding='utf-8') as file:
                file.write(text)
        except sr.UnknownValueError:
            print('Google Speech Recognition não conseguiu entender o áudio')
        except sr.RequestError as e:
            print('Erro ao solicitar resultados do serviço de reconhecimento de fala do Google; {0}'.format(e))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(script_dir, 'audio.wav') # Áudio de saída
    text_output_path = os.path.join(script_dir, 'transcricao2.txt')

    transcribe_audio_to_text(audio_path, text_output_path)

if __name__ == '__main__':
    main()
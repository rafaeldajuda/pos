# lib - deepface - https://pypi.org/project/deepface/ - pip install deepface
# lib - tf_keras - pip install tf-keras
# lib - opencv-python-headless - opencv sem a parte de interface gráfica - pip install opencv-python-headless

import cv2
from deepface import DeepFace
import os
import numpy as np
from tqdm import tqdm

def detect_emotions(video_path, outpath_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print('Erro ao abrir o video')
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(outpath_path, fourcc, fps, (width, height))

    for _ in tqdm(range(total_frames), desc='Processando vídeo'):
        ret, frame = cap.read()
        
        if not ret:
            break

        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        for face in result:
            # Obter a caixa delimitadora da face
            x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']

            # Obter a emoção dominante
            dominant_emotion = face['dominant_emotion']

            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

            # Escrever a emoção dominante acima da face
            cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')
output_video_path = os.path.join(script_dir, 'output_video.mp4')

detect_emotions(input_video_path, output_video_path)

import cv2
import face_recognition
import os
import numpy as np
from tqdm import tqdm
from deepface import DeepFace

def load_images_from_folder(folder):
    known_face_encodings = []
    known_faces_names = []

    for filename in os.listdir(folder):
        if (filename.endswith('.jpg') or filename.endswith('.png')):
            image_path = os.path.join(folder, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                face_encoding = face_encodings[0]
                name = os.path.splitext(filename)[0][:-1]
                known_face_encodings.append(face_encoding)
                known_faces_names.append(name)
    
    return known_face_encodings, known_faces_names

def detect_faces_and_emotions(video_path, outpath_path, known_face_encodings, known_faces_names):
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

        # Obter as localizações e codificações das faces conhecidas no frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = 'Desconhecido'
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            face_names.append(name)

        # Iterar sobre cada face detectada pelo DeepFace
        for face in result:
            # Obter a caixa delimitadora da face
            x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']

            # Obter a emoção dominante
            dominant_emotion = face['dominant_emotion']

            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

            # Escrever a emoção dominante acima da face
            cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        
            # Associar a face detectada pelo DeepFace com as faces conhecidas
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                if x <= left <= x + w and y <= top <= y + h:
                    # Escrever o nome abaixo da face
                    cv2.putText(frame, name, (x + 6, y + h - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
                    break

        # Escrever o frame processando no vídeo de saída
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

image_folder = 'images'

known_face_encodings, known_faces_names = load_images_from_folder(image_folder)

script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')
output_video_path = os.path.join(script_dir, 'output_video_recognize.mp4')

detect_faces_and_emotions(input_video_path, output_video_path, known_face_encodings, known_faces_names)

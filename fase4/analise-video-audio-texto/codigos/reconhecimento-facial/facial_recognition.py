import cv2
import os
import numpy as np

# https://pypi.org/project/face-recognition/
# instalar sem cache - pip install --no-cache-dir face_recognition
# precisa instalar a biblioteca dlib (no windows pode dar problema)
# para o dlib funcionar instalar C++ CMake tools for Windows e Windows 11 SDK
# Ao instalar o Visual Studio Installer é possível baixar as libs junto
# setuptools - auxiliar - pip install setuptools
import face_recognition 

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

def main():
    image_folder = 'images'
    known_face_encodings, known_faces_names = load_images_from_folder(image_folder)

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = 'Desconhecido'
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            face_names.append(name)
        
        for (top, right, bottom, left), names in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # desenhar um retangulo em volta da face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # desenhar uma etiqueta com o nome abaixo da face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

            

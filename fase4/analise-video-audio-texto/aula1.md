# FASE 4 - ANALISE VDEIO AUDIO TEXTO - RECONHECIMENTO FACIAL

Nesta aula, você aprenderá sobre o conceito de reconhecimento facial na área de visão computacional. Exploraremos os arquivos Haarcascades e sua importância para o reconhecimento facial. Em seguida, implementaremos um projeto prático de reconhecimento facial usando a webcam. Para isso, utilizaremos a linguagem de programação Python e a biblioteca face_recognition.

Nesta aula entenderemos o conceito do reconhecimento facial e onde ele está inserido em nosso dia a dia. Após isso, criaremos dois projetos: um que realiza a detecção facial via webcam e outro que faz o reconhecimento facial  de acordo com fotos de pessoas para que o algoritmo entenda quem ele deve identificar. 

face_detection.py
```python
import cv2

def capture_video():
    # Iniciar a captura de vídeo da webcam
    cap = cv2.VideoCapture(0)

    # Verificar se a captura foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao acessar a webcam.")
        return

    # Carregar o classificador Haar Cascade para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    try:
        while True:
            # Capturar frame por frame
            ret, frame = cap.read()

            if not ret:
                break

            # Converter o frame para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detectar rostos no frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Desenhar retângulos ao redor dos rostos detectados
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Exibir o frame com detecções
            cv2.imshow('Face Detection', frame)

            # Parar o loop ao pressionar a tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        pass

    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    cv2.destroyAllWindows()

# Chamar a função para capturar e exibir vídeo da webcam
if __name__ == "__main__":
    capture_video()
```

Com isso, abrimos nossa webcam, em que um quadrado será desenhado em nosso rosto.

Logo após,  criaremos um algoritmo que reconhece rostos e mostra o nome da pessoa de acordo com uma base de dados de imagens. Para isso, na mesma pasta do script face_detection.py, criamos uma pasta chamada “images” e nela nós colocaremos as fotos com os nomes e o número das fotos. Exemplo: carlos1.jpg, carlos2.jpg, carlos3.jpg, individuo1.jpg, individuo2.jpg, individuo3.jpg.

Feito isso, escreveremos o seguinte código.

face_recognition.py
```python
import cv2
import face_recognition
import os
import numpy as np

def load_images_from_folder(folder):
    known_face_encodings = []
    known_face_names = []

    # Percorrer todos os arquivos na pasta fornecida
    for filename in os.listdir(folder):
        # Verificar se o arquivo é uma imagem
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Carregar a imagem
            image_path = os.path.join(folder, filename)
            image = face_recognition.load_image_file(image_path)
            # Obter as codificações faciais (assumindo uma face por imagem)
            face_encodings = face_recognition.face_encodings(image)
            
            if face_encodings:
                face_encoding = face_encodings[0]
                # Extrair o nome do arquivo, removendo o sufixo numérico e a extensão
                name = os.path.splitext(filename)[0][:-1]
                # Adicionar a codificação e o nome às listas
                known_face_encodings.append(face_encoding)
                known_face_names.append(name)

    return known_face_encodings, known_face_names

def main():
    image_folder = 'images'  # Caminho para a pasta de imagens
    known_face_encodings, known_face_names = load_images_from_folder(image_folder)  # Carregar imagens e codificações

    video_capture = cv2.VideoCapture(0)  # Iniciar captura de vídeo da webcam

    while True:
        ret, frame = video_capture.read()  # Capturar um único frame de vídeo
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Redimensionar o frame para 1/4 do tamanho
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])  # Converter BGR para RGB

        face_locations = face_recognition.face_locations(rgb_small_frame)  # Localizar faces no frame
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # Obter codificações faciais

        face_names = []  # Lista para armazenar os nomes das faces detectadas
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  # Verificar se a face é conhecida
            name = "Desconhecido"  # Nome padrão se a face não for reconhecida
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)  # Calcular a distância para faces conhecidas
            best_match_index = np.argmin(face_distances)  # Encontrar o índice da melhor correspondência
            if matches[best_match_index]:  # Verificar se a melhor correspondência é uma face conhecida
                name = known_face_names[best_match_index]  # Obter o nome da face conhecida
            face_names.append(name)  # Adicionar o nome à lista de nomes

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Redimensionar as coordenadas das faces de volta ao tamanho original
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Desenhar uma etiqueta com o nome abaixo da face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Exibir a imagem resultante
        cv2.imshow('Video', frame)

        # Pressionar 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a captura de vídeo e fechar todas as janelas
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

Lembrando que nós nomeamos o arquivo como facial_recognition.py para não  conflitar  com a importação da biblioteca face_recognition.

# Reconhecimento Facial

!["img"](../img/fase4_analise_aula1_1.png)

## Definição

O reconhecimento facial é uma tecnologia de biometria que identifica ou verifica a identidade de uma pessoa a partir da análise de suas características faciais. Utiliza algoritmos de visão computacional pxara comparar uma imagem ou video do rosto de uma pessoa com uma base de dados de rostos conhecidos. É uma forma de idenficação e autenticação que ganhou popularidade em diversas aplicações devido à sua precisão e conveniência.

## Como funciona

* **Detecção do Rosto:** Identifcar a presença de um rosto em uma imagem ou vídeo. Isso geralmente é feito utilizando algoritmos de detecção de objetos, como os classificadores Haar Cascade ou redes neurais convolucionais (CNNs).

* **Alinhamento e Normalização:** O rosto detectado é alinhado e normalizado para ajustar a escala, a rotação e a posição, garantido que as características faciais estejam em uma posição consistente para a análise.

* **Extração de Características:** As características únicas do rosto são extraídas e convertidas em uma representação numérica (vetor de características). Técnicas modernas frequentemente utilizam redes neurais profundas para esta tarefa.

* **Comparação:** O vetor de características do rosto detectado é comparado com os vetores de características armazenados em uma base de dados para encontrar correspondências. Métodos de comparação podem incluir medidas de distância, como a distância euclidiana ou o cosseno da similaridade.

* **Identificação ou Verificação:** Dependendo da aplicação, o sistema pode identificar a pessoa (procurando a melhor correspodência na base de dados) ou verificar a identidade (comparando com uma identidade específica fornecida).

* **Precisão Variável:** A precisão do reconhecimento facial pode variar com a qualidade de imagem, a iluminação e as características físicas do indivíduo.

* **Bias e Discriminação:** Algoritmos podem apresentar vieses que afetam a precisão de certas demografias, levando a possíveis discriminações. É essencial treinar modelos com dados diversificados para minizar esses vieses.
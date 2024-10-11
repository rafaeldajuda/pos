# FASE 4 - ANALISE VIDEO AUDIO TEXTO - DETECÇÃO DE ATIVIDADES E RECONHECIMENTO DE AÇÕES EM VÍDEOS

Nesta aula, você aprenderá sobre o conceito de detecção de atividades em vídeos, explorando como identificar diferentes tipos de movimentos em sequências de vídeos, além de entender o conceito de reconhecimento de ações em vídeos.

Você conhecerá os Keypoints, (pontos-chave) usados para identificar posições específicas no corpo, e os Landmarks, que são referências anatômicas utilizadas para análise de movimento.

Além disso, implementaremos um projeto prático de detecção e análise de movimento utilizando a biblioteca MediaPipe, aplicando esses conceitos para criar soluções eficazes em visão computacional.  
            
Nesta aula entenderemos o conceito de detecção e reconhecimento de ações em vídeos e como podemos utilizá-lo. Nós criaremos dois projetos: um para detectar os keypoints e outro para mostrar os keypoints (que são os pontos relevantes no corpo do ser humano) e que a biblioteca mediapipe nos disponibiliza.

Para os dois projetos precisaremos instalar as seguintes bibliotecas:

Instalação de bibliotecas
```sh
pip install opencv-python mediapipe tqdm
```

Feito isso, nós começaremos desenvolvendo o primeiro script em uma pasta. Vamos criá-lo e, nesta mesma pasta, colocá-lo. Nomearemos este arquivo como “pose_detection_video.py” e ele terá o seguinte código:

pose_detection_video.py
```python
import cv2
import mediapipe as mp
import os
from tqdm import tqdm

def detect_pose(video_path, output_path):
    # Inicializar o MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    # Capturar vídeo do arquivo especificado
    cap = cv2.VideoCapture(video_path)

    # Verificar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Obter propriedades do vídeo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Definir o codec e criar o objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Loop para processar cada frame do vídeo com barra de progresso
    for _ in tqdm(range(total_frames), desc="Processando vídeo"):
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Se não conseguiu ler o frame (final do vídeo), sair do loop
        if not ret:
            break

        # Converter o frame para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Processar o frame para detectar a pose
        results = pose.process(rgb_frame)

        # Desenhar as anotações da pose no frame
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Escrever o frame processado no vídeo de saída
        out.write(frame)

        # Exibir o frame processado
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Caminho para o vídeo de entrada e saída
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')  # Nome do vídeo de entrada
output_video_path = os.path.join(script_dir, 'output_video_pose.mp4')  # Nome do vídeo de saída

# Processar o vídeo
detect_pose(input_video_path, output_video_path)
```

Após isso, podemos observar os keypoints que aparecem desenhados no vídeo. Assim, podemos analisar a movimentação desses pontos fazendo comparações e, como explicado anteriormente, utilizamos um exercício de levantar os braços como exemplo. Nisso criamos o seguinte script, nomeado “pose_detection_arm_up.py” e com o seguinte código:

pose_detection_arm_up.py     
```python
import cv2
import mediapipe as mp
import os
from tqdm import tqdm

def detect_pose_and_count_arm_movements(video_path, output_path):
    # Inicializar o MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    # Capturar vídeo do arquivo especificado
    cap = cv2.VideoCapture(video_path)

    # Verificar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Obter propriedades do vídeo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Definir o codec e criar o objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Variáveis para contar movimentos dos braços
    arm_up = False
    arm_movements_count = 0

    # Função para verificar se o braço está levantado
    def is_arm_up(landmarks):
        left_eye = landmarks[mp_pose.PoseLandmark.LEFT_EYE.value]
        right_eye = landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]

        left_arm_up = left_elbow.y < left_eye.y
        right_arm_up = right_elbow.y < right_eye.y

        return left_arm_up or right_arm_up

    # Loop para processar cada frame do vídeo com barra de progresso
    for _ in tqdm(range(total_frames), desc="Processando vídeo"):
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Se não conseguiu ler o frame (final do vídeo), sair do loop
        if not ret:
            break

        # Converter o frame para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Processar o frame para detectar a pose
        results = pose.process(rgb_frame)

        # Desenhar as anotações da pose no frame
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Verificar se o braço está levantado
            if is_arm_up(results.pose_landmarks.landmark):
                if not arm_up:
                    arm_up = True
                    arm_movements_count += 1
            else:
                arm_up = False

            # Exibir a contagem de movimentos dos braços no frame
            cv2.putText(frame, f'Movimentos dos bracos: {arm_movements_count}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        # Escrever o frame processado no vídeo de saída
        out.write(frame)

        # Exibir o frame processado
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Caminho para o vídeo de entrada e saída
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video_arm_up.mp4')  # Nome do vídeo de entrada
output_video_path = os.path.join(script_dir, 'output_video_arm_up.mp4')  # Nome do vídeo de saída

# Processar o vídeo
detect_pose_and_count_arm_movements(input_video_path, output_video_path)
```

Com isso, tivemos um resultado interessante. Agora, tente novas combinações e leia a documentação do mediapipe nos links:

https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker?hl=pt-br
https://developers.google.com/android/reference/com/google/mlkit/vision/pose/PoseLandmark.Type

Tente também novas análises com diferentes tipos de vídeo. Não deixe de praticar!
          
          

            
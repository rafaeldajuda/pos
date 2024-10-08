# cv2 - opencv é uma biblioteca utilizada para acessar a webcam
# https://pypi.org/project/opencv-python/
import cv2

def capture_video():
    # cap = cv2.VideoCapture(0, cv2.CAL_DSHOW) # caso precise acessar o drive da webcam
    cap  = cv2.VideoCapture(1)

    if not cap.isOpened():
        print('Erro ao acessar a webcam')
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # pegando os frames da webcam
    try:
        while True:
            ret, frame = cap.read()

            # se a webcam não retornar nada
            if not ret:
                break

            # convertendo para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # detectar faces
            # gray: A imagem em escala de cinza na qual a detecção de faces será feita.
            # scaleFactor=1.1: Especifica o quanto a imagem será reduzida a cada escala (1.1 significa reduzir em 10% a cada iteração).
            # minNeighbors=5: Define quantos vizinhos um retângulo candidato precisa ter para ser considerado como uma face. Valores mais altos resultam em menos detecções, mas mais precisas.
            # minSize=(30, 30): O menor tamanho que a face deve ter para ser detectada (em pixels). 
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # mostrando a imagem da webcam
            for (x, y, w, h) in faces:

                # frame: A imagem ou frame onde o retângulo será desenhado.
                # (x, y): Coordenadas do canto superior esquerdo do retângulo, correspondendo à face detectada.
                # (x+w, y+h): Coordenadas do canto inferior direito do retângulo (calculadas somando w (largura) e h (altura) à posição inicial x e y).
                # (255, 0, 0): A cor do retângulo no formato BGR (neste caso, azul).
                # 2: Espessura da linha do retângulo.
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            cv2.imshow('Face Detection', frame)

            # cv2.waitKey(1): Espera 1 milissegundo por uma tecla ser pressionada enquanto exibe o frame. Retorna o código da tecla pressionada.
            # & 0xFF: Garante compatibilidade ao pegar os últimos 8 bits do código da tecla (necessário em algumas plataformas).
            # ord('q'): Converte o caractere 'q' no código ASCII correspondente.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
    except KeyboardInterrupt:
        pass
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_video()
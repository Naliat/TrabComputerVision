from ultralytics import YOLO
import cv2

modelo = YOLO('yolov8n-pose.pt') 

cap = cv2.VideoCapture(0)

print("Iniciando a detecção. Pressione 'q' na janela do vídeo para sair.")

while cap.isOpened():
    sucesso, frame = cap.read()
    if not sucesso:
        print("Falha ao capturar a webcam.")
        break

    resultados = modelo(frame,verbose=False)

    for r in resultados:
        frame_anotado = r.plot()

        if r.keypoints is not None and len(r.keypoints.data) > 0:
            pontos = r.keypoints.data[0] 

            if len(pontos) >= 7:
                # Extrai Nariz (0), Ombro Esquerdo (5) e Ombro Direito (6)
                x_n, y_n, c_n = pontos[0]
                x_o_esq, y_o_esq, c_o_esq = pontos[5]
                x_o_dir, y_o_dir, c_o_dir = pontos[6] 

                # Transforma tudo em float
                y_n, y_o_esq, y_o_dir = float(y_n), float(y_o_esq), float(y_o_dir)
                x_o_esq, x_o_dir = float(x_o_esq), float(x_o_dir)
                c_n, c_o_esq, c_o_dir = float(c_n), float(c_o_esq), float(c_o_dir)

                alerta = ""

                if c_n > 0.5 and c_o_esq > 0.5 and c_o_dir > 0.5:
                    
                    # ALERTA 1: 
                    if (y_o_esq - y_n) < 90:
                        alerta = "Cabeca Baixa!"
                    
                    # ALERTA 2
                    elif abs(y_o_esq - y_o_dir) > 20:
                        alerta = "Ombros Desalinhados!"
                        
                    # ALERTA 3
                    elif abs(x_o_esq - x_o_dir) > 350:
                        alerta = "Muito perto da tela!"

                if alerta != "":
                    cv2.putText(
                        frame_anotado, 
                        f"ALERTA: {alerta}", 
                        (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (0, 0, 255), 
                        3 
                    )

    cv2.imshow('YOLOv8 Pose Detection - Apresentacao', frame_anotado)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
from ultralytics import YOLO
import cv2

# 1. Carrega o modelo pré-treinado de pose 
modelo = YOLO('yolov8n-pose.pt') 

# 2. Inicia a captura da webcam
cap = cv2.VideoCapture(0)

print("Iniciando a detecção. Pressione 'q' na janela do vídeo para sair.")

while cap.isOpened():
    sucesso, frame = cap.read()
    if not sucesso:
        print("Falha ao capturar a webcam.")
        break

    resultados = modelo(frame)

    for r in resultados:
        frame_anotado = r.plot()

        if r.keypoints is not None and len(r.keypoints.data) > 0:
            
            pontos = r.keypoints.data[0] 

            if len(pontos) >= 6:
                x_nariz, y_nariz, conf_nariz = pontos[0]
                x_ombro, y_ombro, conf_ombro = pontos[5]

                y_n = float(y_nariz)
                y_o = float(y_ombro)
                c_n = float(conf_nariz)
                c_o = float(conf_ombro)

                if c_n > 0.5 and c_o > 0.5:
                    
                    # LÓGICA DE NEGÓCIO: Avaliação de Postura
                    if y_n > y_o:
                        print(f"Alerta: Cabeça baixa! (Y do Nariz: {y_n:.1f} | Y do Ombro: {y_o:.1f})")
                        
                        cv2.putText(
                            frame_anotado, 
                            "ALERTA: Postura Incorreta!", 
                            (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            1, 
                            (0, 0, 255), 
                            3 
                        )

    cv2.imshow('YOLOv8 Pose Detection', frame_anotado)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Pose Detection com YOLOv8 🧍‍♂️🤖

Este projeto é uma demonstração prática de estimativa de pose (Pose Estimation) em tempo real utilizando Visão Computacional e Deep Learning. O script captura o feed da webcam e utiliza a arquitetura YOLOv8 para mapear o esqueleto humano, calculando métricas de postura em tempo real.

Projeto desenvolvido para fins de apresentação acadêmica/técnica.

## 🚀 Funcionalidades

- **Mapeamento de Keypoints:** Identifica e desenha as articulações do corpo (olhos, ombros, cotovelos, etc.) em tempo real.
- **Análise Biomecânica:** Extrai tensores das coordenadas numéricas de cada ponto detectado.
- **Alerta de Postura:** Lógica de negócio integrada que cruza a coordenada $Y$ do nariz com a coordenada $Y$ do ombro. Se a cabeça abaixar além do limite, o sistema emite um alerta visual na tela.
- **Alta Performance:** Utiliza o modelo `yolov8n-pose.pt` (versão nano), otimizado para rodar a altas taxas de FPS apenas com a CPU.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Ultralytics (YOLOv8)**
- **OpenCV**

## ⚙️ Instalação e Configuração

Recomenda-se o uso de um ambiente virtual (como Conda) para isolar as dependências do projeto.

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/poseDetection.git](https://github.com/SEU_USUARIO/poseDetection.git)
cd poseDetection
# Projeto: Detecção de Mãos em Tempo Real com IA

Este projeto utiliza a biblioteca `cv2` (OpenCV) e `cvzone` para realizar a detecção de mãos em tempo real através de uma webcam. O código captura imagens da webcam, processa-as para detectar as mãos e exibe as coordenadas dos pontos detectados.

## Funcionalidades

- Detecção de mãos em tempo real utilizando a webcam do computador.
- Exibição das coordenadas das mãos detectadas.
- Interface simples que mostra a imagem capturada e o rastreamento das mãos.

## Tecnologias Utilizadas

- **Python 3**
- **OpenCV (`cv2`)**: Para captura e processamento de imagens em tempo real.
- **cvzone**: Para simplificar o uso do módulo de detecção de mãos.
- **HandDetector**: Classe fornecida pelo `cvzone` para detecção de mãos com facilidade.

## Pré-requisitos

Para executar este projeto, você precisará ter as seguintes bibliotecas Python instaladas:

```bash
pip install opencv-python cvzone

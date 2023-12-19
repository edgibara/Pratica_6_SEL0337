#!/usr/bin/python3
import cv2 # Biblioteca OpenCV
import time # Biblioteca de tempo
import RPi.GPIO as GPIO
from time import sleep
from picamera2 import Picamera2 # Biblioteca da câmera da Raspberry Pi



GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)


# Carrega o classificador para detecção facial (informar o caminho do arquivo)
face_detector = cv2.CascadeClassifier("/home/sel/SEL-0337/haarcascade_frontalface_default.xml")
# Inicia uma thread para gerenciar janelas de visualização
cv2.startWindowThread()
# Inicializa a câmera da Raspberry Pi
picam2 = Picamera2()
# Configura a câmera para criar uma visualização com formato de representação
# de cores 32 bits “XRGB8888” e resolução de 640x480 pixels
picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size": (640, 480)}))
# Inicia a câmera
picam2.start()
# Loop para captura e detecção de rostos
while True:
# Captura um quadro da câmera e armazena na variável
	im = picam2.capture_array()
# Converte a imagem colorida para escala de cinza
	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Usa o classificador para encontrar olhos		
	eyes = eye_cascade.detectMultiScale(grey, 1.1, 5))
	for (x, y, w, h) in eyes:
		#Cria um retângulo vermelho onde o classificador encontra olhos
		cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0))
# Exibe a imagem com os retângulos desenhados em uma janela com o título "Camera"
	cv2.imshow("Camera", im)
	sleep(1)

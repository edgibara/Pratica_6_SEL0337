import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522
from gpiozero import LED

GPIO.setwarnings(False)
green = LED(26)
red = LED(21)
green.off()
red.off()
leitor=SimpleMFRC522()

print("Aproxime o tag do leitor para leitura")


while True:
    id,texto=leitor.read()
    if id==16625018518:
        print("TAG detectado, texto é:",texto)
        green.on()
        red.off()
        sleep(3)
    else:
        print("Tag nao reconhecido")
        green.off()
        red.on()
        sleep(3)

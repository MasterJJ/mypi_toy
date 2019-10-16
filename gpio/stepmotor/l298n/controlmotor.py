import RPi.GPIO as GPIO
import time
from collections import deque
GPIO.setmode(GPIO.BOARD)

ENA=29
IN1=28
IN2=27
IN3=25
IN4=24
ENB=23

sig=deque([0,1,0,1])
sig_end=deque([0,0,0,0,0,0])
step=400
dir=1
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)


try:
    while 1:
        for cnt in range(0, step):
            GPIO.output(AIN1,sig[0])
            GPIO.output(BIN1,sig[1])
            GPIO.output(AIN2,sig[2])
            GPIO.output(BIN2,sig[3])

            time.sleep(0.01)
            sig.rotate(dir)
        dir=dir*-1
except KeyboardInterrupt:
    pass
GPIO.cleanup()


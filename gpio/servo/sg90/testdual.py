import RPi.GPIO as GPIO
import time

pin = 18 # PWM pin num 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
sleep_t = 0.7
try:
    while True:
        p.ChangeDutyCycle(1)
        print "angle : 1"
        time.sleep(sleep_t)
        p.ChangeDutyCycle(12)
        print "angle : 8"
        time.sleep(sleep_t)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()



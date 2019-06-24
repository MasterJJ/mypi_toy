import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print "Setup LED pins as outputs"

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

cnt = 100

while cnt > 0 :
    GPIO.output(23, True)
    GPIO.output(24, True)

    print "on LED pins as outputs"
    time.sleep(1)

    GPIO.output(23, False)
    GPIO.output(24, False)
    cnt -= 1
    
    print "off LED pins as outputs"
    time.sleep(1)


raw_input('press enter to exit program')

GPIO.cleanup()

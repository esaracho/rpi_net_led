import RPi.GPIO as GPIO
import time
import threading

dev = "eth0"

def actividadred(dev, direcc):
    path = "/sys/class/net/{}/statistics/{}_bytes".format(dev, direcc)
    f = open(path, "r")
    bytes_antes = int(f.read())
    f.close()
    time.sleep(0.1)
    f = open(path, "r")
    bytes_despues = int(f.read())
    f.close()
    return (bytes_despues-bytes_antes)

def ledrx():
    while True:
        if actividadred(dev, "rx") > 3000:
            #LED rojo
            GPIO.output(11,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(11,GPIO.LOW)

def ledtx():
    while True:
        if actividadred(dev, "tx") > 500:
            #LED verde
            GPIO.output(24,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(24,GPIO.LOW)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

    rx = threading.Thread(target=ledrx)
    tx = threading.Thread(target=ledtx)

    rx.start()
    tx.start()

if __name__ == '__main__':
    main()

import RPi.GPIO as GPIO
import time
import math

BUZZER = 11 # define the BUZZER
GPIO_PIN = 12 # define the GPIO_PIN

def setup():
    global pwm
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(BUZZER, GPIO.OUT) # Set BUZZER's mode is output
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set BUTTON's mode is input, and pull up to high level(3.3V)
    pwm = GPIO.PWM(BUZZER, 1)
    pwm.start(0);
    
def main_loop():
    while True:
        time.sleep(2)
        alertor()
        print ('buzzer on ...')
        stopAlertor()
        print ('buzzer off ...')
        
def alertor():
    pwm.start(50)
    for x in range(0,361): #frequency of the alarm along the sine wave change
        sinVal = math.sin(x * (math.pi / 180.0)) #calculate the sine value
        toneVal = 2000 + sinVal * 500 #Add to the resonant frequency with a Weighted
        pwm.ChangeFrequency(toneVal) #output PWM
        time.sleep(0.001)

def stopAlertor():
    pwm.stop()

def quit():
    GPIO.output(BUZZER, GPIO.LOW) # buzzer off
    GPIO.cleanup() # Release resource

setup()

if __name__ == '__main__': # Program start from here  
    try:
        main_loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the subprogram quit() will be executed.
        quit()
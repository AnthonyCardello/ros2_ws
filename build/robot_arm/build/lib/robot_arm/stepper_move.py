import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)  # direction pin
GPIO.setup(23, GPIO.OUT)  # pulse pin

def move_motor(direction, steps):
    GPIO.output(24, direction)
    for _ in range(steps):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.001)

def main():
    # Example usage
    move_motor(GPIO.HIGH, 100)  # Move forward
    time.sleep(1)
    move_motor(GPIO.LOW, 100)   # Move backward
    time.sleep(1)
    GPIO.cleanup()

if __name__ == '__main__':
    main()

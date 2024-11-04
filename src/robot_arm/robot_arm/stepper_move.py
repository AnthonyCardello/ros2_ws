import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # direction pin
GPIO.setup(20, GPIO.OUT)  # pulse pin

def move_motor(direction, steps):
    GPIO.output(21, direction)
    for _ in range(steps):
        GPIO.output(20, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(20, GPIO.LOW)
        time.sleep(0.0001)

def main():
    # Example usage
    move_motor(GPIO.HIGH, 5000)  # Move forward
    time.sleep(1)
    move_motor(GPIO.LOW, 5000)   # Move backward
    time.sleep(1)
    move_motor(GPIO.HIGH, 10000)  # Move forward
    GPIO.cleanup()

if __name__ == '__main__':
    main()

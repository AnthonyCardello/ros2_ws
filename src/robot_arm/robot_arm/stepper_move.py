import RPi.GPIO as GPIO
import time

# GPIO setup
print("ok that is doing somthing")
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # direction pin
GPIO.setup(20, GPIO.OUT)  # pulse pin
GPIO.output(21, 1)

def move_motor(direction, steps):
    print("move moter is called")
    GPIO.output(21, direction)
    for _ in range(steps):
        GPIO.output(20, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(20, GPIO.LOW)
        time.sleep(0.001)

def main():
    print("main is here")
    # Example usage
    move_motor(GPIO.HIGH, 100)  # Move forward
    time.sleep(1)
    move_motor(GPIO.LOW, 100)   # Move backward
    time.sleep(1)
    GPIO.cleanup()

if __name__ == '__main__':
    print("what the sigma")
    main()

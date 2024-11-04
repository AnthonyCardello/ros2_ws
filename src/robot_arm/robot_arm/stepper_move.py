import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # direction pin
GPIO.setup(20, GPIO.OUT)  # pulse pin

def move_motor(direction, steps):
    print(f"Moving motor {'Forward' if direction == GPIO.HIGH else 'Backward'}")
    GPIO.output(21, direction)
    for _ in range(steps):
        GPIO.output(20, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(20, GPIO.LOW)
        time.sleep(0.001)
    print("Motor movement complete")

def main():
    print("Starting main function")
    move_motor(GPIO.HIGH, 100)  # Move forward
    time.sleep(1)
    move_motor(GPIO.LOW, 100)   # Move backward
    time.sleep(1)
    GPIO.cleanup()
    print("Main function complete")

if __name__ == '__main__':
    print("Executing as script")
    main()

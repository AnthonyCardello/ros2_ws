import RPi.GPIO as GPIO
import time
#thanks chatgpt
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Function to move the motor
def move_motor(direction, steps):
    GPIO.output(20, direction)
    for _ in range(steps):
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(22, GPIO.LOW)
        time.sleep(0.001)

# Example usage
move_motor(GPIO.HIGH, 100)  # Move forward
time.sleep(1)
move_motor(GPIO.LOW, 100)   # Move backward
time.sleep(1)

# Cleanup
GPIO.cleanup()

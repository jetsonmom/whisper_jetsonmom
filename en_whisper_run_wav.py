import os
import time
import whisper
import smbus as smbus
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from Adafruit_GPIO import I2C
from Adafruit_PCA9685 import PCA9685
from adafruit_servokit import ServoKit

def setup_pwm():
    try:
        pwm = PCA9685(0x40, busnum=7)
        pwm.set_pwm_freq(50)
        servo_kit = ServoKit(channels=16, address=0x60)
        return pwm, servo_kit
    except Exception as e:
        print("Failed to initialize PWM or ServoKit:", e)
        return None, None

class MotorDriver:
    def __init__(self, pwm):
        self.pwm = pwm
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, direction, speed):
        duty_cycle = int(speed * 40.95)
        motor_channels = [self.PWMA, self.PWMB][motor]
        dir_channels = [self.AIN1, self.AIN2] if direction == 'forward' else [self.AIN2, self.AIN1]
        self.pwm.set_pwm(motor_channels, 0, duty_cycle)
        self.pwm.set_pwm(dir_channels[0], 0, 4095)
        self.pwm.set_pwm(dir_channels[1], 0, 0)

    def MotorStop(self, motor):
        self.pwm.set_pwm([self.PWMA, self.PWMB][motor], 0, 0)

    def steer(self, angle, servo_kit):
        servo_kit.servo[0].angle = angle

def load_model():
    model = whisper.load_model("base")
    return model

def execute_commands_from_audio(audio_path, model, motor, servo_kit):
    result = model.transcribe(audio_path)
    commands = result['text'].lower().split()
    valid_commands = ['forward', 'backward', 'left', 'right', 'stop']
    filtered_commands = [cmd for cmd in commands if cmd in valid_commands]
    print("Recognized commands:", commands)
    for command in filtered_commands:
        if command in valid_commands:
            print(f"Executing command: {command}")
            if command == 'forward':
                motor.MotorRun(0, 'forward', 100)
                motor.MotorRun(1, 'backward', 100)
                print("forward run")
            elif command == 'backward':
                motor.MotorRun(0, 'backward', 100)
                motor.MotorRun(1, 'forward', 100)
                print("backward run")
            elif command == 'left':
                motor.steer(45, servo_kit)
            elif command == 'right':
                motor.steer(135, servo_kit)
            elif command == 'stop':
                motor.MotorStop(0)
                motor.MotorStop(1)
            time.sleep(1)

if __name__ == "__main__":
    pwm, servo_kit = setup_pwm()
    if pwm and servo_kit:
        motor = MotorDriver(pwm)
        model = load_model()
        audio_path = 'test.wav'
        execute_commands_from_audio(audio_path, model, motor, servo_kit)


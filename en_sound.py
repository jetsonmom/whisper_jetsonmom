import os
import time
import whisper
from adafruit_servokit import ServoKit
from Adafruit_PCA9685 import PCA9685

# 인스턴스 생성 시 I2C 버스 번호 명시
def setup_pwm():
    try:
        pwm = PCA9685(busnum=7)  # 사용 가능한 I2C 버스 번호로 변경
        pwm.set_pwm_freq(50)  # PWM 주파수 설정 (Hz)
        return pwm
    except Exception as e:
        print("Error initializing PCA9685:", str(e))
        return None

# 모터 드라이버 설정
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
        duty_cycle = int(speed * 40.95)  # 0-100 범위를 0-4095로 변환
        motor_channels = [self.PWMA, self.PWMB][motor]
        dir_channels = [self.AIN1, self.AIN2] if direction == 'forward' else [self.AIN2, self.AIN1]
        self.pwm.set_pwm(motor_channels, 0, duty_cycle)
        self.pwm.set_pwm(dir_channels[0], 0, 4095)
        self.pwm.set_pwm(dir_channels[1], 0, 0)

    def MotorStop(self, motor):
        self.pwm.set_pwm([self.PWMA, self.PWMB][motor], 0, 0)

    def steer(self, angle, servo_kit):
        servo_kit.servo[0].angle = angle

# Whisper 모델 로드
def load_model():
    model = whisper.load_model("base")
    return model

# 오디오 파일 필사 및 명령 실행
def execute_commands_from_audio(audio_path, model, motor, servo_kit):
    result = model.transcribe(audio_path)
    commands = result['text'].lower().split()
    valid_commands = ['forward', 'backward', 'left', 'right', 'stop']
    filtered_commands = [cmd for cmd in commands if cmd in valid_commands]
    print("Recognized commands:", commands)  # 인식된 명령어들 출력
    for command in filtered_commands:
        if command in ['forward', 'backward', 'stop', 'left', 'right']:
            if command == 'forward':
                motor.MotorRun(0, 'forward', 100)
                motor.MotorRun(1, 'backward', 100)
                time.sleep(5)
                print("forward run")
            elif command == 'backward':
                motor.MotorRun(0, 'backward', 100)
                motor.MotorRun(1, 'forward', 100)
                time.sleep(5)
                print("backward run")
            elif command == 'left':
                motor.steer(45, servo_kit)  # 좌회전
                motor.MotorRun(0, 'forward', 100)
                motor.MotorRun(1, 'backward', 100)
            elif command == 'right':
                motor.steer(135, servo_kit) # 우회전
                motor.MotorRun(0, 'forward', 100)
                motor.MotorRun(1, 'backward', 100)
            elif command == 'stop':
                motor.MotorStop(0)
                motor.MotorStop(1)
            time.sleep(1)  # 명령 실행 후 잠시 대기
            print(f"Executing command: {command}")

if __name__ == "__main__":
    pwm = setup_pwm()
    if pwm:
        servo_kit = ServoKit(channels=16)
        motor = MotorDriver(pwm)
        model = load_model()
        audio_path = 'test.wav'
        execute_commands_from_audio(audio_path, model, motor, servo_kit)


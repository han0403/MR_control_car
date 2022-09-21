import RPi.GPIO as GPIO
import pygame
import time
import sys


print('start program')


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# front left
F_IN1 = 17
F_IN2 = 18

# front right
F_IN3 = 27
F_IN4 = 22

# back left
B_IN1 = 13
B_IN2 = 12

#back right
B_IN3 = 5
B_IN4 = 6


# 驅動板
GPIO.setup(F_IN1,GPIO.OUT)
GPIO.setup(F_IN2,GPIO.OUT)
GPIO.setup(F_IN3,GPIO.OUT)
GPIO.setup(F_IN4,GPIO.OUT)

GPIO.setup(B_IN1,GPIO.OUT)
GPIO.setup(B_IN2,GPIO.OUT)
GPIO.setup(B_IN3,GPIO.OUT)
GPIO.setup(B_IN4,GPIO.OUT)


# 設定馬達初始頻率
PWM_Freq = 50

pwmB_IN1 = GPIO.PWM(B_IN1, PWM_Freq)
pwmB_IN2 = GPIO.PWM(B_IN2, PWM_Freq)
pwmB_IN3 = GPIO.PWM(B_IN3, PWM_Freq)
pwmB_IN4 = GPIO.PWM(B_IN4, PWM_Freq)

pwmF_IN1 = GPIO.PWM(F_IN1, PWM_Freq)
pwmF_IN2 = GPIO.PWM(F_IN2, PWM_Freq)
pwmF_IN3 = GPIO.PWM(F_IN3, PWM_Freq)
pwmF_IN4 = GPIO.PWM(F_IN4, PWM_Freq)


# 設定馬達能量
pwmB_IN1.start(0)
pwmB_IN2.start(0)
pwmB_IN3.start(0)
pwmB_IN4.start(0)

pwmF_IN1.start(0)
pwmF_IN2.start(0)
pwmF_IN3.start(0)
pwmF_IN4.start(0)


# front
def MoveForward(x):
    print('MoveForward ')

    pwmB_IN1.ChangeDutyCycle(0)
    pwmB_IN3.ChangeDutyCycle(0)
    pwmF_IN1.ChangeDutyCycle(0)
    pwmF_IN3.ChangeDutyCycle(0)

    pwmB_IN2.ChangeDutyCycle(abs(50*x))
    pwmB_IN4.ChangeDutyCycle(abs(50*x))
    pwmF_IN2.ChangeDutyCycle(abs(50*x))
    pwmF_IN4.ChangeDutyCycle(abs(50*x))


# back
def MoveBack(x):
    print('MoveBack ')

    pwmB_IN2.ChangeDutyCycle(0)
    pwmB_IN4.ChangeDutyCycle(0)
    pwmF_IN2.ChangeDutyCycle(0)
    pwmF_IN4.ChangeDutyCycle(0)

    pwmB_IN1.ChangeDutyCycle(abs(50*x))
    pwmB_IN3.ChangeDutyCycle(abs(50*x))
    pwmF_IN1.ChangeDutyCycle(abs(50*x))
    pwmF_IN3.ChangeDutyCycle(abs(50*x))


# stop
def Stop():
    print('Stop() ')
    pwmB_IN1.ChangeDutyCycle(0)
    pwmB_IN2.ChangeDutyCycle(0)
    pwmB_IN3.ChangeDutyCycle(0)
    pwmB_IN4.ChangeDutyCycle(0)

    pwmF_IN1.ChangeDutyCycle(0)
    pwmF_IN2.ChangeDutyCycle(0)
    pwmF_IN3.ChangeDutyCycle(0)
    pwmF_IN4.ChangeDutyCycle(0)


# left
def MoveLeft(x):
    print('MoveLeft() ')
    pwmB_IN1.ChangeDutyCycle(0)
    pwmB_IN2.ChangeDutyCycle(abs(60*x))
    pwmB_IN3.ChangeDutyCycle(0)
    pwmB_IN4.ChangeDutyCycle(abs(60*x))

    pwmF_IN1.ChangeDutyCycle(15)
    pwmF_IN2.ChangeDutyCycle(0)
    pwmF_IN3.ChangeDutyCycle(0)
    pwmF_IN4.ChangeDutyCycle(abs(60*x))


# right
def MoveRight(x):
    print('MoveRight()')
    pwmB_IN1.ChangeDutyCycle(0)
    pwmB_IN2.ChangeDutyCycle(abs(60*x))
    pwmB_IN3.ChangeDutyCycle(0)
    pwmB_IN4.ChangeDutyCycle(abs(60*x))

    pwmF_IN1.ChangeDutyCycle(0)
    pwmF_IN2.ChangeDutyCycle(abs(60*x))
    pwmF_IN3.ChangeDutyCycle(15)
    pwmF_IN4.ChangeDutyCycle(0)


# backleft
def MoveBackLeft(x):
    print('MoveBackLeft() ')
    pwmB_IN1.ChangeDutyCycle(abs(60*x))
    pwmB_IN2.ChangeDutyCycle(0)
    pwmB_IN3.ChangeDutyCycle(abs(60*x))
    pwmB_IN4.ChangeDutyCycle(0)

    pwmF_IN1.ChangeDutyCycle(0)
    pwmF_IN2.ChangeDutyCycle(15)
    pwmF_IN3.ChangeDutyCycle(abs(60*x))
    pwmF_IN4.ChangeDutyCycle(0)


# backright
def MoveBackRight(x):
    print('MoveBackRight()')
    pwmB_IN1.ChangeDutyCycle(abs(60*x))
    pwmB_IN2.ChangeDutyCycle(0)
    pwmB_IN3.ChangeDutyCycle(abs(60*x))
    pwmB_IN4.ChangeDutyCycle(0)

    pwmF_IN1.ChangeDutyCycle(abs(60*x))
    pwmF_IN2.ChangeDutyCycle(0)
    pwmF_IN3.ChangeDutyCycle(0)
    pwmF_IN4.ChangeDutyCycle(15)



pygame.init()
pygame.joystick.init()


# 檢查搖桿名稱
if pygame.joystick.get_init():
    #print('JoyStick Count:', pygame.joystick.get_count(),'\n')

    # 設定使用搖桿0
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # 取得搖桿名稱
    name = joystick.get_name()
    print('JoyStick Name:', name)

    # 取得搖桿軸數量
    numaxes = joystick.get_numaxes()
    print('axes Count:', numaxes)

    # 取得搖桿按鈕數量
    numbuttons = joystick.get_numbuttons()
    print('button Count:', numbuttons)
    

while True :
    for event in pygame.event.get() :
        if event.type == pygame.JOYBUTTONDOWN :
            if joystick.get_button(10) == 1 :
                MoveForward(1)

            elif joystick.get_button(5) == 1 :
                MoveLeft(1)

            elif joystick.get_button(4) == 1 :
                MoveRight(1)

            elif joystick.get_button(11) == 1 :
                MoveBack(1)

            elif joystick.get_button(6) == 1 :
                MoveBackLeft(1)

            elif joystick.get_button(7) == 1 :
                MoveBackRight(1)

            elif joystick.get_button(0) == 1 :
                Stop()

            elif joystick.get_button(2) == 1 :
                pygame.quit()


# 釋放清理
pwmB_IN1.stop()
pwmB_IN2.stop()
pwmB_IN3.stop()
pwmB_IN4.stop()

pwmF_IN1.stop()
pwmF_IN2.stop()
pwmF_IN3.stop()
pwmF_IN4.stop()
GPIO.cleanup()

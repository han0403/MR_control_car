import pygame


pygame.init()


# 搖桿初始化
pygame.joystick.init()
pygame.joystick.Joystick(0).init


if pygame.joystick.get_init():
    print('JoyStick Count:', pygame.joystick.get_count(),'\n')

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
    

    numhats = joystick.get_numhats()
    print('hats Count:',numhats)
    
while True :
    event = pygame.event.get()

    axis1 = joystick.get_axis(1)
    BUTTON_S = joystick.get_button(2)
    
    if axis1 > 0 :
        print("OK!")
        print(axis1)

    elif BUTTON_S :
        print("STOP!")
        pygame.quit()



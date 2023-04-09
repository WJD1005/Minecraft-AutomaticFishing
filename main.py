import cv2 as cv
import pyautogui
import time
import keyboard

version = 'V1.0.1'
# 更新日志
# V1.0.0 实现了钓鱼基本功能
# V1.0.1 增加了开始钓鱼、暂停钓鱼的全局快捷键，使用更加方便

run = 0


def start_stop():
    global run
    if run:
        run = 0
        print('已暂停')
    else:
        run = 1
        print('已开始')


# 获取用户屏幕分辨率
width, height = pyautogui.size()
x = int(885 / 1920 * width)
y = int(440 / 1080 * height)
size = int(150 / 1920 * width)

# 快捷键监听
keyboard.add_hotkey('u', start_stop)

print('MC辅助钓鱼 %s  by 星云质心\n' % version)

while True:
    if run:
        red = 0
        pyautogui.screenshot('screen.png', region=(x, y, size, size))
        screen = cv.imread('screen.png')
        for i in screen:
            for j in i:
                if j[2] > 200:
                    red += 1
        print(red)
        if red < 500:
            print('收杆！')
            pyautogui.rightClick()
            time.sleep(1)
            print('放杆！')
            pyautogui.rightClick()
            time.sleep(3)

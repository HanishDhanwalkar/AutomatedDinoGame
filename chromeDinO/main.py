import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    return

def iscollide():
    '''To check daylight'''
    for a in range(100, 110):
        for b in range(200, 210):

            if data2[a,b] > 150:

                for i in range(400, 600):
                    for j in range(675, 700):
                        if data[i, j] < 151:
                            hit('up')
                            return
                for i in range(400, 480):
                    for j in range(550, 575):
                        if data[i, j] < 151:
                            hit('down')
                            return
            else:
                for i in range(400, 600):
                    for j in range(675, 700):
                        if data[i, j] > 150:
                            hit('up')
                            return
                for i in range(400, 480):
                    for j in range(550, 575):
                        if data[i, j] > 150:
                            hit('down')
                            return
    return False

if __name__ == '__main__':
    time.sleep(1)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        data2 = image.load()

        # print(asarray(image))
        iscollide()

        # Draaw the rect

        # for a in range(45, 67):
        #     for b in range(167, 180):
        #
        #          data2[a,b] =0
        #
        # image.show()
        # break
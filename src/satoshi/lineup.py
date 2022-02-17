from random import random
import pyautogui
from time import sleep
from src import helper

def execute():

    while (True):

        sleep(1)
        clickIngameButtons()

        nextButton = getNextButtons()

        if len(nextButton) == 0:
            break

        (x, y, w, h) = nextButton[0]

        pyautogui.moveTo(x + (w/2), y + (h / 2), 1 + random() / 5)
        pyautogui.click()


    print('Click on confirm')
    helper.clickDestinationImage('ssm_confirm.png', 'ssm_confirm')

def getNextButtons():
    screen = helper.printSreen()

    positions = helper.getImagePositions('ssm_next.png', 0.9, screen)

    print('selected next buttons: ', len(positions))
    return positions


def clickIngameButtons():

    screen = helper.printSreen()

    for (x, y, w, h) in getIngameButtons(screen):
        pyautogui.moveTo(x + (w/2), y + (h / 2), 1 + random() / 10)
        pyautogui.click()

def getIngameButtons(screen):
    positions = helper.getImagePositions('ssm_ingame.png', 0.9, screen)

    print('selected ingame buttons: ', len(positions))
    return positions

# -*- coding: utf-8 -*-

import pyautogui
import time
import sys
from src.luna import heroselect, bosshunt, fight, login_luna
from src import helper

pyautogui.FAILSAFE = False


def luna_main():

    time.sleep(1)

    while(True):
        try:
            screen = helper.printSreen()
            if(isLoginScreen(screen)):
                print('Login screen found!!!')
                login_luna.doLogin()

            screen = helper.printSreen()
            if(isModeSelectScreen(screen)):
                print('Mode select found!!!')
                helper.clickDestinationImage('boss-fight-mode-icon.png', 'boss-fight-mode')

            screen = helper.printSreen()
            if(isBossHuntStageSelect(screen)):
                print('Boss stage select screen found!!!')
                bosshunt.execute()

            screen = helper.printSreen()
            if(isHeroSelectScreen(screen)):
                print('Hero select screen found!!!')
                heroselect.execute(screen)

            screen = helper.printSreen()
            fight.execute(screen)

            sys.stdout.flush()

            print('waiting...')
            time.sleep(1)
        except:
            break


def isLoginScreen(screen):
    positions = helper.getImagePositions('connect-wallet.png', 0.7, screen)

    return len(positions) > 0


def isModeSelectScreen(screen):
    positions = helper.getImagePositions(
        'boss-fight-mode-icon.png', 0.7, screen)

    return len(positions) > 0


def isModeSelectScreen(screen):
    positions = helper.getImagePositions(
        'boss-fight-mode-icon.png', 0.7, screen)

    return len(positions) > 0


def isBossHuntStageSelect(screen):
    positions = helper.getImagePositions('boss-hunt-map.png', 0.7, screen)

    return len(positions) > 0


def isHeroSelectScreen(screen):
    positions = helper.getImagePositions('boss-hunt-button.png', 0.7, screen)

    return len(positions) > 0


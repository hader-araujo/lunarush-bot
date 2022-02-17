# -*- coding: utf-8 -*-

import pyautogui
import time
import sys
from src import helper
from src.satoshi import lineup

pyautogui.FAILSAFE = False

def satoshi_main():

    print('Click on tower')
    helper.clickDestinationImage('ssm_tower.png', 'ssm_tower')

    print('Click on lineup')
    helper.clickDestinationImage('ssm_lineup.png', 'ssm_lineup')

    lineup.execute()

    print('Click on farm')
    helper.clickDestinationImage('ssm_farm.png', 'ssm_farm')
    sys.stdout.flush()

    print('fim satoshi ...')
    time.sleep(1)


def check_next_map():

    try:
        print('Checking next map')
        if helper.clickDestinationImage('ssm_next_map.png', 'ssm_next_map'):
            time.sleep(1)
    except:
        pass



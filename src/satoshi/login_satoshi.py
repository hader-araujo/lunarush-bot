
import pyautogui
from src.helper import clickDestination
from time import sleep
from src import helper

def doLogin():

    print('>>> Refreshing screen')
    pyautogui.hotkey('ctrl', 'f5')

    sleep(15)

    print('Fim do sleep do ctrl F5')

    print("Vai clicar no wallet")
    if clickDestination('connect-wallet.png', name='connect-wallet-btn', timeout=15):
        print('Logging in!')

    if clickDestination('wallet-sign.png', name='sign button', timeout=15):
        sleep(20)
#
#     ssm_input_text
#
# def setUserNameAndPassword:
#
#     inputs = ['hader']
#     for (x, y, w, h) in getIngameButtons(screen):
#         pyautogui.moveTo(x+100, y, 1 + random()/2)
#         pyautogui.click()
#         sleep(1)
#
# def getInputTexts(screen):
#     positions = helper.getImagePositions('ssm_input_text.png', 0.9, screen)
#
#     print('selected inputs: ', len(positions))
#     return positions

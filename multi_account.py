import sys
import time
import pygetwindow

from src.satoshi import login_satoshi
from index_luna import luna_main
from index_satoshi import satoshi_main, check_next_map


def runMultiAccount():
    time.sleep(5)

    windows = []
    title_luna = 'Luna Rush'
    title_satoshi = 'SatoshiMonsters!'

    print('🆗 Start')

    for w in pygetwindow.getWindowsWithTitle(title_luna):
        windows.append({
            "window": w,
            "title": title_luna,
            "play_time": 10 * 60,
            "last_play_time": 0,
        })

    for w in pygetwindow.getWindowsWithTitle(title_satoshi):
        windows.append({
            "window": w,
            "title": title_satoshi,
            "play_time": 25 * 60,
            "last_play_time": 0,
            "new_map_time": 1 * 60,
            "last_new_map_time": 0,
            # "refresh_time": 10 * 60,
            # "last_refresh_time": 0,
        })

    print('Found {} window(s):'.format(len(windows)))
    for index, last in enumerate(windows):
        print('{} -> {}'.format(index + 1, last['window'].title))

    if len(windows) == 0:
        print('Exiting because dont have windows contains "{}" or {} title'.format(title_luna, title_satoshi))
        exit()

    while True:

        for index, last in enumerate(windows):

            print('CLIENT ACTIVE WINDOW -> {} : {}'.format(index + 1, last['window'].title))
            time.sleep(2)

            now = time.time()

            if last['title'] == title_luna:

                if now - last["last_play_time"] > last['play_time']:

                    last["window"].activate()
                    luna_main()
                    last["last_play_time"] = now

            if last['title'] == title_satoshi:
                if now - last["last_play_time"] > last['play_time']:

                    last["window"].activate()
                    satoshi_main()
                    last["last_play_time"] = now

                if now - last["last_new_map_time"] > last['new_map_time']:

                    last["window"].activate()
                    check_next_map()
                    last["last_new_map_time"] = now

                # if now - last["last_refresh_time"] > last['refresh_time']:
                #
                #     last["last_refresh_time"] = now
                #     last["window"].activate()
                #
                #     login_satoshi.doLogin()

            time.sleep(1)

        time.sleep(1 * 5)

    sys.stdout.flush()

runMultiAccount()

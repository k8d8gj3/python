import pyautogui
import time

# def auto_box():
#     pyautogui.click(500, 170, duration=1)
#     time.sleep(35)
#     pyautogui.press('esc')
#     pyautogui.sleep(5)
#     pyautogui.press('space')
#     return auto_box()

def enter_store():
    shop_pos = pyautogui.locateOnScreen('shop-button.png', confidence=0.8)
    if not shop_pos:
        pyautogui.press('esc')
        pyautogui.press('esc')
        return False
    pyautogui.click(int(shop_pos[0])+50, int(shop_pos[1])+40, duration=1)
    time.sleep(2)
    store_pos = pyautogui.locateOnScreen('store-button.png', confidence=0.8)
    if not store_pos:
        pyautogui.press('esc')
        pyautogui.press('esc')
        return False
    pyautogui.click(int(store_pos[0])+30, int(store_pos[1])+20, duration=1)
    return True


def auto_watch(counter=0):
    print('auto watching ads...')
    if counter > 15:
        print('watch button not found...')
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('esc')
        return False
    button_pos = pyautogui.locateOnScreen('watch-button.png', confidence=0.6)
    if not button_pos:
        print('searching for the watch button')
        pyautogui.scroll(-1)
        time.sleep(1)
        return auto_watch(counter+1)
    pyautogui.click(int(button_pos[0])+130, int(button_pos[1])+170, duration=1)
    time.sleep(35)
    pyautogui.press('esc')
    pyautogui.sleep(2)
    pyautogui.press('space')
    return auto_watch()

while True:
    time.sleep(3)
    # auto_box()
    auto_watch()
    enter_store()
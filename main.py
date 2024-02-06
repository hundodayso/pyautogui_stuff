import pyautogui
import PIL
import time

game_on = True
for i in range(0,4):
    time.sleep(1)
    im = pyautogui.screenshot(region=(855, 145, 1033, 1264))
    im.save(f'screenshot{i}.png')
    pyautogui.click(104,130)
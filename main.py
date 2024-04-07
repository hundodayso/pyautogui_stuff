import pyautogui
import PIL
import time
import cv2

game_on = True
for i in range(0,1):
    time.sleep(1)
    im = pyautogui.screenshot(region=(855, 145, 1033, 1264))
    im.save(f'screenshot{i}.png')
    im_filename = (f'screenshot{i}.png')
    cv2_img = cv2.imread(im_filename,1)
    # cv2.imshow('Seen Image', cv2_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(cv2_img[10][1000])

    pyautogui.click(104,130)
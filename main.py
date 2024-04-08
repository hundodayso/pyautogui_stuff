import pyautogui
import PIL
import time
import cv2
import os



PORTRAIT_REGION = (785, 145, 1000, 1260)
LANDSCAPE_REGION = (456, 145, 1260, 974)
LANDSCAPE_REGION_PGFIT = (456, 145, 1640, 1260)
NEXT_PAGE_BTN = (104, 130) #x, y
IMG_CHECK_Y = 200
IMG_CHECK_X = 1539


def is_rotated(pixel_colour):
    colour_total = 0

    for colour in pixel_colour:
        #print(f'This is the {colour}')
        colour_total += colour
        #print(f'This is the total: {colour_total}')
    if colour_total == 130:
        return True
    else:
        return False

def rotate_clockwise():
    #open menu
    pyautogui.click(2541, 129)
    #rotate page
    pyautogui.click(2418, 298)
    #close menu
    pyautogui.click(2541, 129)

def rotate_anticlockwise():
    # open menu
    pyautogui.click(2541, 129)
    # rotate page
    pyautogui.click(2418, 327)
    # close menu
    pyautogui.click(2541, 129)

def take_screenshot(i):
    im = pyautogui.screenshot(region=LANDSCAPE_REGION_PGFIT)
    im_filename = (f'screenshot{i}.png')
    im.save(im_filename)
    return im_filename

for i in range(0,3):
    time.sleep(1)
    filename = take_screenshot(i)

    cv2_img = cv2.imread(filename,1)
    colour_check = cv2_img[IMG_CHECK_Y][IMG_CHECK_X]

    if is_rotated(colour_check):
        print("true")
        os.remove(filename)
        rotate_clockwise()
        time.sleep(1)
        take_screenshot(i)
        rotate_anticlockwise()

    else:
        cv2.rotate(cv2_img, cv2.ROTATE_90_CLOCKWISE)
        print("false")



    #print(cv2_img[IMG_CHECK_Y][IMG_CHECK_Y])


    # cv2.imshow('Seen Image', cv2_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    pyautogui.click(NEXT_PAGE_BTN)




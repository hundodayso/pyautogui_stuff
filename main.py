import pyautogui
import PIL
import time
import cv2



PORTRAIT_REGION = (785, 145, 1000, 1260)
LANDSCAPE_REGION = (456, 145, 1260, 974)
LANDSCAPE_REGION_PGFIT = (456, 145, 1640, 1260)
NEXT_PAGE_BTN = (104, 130) #x, y
IMG_CHECK_Y = 200
IMG_CHECK_X = 1539


def is_portrait(pixel_colour):
    colour_total = 0

    for colour in pixel_colour:
        print(f'This is the {colour}')
        colour_total += colour
        print(f'This is the total: {colour_total}')
    if colour_total == 130:
        return True
    else:
        return False




for i in range(0,3):
    time.sleep(1)
    im = pyautogui.screenshot(region=LANDSCAPE_REGION_PGFIT)
    im_filename = (f'screenshot{i}.png')
    im.save(im_filename)

    cv2_img = cv2.imread(im_filename,1)
    colour_check = cv2_img[IMG_CHECK_Y][IMG_CHECK_X]
    print(f'This is colourcheck: {colour_check}')
    is_portrait(colour_check)



    #print(cv2_img[IMG_CHECK_Y][IMG_CHECK_Y])


    # cv2.imshow('Seen Image', cv2_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    pyautogui.click(NEXT_PAGE_BTN)




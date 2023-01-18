import pyautogui
import keyboard
import time


def cautare_google():
    if pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\image.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\image.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("https://www.youtube.com/")
        pyautogui.press('enter')
    else:
        print("IMAGINEA NU SE AFLA PE ECRAN")


def coordonate():
    print(pyautogui.position())


time.sleep(2)


coordonate()

cautare_google()

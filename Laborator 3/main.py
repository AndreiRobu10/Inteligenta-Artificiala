import pyautogui
import keyboard
import time


def cautare_google():
    if pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\image.png', confidence=0.7) is not None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\image.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
        pyautogui.press('enter')
        time.sleep(5)
        subscribe = pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\subscribe.png', confidence=0.7)
        pyautogui.click(subscribe)
        videoclipuri = pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\videoclipuri.png', confidence=0.7)
        pyautogui.click(videoclipuri)
        back = pyautogui.locateOnScreen(r'C:\Users\andre\Desktop\back.png', confidence=0.7)
        x = 570
        y = 820
        scrollValue = 0
        for i in range(0, 2):
            for j in range(0, 4):
                time.sleep(1)
                pyautogui.click(x, y)
                time.sleep(4)
                pyautogui.click(pyautogui.position(239, 927))
                time.sleep(1)
                pyautogui.click(videoclipuri)
                time.sleep(2)
                pyautogui.scroll(scrollValue)
                x = x + 350
            scrollValue = scrollValue - 300
            x = 570

    else:
        print("IMAGINEA NU SE AFLA PE ECRAN")


def coordonate():
    print(pyautogui.position())


time.sleep(1.5)


coordonate()

cautare_google()

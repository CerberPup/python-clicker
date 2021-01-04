import pyautogui
import os
import time

def findAndClick(image):
    try:
        x,y = pyautogui.locateCenterOnScreen(image)
        pyautogui.click(x, y)
    except:
        print(f"Nie znaleziono {image}")

if __name__ == "__main__":
    interval=30
    filename="toclick.png"
    while True:
        finput = input("nazwa pliku do klikniecia (domyslnie toclick.png):")
        if finput == "" and os.path.exists(filename):
            break
        if os.path.exists(finput):
            filename = finput
            print(f'Klikne w "{filename}"')
            break
        print(f'"{finput}" nie istnieje')
    while True:
        iinput = input("Co ile sekund klikac? (domyslnie 30):")
        if iinput == "":
            break
        try:
            interval=int(iinput)
            break
        except:
            pass
    print(f'Klikne co {interval}s')

    while True:
        findAndClick(filename)
        time.sleep(interval)
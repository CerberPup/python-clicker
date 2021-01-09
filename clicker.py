import pyautogui
import os
import time

def findAndClick(image, confidence=0.95):
    try:
        x,y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        pyautogui.click(x, y)
        print(f"Kilk {x},{y}")
    except:
        print(f"Nie znaleziono {image}")

if __name__ == "__main__":
    interval=30
    confidence=0.95
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
    print(f'"Spróbuję kliknąć co {interval}s')
    while True:
        iconfidence = input("Z jaką dokładnośćią szukać? (domyslnie 95):")
        if iconfidence == "":
            break
        try:
            confidence=int(iconfidence)/100
            break
        except:
            pass
    print(f'Znajdę z dokładnością {confidence*100}%')

    while True:
        findAndClick(filename,confidence)
        time.sleep(interval)
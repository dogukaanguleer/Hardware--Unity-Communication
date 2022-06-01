import pyautogui

# Holds down the alt key
pyautogui.keyDown("alt")

# Presses the tab key once
pyautogui.press("tab")
# Lets go of the alt key



pyautogui.keyUp("alt")
val = 1
if val==1:
    pyautogui.press("z")
elif val==2:
    pyautogui.press("x")
elif val==3:
    pyautogui.press("c")

# Made By Prashanth Umapathy
# Specialises in Extreme Laziness

# Very important imports
import webbrowser, time
import pyautogui as pag
import schedule


# Meeing info

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


# Opens the meeting ID
def meeting_join(url):
    webbrowser.get(chrome_path).open(url)

    time.sleep(8)

    pag.hotkey('ctrl','d')
    pag.hotkey('ctrl','e')

    time.sleep(6)

    for i in range(8):                              
        pag.press('tab')

    time.sleep(2)
    pag.press('enter')

    time.sleep(2)



# Where the wizards work

def mainFunc(url):
    meeting_join(url)
    

# if __name__ == "__main__":
#     url = "https://meet.google.com/wwk-ysks-kjg"
#     mainFunc(url)

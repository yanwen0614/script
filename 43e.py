import pyautogui
import uts

locoal_commd = [597, 569]
airport =   [1690+1545-570 ,650+750-555 ]



def drag2airport()
    pyautogui.moveTo(1545,750)
    pyautogui.dragTo(570,555,duration=1.5)
    airport = [1690 ,650]
    x,y = uts.random_cyclic(airport)
    pyautogui.moveTo(x,y)

def clicklocoal_commd()
x,y = uts.random_cyclic(locoal_commd)
pyautogui.moveTo(x,y)
pyautogui.click()
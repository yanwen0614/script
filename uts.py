import pyautogui
import win32gui
import numpy as np
import random
# import matplotlib.pyplot as plt
from math import sin,cos,pi
from numpy.linalg import cholesky
from time import sleep


def click_aim(aim_cenrtel, maxr=40):
    pyautogui.moveTo(*random_cyclic(aim_cenrtel, maxr=maxr))
    pyautogui.click()

def randomclick(local,sg=5):
    x,y = random_coor(local,sg)
    pyautogui.moveTo(x, y, duration=0.25)
    pyautogui.click()
    return x,y

def random_coor(local,sg):
    isout = True
    while isout:
        isout = False
        mu = np.array([[local[0]+local[2]/2,local[1]+local[3]/2]])
        Sigma = np.array([[sg*local[2],0 ],[0, sg*local[3]]])
        R = cholesky(Sigma)
        s = np.dot(np.random.randn(1, 2), R) + mu
        x,y = map(int,s[0])
        #plt.scatter(x,y)
        #plt.show()
        #print(x,y)
        if (x<local[0] or x>local[0]+local[2]):
            isout = True
        elif (y<local[1] or y>local[1]+local[3]):
            isout = True
        if isout:
            print("isout",x,y,"sq")
    return x,y

def random_cyclic(centrel,maxr=100):
    isout = True
    while isout:
        isout = False
        sigma = maxr/3
        r = np.random.normal(0,sigma,1)
        theta = random.random()**pi
        x,y = centrel[0]+r*cos(theta),centrel[1]+r*sin(theta)
        #print(x,y)
        if (r>maxr):
            isout = True
            print("isout",x,y,"cyclic")
    return x,y


def select_campaign(campaign_num):
    if campaign_num<=5:
        local = [360,180,170,120]
        while campaign_num:
            local[1] +=150
            campaign_num-=1
    else:
        campaign_scroll()
        local =[360,225,170,120]
        campaign_num=campaign_num-6
        while campaign_num:
            local[1] +=150
            campaign_num-=1
    randomclick(local)

    
def select_battle(battle_num):
    local = [700,365,800,100]
    if battle_num<5:
        battle_num-=1
        while battle_num:
            local[1]+=175
            battle_num-=1
            sleep(1+abs(random.normalvariate(0,1)))
        randomclick(local)
    else:
        pyautogui.moveTo(random.normalvariate(1200,50), random.normalvariate(900,50), duration=0.25)
        pyautogui.dragRel(0,-800,duration=1)
        battle_num-=5
        local = [700,640,800,100]
        while battle_num:
            local[1]+=175
            battle_num-=1
        sleep(0.5+abs(random.normalvariate(0,1)))
        randomclick(local)


def fairy(aim_cenrtel):
    #pyautogui.moveTo(random_cyclic(aim_cenrtel, maxr=30))
    #pyautogui.click()
    sleep(0.5+random.random()/2)
    local = (1730,580,123,43)
    randomclick(local)
    sleep(0.5+random.random()/2)
    #pyautogui.moveTo(random_cyclic(aim_cenrtel, maxr=30))
    #pyautogui.click()
    sleep(0.5+random.random()/2)


def end_click():
    local = (555,375,109,277)
    randomclick(local)

def select_e():
    local = (1565,250,128,71)
    randomclick(local)

def select_n():
    local = (1725,250,128,71)
    randomclick(local,sg=3)

def campaign_scroll():
    pyautogui.moveTo(440, 950, duration=0.25)
    pyautogui.dragRel(0,-800,duration=1)
    return scrolln

def entry_mission():
    local = (1030,810,190,96)
    randomclick(local)


def addamry(centre):
    click_aim(centre,maxr = 30)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    randomclick([centre[0]+15,centre[1]-35,225,60] ,sg=5)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    checkamry()
    

def start_mission():
    local = (1645,887,215,110)
    randomclick(local,sg=3)



def checkamry(): # 梯队确认
    local = (1637,907,212,72)
    randomclick(local)

def plainTask():
    local = (92,840,190,44)
    randomclick(local,sg=3)

def start_plain():
    local = (1645,900,215,110)
    randomclick(local)

def end_mission():
    local = (1495,887,360,130)
    randomclick(local)

def select_amry(amrynum):
    photo = "amry"+str(amrynum)+".bmp"
    x = pyautogui.locateOnScreen(photo)
    print(x)

def amry_editor():
    local = (300,875,230,55)
    randomclick(local)

def main():
    n = 100
    while n:
        plainTask()
        n -=1
        sleep(1)

def get_color(pos=(1656,923)): #50175  25731  57855

    hdc_screen = win32gui.CreateDC("DISPLAY", "", None)
    return win32gui.GetPixel(hdc_screen,*pos)


def checkinbattle():
    c = get_color(pos=(943,50))
    if c == 48127:
        return True
    else:
        return False

def checkEndPlain():
    c = get_color(pos=(290,880))
    if c == 16777215:
        return True
    else:
        return False

def is_returnbattlemeun():
    photo = "battlemeun.bmp"
    x = pyautogui.locateOnScreen(photo)
    if x:
        return True
    return False

def check_into_amry_editor():
    photo = "return_w.bmp"
    x = pyautogui.locateOnScreen(photo)
    if x:
        return True
    return False

def check_into_echelon_formation():
    photo = "echelon_formation.bmp"
    x = pyautogui.locateOnScreen(photo)
    if x:
        return True
    return False


def repair(stacknum):
    lcl = [300,250,230,600]
    lcl[0]+=(stacknum-1)*263
    randomclick(lcl,sg=4)
    sleep(0.4+abs(random.normalvariate(0.2, 0.1)))
    randomclick([1267,702,220,80],sg=4)


def not_force_replace():
    photo = "not_force_replace.bmp"
    x = pyautogui.locateOnScreen(photo)
    if x:
        return True
    return False

def supply(clickfuntion):
    clickfuntion()
    sleep(0.2+abs(random.normalvariate(0.2, 0.1)))
    clickfuntion()
    sleep(0.4+abs(random.normalvariate(0.2, 0.1)))
    supplybtn = [1610,780,260,80]
    randomclick(supplybtn)

def restart():
    end = [461,47,135,95]
    randomclick(end)
    sleep(0.4+abs(random.normalvariate(0.2, 0.1)))
    restart = [668,688,205,65]
    randomclick(restart)

def army_back(clickfuntion,isselect=False):
    if not isselect:
        clickfuntion()
        sleep(0.2+abs(random.normalvariate(0.2, 0.1)))
    clickfuntion()
    sleep(0.4+abs(random.normalvariate(0.2, 0.1)))
    backbtn = [1377,904,220,80]
    randomclick(backbtn)
    sleep(0.4+abs(random.normalvariate(0.2, 0.1)))
    surebtn = [1021,687,220,80]
    randomclick(surebtn)

def checkisload(): 
    x = get_color(pos=(1656,923))
    if x != 58111:
        return False
    return True

def planend(pos):
    x = uts.get_color(pos)
    if x != 13360495:
        return False
    return True

if __name__ == '__main__':
    get_color()
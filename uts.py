import pyautogui
import win32gui
import numpy as np
import random
# import matplotlib.pyplot as plt
from math import sin,cos,pi
from numpy.linalg import cholesky
from time import sleep
from sys import stdout


def click_aim(aim_cenrtel, maxr=40):
    """随机点击 aim_cenrtel为圆心坐标"""
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


def fairy(aim_cenrtel,isselected=True):
    """对于战斗妖精 点击一次释放 前后已加延时"""
    #pyautogui.moveTo(random_cyclic(aim_cenrtel, maxr=30))
    #pyautogui.click()
    sleep(0.3+random.random()/4)
    local = (1730,580,123,43)
    randomclick(local)
    sleep(0.3+random.random()/4)
    #pyautogui.moveTo(random_cyclic(aim_cenrtel, maxr=30))
    #pyautogui.click()

def End_mission():
    """退出整个战役 """
    start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        end_click()
        sleep(0.42+random.normalvariate(0.3, 0.1))


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
        planTask()
        n -=1
        sleep(1)

def get_color(pos=(1656,923)): #50175  25731  57855
    #hwnd = win32gui.GetDesktopWindow()
    dc = win32gui.GetDC(0)
    c = win32gui.GetPixel(dc,*pos)
    return c

def planTask(max_try=10):
    """ para: max_try default 10"""
    local = (92,840,190,44)
    for i in range(max_try):
        randomclick(local,sg=3)
        sleep(0.2)
        if get_color((261,879)) == 177918 and get_color((281,882)) == 111869:
            break

def checkinbattle():
    c = get_color(pos=(943,50))
    if c == 48127:
        return True
    else:
        return False

def checkEndPlan():
    """ 通过判断计划任务按钮"""
    c1 = get_color(pos=(290,880))  # 计划模式按钮颜色
    c2 = get_color(pos=(155,1015))  # 下方铁血标识颜色
    if c1 == 16777215 and c2==5046512:
        return True
    else:
        return False


def is_returnbattlemeun():
    photo = "battlemeun.bmp"
    x = pyautogui.locateOnScreen(photo)
    if x:
        return True
    return False

def checkload(function,descption : str,basic_delaytime=2):
    """检查载入的函数  
        para： function 判断的函数 载入了为True
               descption 当前判断的描述
               basic_delaytime 基本延迟时间
               """

    print(descption,end="")
    sleep(basic_delaytime)
    while 1:
        sleep(0.5)
        print(".",end="")
        stdout.flush()
        if function():
            break
    print(".")

    

def check_into_amry_editor():
    photo = "return_w.bmp"
    x = pyautogui.locateOnScreen(photo)
    if x:
        return True
    return False

def check_start():
    """检测是否到预备作战画面，即进入战役但未下梯队 """
    photo = "startbattle.bmp"
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

def supply(clickfuntion_or_coor,isselect=False):
    if isinstance(clickfuntion_or_coor,tuple):
        clickfuntion = lambda : click_aim(clickfuntion_or_coor)
    else:
        clickfuntion = clickfuntion_or_coor
    if not isselect:
        clickfuntion()
        sleep(0.2+abs(random.normalvariate(0.2, 0.1)))
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

def army_back(clickfuntion_or_coor,isselect=False):
    """ clickfuntion_or_coor 点击函数或者中心坐标 """
    if isinstance(clickfuntion_or_coor,tuple):
        clickfuntion = lambda : click_aim(clickfuntion_or_coor)
    else:
        clickfuntion = clickfuntion_or_coor
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
    if x != 254205:
        return False
    return True

def PlanEnd(pos):
    """
    通过判断血条位置（通过颜色）
    """
    x = get_color(pos)
    if x != 13360495:
        return False
    return True

def scroll_y(sroll_dy):
    """  传入正 鼠标按住向上"""
    sroll_y = abs(sroll_dy)
    sig = sroll_y/sroll_dy
    loop = (sroll_y/3) if (sroll_y/3)>200 else 200
    loop = loop*sig
    while sroll_y > 0:  
        x = random.normalvariate(1000, 100)
        y = random.normalvariate(400, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(50, 20)
        dy = loop+sig*abs(random.normalvariate(sroll_dy/6, 50))
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= abs(dy)

def scroll_x(sroll_dx):
    """ 鼠标按住向左"""
    sroll_x = abs(sroll_dx)
    sig = sroll_x/sroll_dx
    loop = (sroll_x/3) if (sroll_x/3)>200 else 200
    loop = loop*sig
    while sroll_x > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(300, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dy = random.normalvariate(50, 20)
        dx = loop+sig*abs(random.normalvariate(sroll_dx/6, 50))
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_x -= abs(dx)

def fairy_switch():
    print("fairy_switch")
    switch = [1733,313,117,53]
    randomclick(switch)

def EmeryTurnFunc(sleeptime = 6):
    """敌方回合调用函数，用于处理自动遇敌等问题"""
    def emeryroundend():
        x = get_color(pos=(1525,950))
        if x != 436990:
            return False
        return True
        print("emeary turn")
    sleep(sleeptime)
    while 1:
        if emeryroundend():
            print("Yes")
            break
        if checkinbattle():
            print("in_battle")
            sleep(0.3)
            while checkinbattle():
                sleep(0.3)
            else:
                print("out_battle")
                sleep(2)
                for i in range(4):
                    sleep(0.5)
                    x = random.normalvariate(900, 300)
                    y = random.normalvariate(550, 200)
                    pyautogui.moveTo(x, y, duration=0.25)
                    pyautogui.click()
                    sleep((0.383+abs(random.normalvariate(0.2, 0.1))))
        sleep(0.3)
    sleep(7.5)

if __name__ == '__main__':
    get_color()
import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [1567, 350]
airport =   [1090, 520]


round_aim = [(990,748),(810,630)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry34e():
    uts.select_battle(4)
    sleep(0.5+random.random()/2)
    uts.entry_mission()


def battle():
    entry34e()
    sleep(5+random.random())

    clicklocoal_commd()
    sleep(0.5+random.random()/2)
    uts.checkamry()
    sleep(0.5+random.random()/2)
    clickairport()
    sleep(0.5+random.random()/2)
    uts.checkamry()
    sleep(0.5+random.random()/2)
    uts.start_mission()
    sleep(3+2*random.random())

    uts.checkload(uts.checkisload, "supplying")

    clickairport()
    sleep(0.5+random.random()/2)
    uts.planTask()
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[0])
    sleep(0.5+random.random()/2)


    uts.scroll_y(-600)

    uts.click_aim(round_aim[1],maxr=40)
    sleep(0.5+random.random()/2)


    uts.start_plan()
    print("start_plan")
    uts.checkload(lambda : uts.PlanEnd((921,488)),"判断是否到计划终点",59)
    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(0.42+random.normalvariate(0.3, 0.1))


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        sleep(3+random.normalvariate(3, 1))


def main():
    autobattle(14)

if __name__ == '__main__':
    import sys
    try:
        loop_num =  int(sys.argv[1])
    except :
        
        loop_num = 3
    t = time()
    autobattle(loop_num)
    print(time()-t) 
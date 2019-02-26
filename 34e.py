import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [1567, 350]
airport =   [1090, 520]


round_aim = [(875,540), (990,748), (905,404), (810,630)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry34e():
    uts.select_battle(4)
    sleep(1+random.random())
    uts.entry_mission()


def battle():
    entry34e()
    sleep(5+random.random())

    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    clickairport()
    sleep(1+random.random())
    uts.checkamry()
    uts.start_mission()
    sleep(3+2*random.random())

    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.3)

    clickairport()
    uts.planTask()
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[0])
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[1])
    sleep(0.5+random.random()/2)

    uts.scroll_y(-600)

    uts.click_aim(round_aim[2],maxr=40)
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[3],maxr=50)
    sleep(1+random.random()/2)

    uts.start_plain()
    print("start_plain")
    uts.checkload(lambda : uts.PlanEnd((921,488)),"判断是否到计划终点",59)
    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(1.5+random.normalvariate(5, 2)/5)


def roundgap():
    num = 0
    is_return = False
    while not is_return:
        num+=1
        if num>10:
            uts.start_mission() # end mission
        is_return = uts.is_returnbattlemeun()
        print("ending_screen")
        uts.end_click()
        sleep(0.3)
    sleep(1.5)


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        roundgap()


def main():
    autobattle(4)

if __name__ == '__main__':
    import sys
    try:
        loop_num =  int(sys.argv[1])
    except :
        
        loop_num = 3
    t = time()
    autobattle(loop_num)
    print(time()-t) 
import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [1550, 790]
airport =   [1593, 284]


round_aim = [(1288,255), (1045,333), (755,290), (450,335)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry56():
    uts.select_battle(6)
    sleep(1+random.random())
    uts.entry_mission()


def battle():
    entry56()
    sleep(3+random.random())
    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    uts.scroll_y(800)

    clickairport()
    sleep(0.32+random.random()/3)
    uts.checkamry()
    uts.start_mission()
    sleep(3+2*random.random())

    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.1)

    clickairport()
    uts.planTask()
    sleep(0.34+random.random()/3)
    uts.click_aim(round_aim[0])
    sleep(0.281+abs(random.normalvariate(0.1, 0.07)))
    uts.click_aim(round_aim[1])
    sleep(0.281+abs(random.normalvariate(0.1, 0.07)))

    uts.click_aim(round_aim[2],maxr=30)
    sleep(0.281+abs(random.normalvariate(0.1, 0.07)))
    uts.click_aim(round_aim[3],maxr=60)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))

    uts.start_plain()
    print("start_plain")
    radnum = abs(random.normalvariate(0,1))

    uts.checkload(lambda : uts.PlanEnd((572,192)),"判断是否到计划终点",40)

    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))


    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(1.5+random.normalvariate(5, 2)/5)


def roundgap():
    is_return = False
    while not is_return:
        is_return = uts.is_returnbattlemeun()
        print("ending_screen")
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
    t = time()
    autobattle(10)
    print(time()-t)
import pyautogui
import uts
import random
from time import sleep,time
from sys import stdout
pyautogui.FAILSAFE = True
locoal_commd = [480, 475]

round1 = [(772,503)]
round2 = [(615,738),(833,991),(1210,755)]
round3 = round1+round2+[(920,742)]
round4 = [(922,536),(1151,299),(1400,413),(1371,682),(1218,856)]

round_aim = [(435,545), (610,350), (920,380), (1115,490)]



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry14():
    #uts.select_e()
    uts.select_battle(4)
    sleep(0.63+random.random()/2)
    uts.entry_mission()


def battle():
    entry14()
    uts.checkload(uts.check_start, "check into battle", 4)

    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    sleep(1+random.random())
    uts.start_mission()
    sleep(3+2*random.random())

    uts.checkload(uts.checkisload, "supplying", 2)

    print("round 1")
    clicklocoal_commd()
    sleep(1.431+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round1[0])
    sleep(2.431+abs(random.normalvariate(0.2, 0.1)))
    uts.addamry(locoal_commd)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))

    uts.start_mission() # end mission
    print("emeary turn")
    uts.EmeryTurnFunc(sleeptime=6)

    # round 2
    print("round 2")

    uts.click_aim(round1[0])
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    for aim in round2:
        uts.click_aim(aim,maxr=30)
        sleep(0.431+abs(random.normalvariate(0.2, 0.1)))

    uts.start_plain()
    uts.checkload(lambda : uts.PlanEnd((1291,400)),"判断是否到计划终点",15)
    print("end mission")
    sleep(3)

    uts.start_mission() # end mission
    print("emeary turn")
    uts.EmeryTurnFunc(sleeptime=10)


    print("round 3")
    
    uts.scroll_y(100)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.planTask()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    for aim in round3:
        uts.click_aim(aim,maxr=30)
        sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plain()
    uts.checkload(lambda : uts.PlanEnd((1018,400)),"判断是否到计划终点",45)

    uts.start_mission() # end mission
    print("emeary turn")
    uts.EmeryTurnFunc(sleeptime=10)

    print("round 3")
    sleep(2.431+abs(random.normalvariate(2, 1)))
    uts.planTask()

    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.fairy_switch()
    sleep(1.431+abs(random.normalvariate(0.2, 0.1)))
    for aim in round4:
        uts.click_aim(aim,maxr=30)
        sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plain()
    """
    print("判断是否到计划终点",end="")
    sleep(15)
    while 1:
        sleep(0.5)
        print(".",end="")
        stdout.flush()
        if uts.PlanEnd((1921,568)):
            break
    print(".")
    """
    sleep(60+abs(random.normalvariate(10, 5)))
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.fairy_switch()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.start_mission()

    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(0.5+abs(random.normalvariate(2, 2)/5))


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        


def main():
    for i in range(8):
        num = random.randint(4,5)
        autobattle(num)
        sleep(200+abs(random.normalvariate(50, 20)))
    

if __name__ == '__main__':
    t = time()
    main()
    print(time()-t)
    
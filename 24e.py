import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [480, 785]



round_aim = [(435,545), (610,350), (920,380), (1115,490)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry24():
    #uts.select_e()
    uts.select_battle(4)
    sleep(0.63+random.random()/2)
    uts.entry_mission()


def battle():
    entry24()
    uts.checkload(uts.check_start, "check into battle", 4)

    sroll_y = 250
    while sroll_y > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(600, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(50, 20)
        dy = random.normalvariate(300, 50)
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= dy

    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    sleep(1+random.random())
    uts.start_mission()
    sleep(3+2*random.random())

    uts.checkload(uts.checkisload, "supplying", 2)


    print("round 1")
    clicklocoal_commd()
    uts.planTask()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round_aim[0])
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round_aim[1])
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plain()
    uts.checkload(lambda : uts.PlanEnd((725,208)),"判断是否到计划终点",16)

    uts.start_mission() # end mission
    print("emeary turn")
    uts.EmeryTurnFunc(sleeptime=10)

    # round 2
    print("round 2")
    uts.checkload(lambda : uts.PlanEnd((725,208)),"判断回合开始动画是否加载完",3)
    uts.click_aim(round_aim[1])
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.fairy(round_aim[1])
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round_aim[2],maxr=40)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round_aim[3],maxr=50)
    sleep(0.5+random.random()/3)

    uts.start_plain()
    uts.checkload(lambda : uts.PlanEnd((1197,350)),"判断是否到计划终点",15)
    print("end mission")
    sleep(3)
    uts.End_mission()


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        


def main():
    for i in range(8):
        num = random.randint(5,8)
        autobattle(num)
        sleep(200+abs(random.normalvariate(50, 20)))
    

if __name__ == '__main__':
    t = time()
    main()
    print(time()-t)
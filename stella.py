import random
from datetime import datetime
from sys import stdout
from time import sleep, time

import pyautogui
import win32gui

import uts

pyautogui.FAILSAFE = True

locoal_commd = (1595,800)

airports = (1255,172)
airports1 = (465,172)
go_aim = (1345,672)

def clickairport(airport, maxr=60):
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=maxr))
    pyautogui.click()



def clicklocoal_commd(locoal_commd=locoal_commd, maxr=60):
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=maxr))
    pyautogui.click()

def battle():
    
    sleep(3+2*random.random())


    clicklocoal_commd()
    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))

    clickairport(airports)
    sleep(0.531+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))

    clickairport(airports1,maxr=30)
    sleep(0.531+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))

    uts.start_mission()
    sleep(3.431+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd(maxr=40)

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(go_aim, maxr=40)

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd(maxr=40)

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plan()
    sleep(15+abs(random.normalvariate(5, 2)))

    checkload1("checked plan end")

    sleep(2.583+abs(random.normalvariate(0.1, 0.05)))

    uts.army_back(locoal_commd, isselect=False)
    sleep(0.583+abs(random.normalvariate(0.1, 0.05)))

    uts.restart()  # restart mission

def checkload1(sss="",pos = (1742,657)):
    print(sss)
    while 1:
        first_no = True
        if uts.get_color(pos) == 13360495:
            print("Yes")
            break
        else:
            if first_no:
                print("No",end="")
                first_no = False
            else:
                print(".",end="")
            sleep(random.randint(1,3)+random.random())
        stdout.flush()
    print(".")

def autobattle(num,):
    sleep(2)

    for i in range(num):

        print(i+1,"turn")
        battle()
        sleep(2+random.normalvariate(2, 2)/5)
        #roundgap()

        

if __name__ == '__main__':
    import sys
    loop_num = int(sys.argv[1])
    t = time()
    battler = autobattle(loop_num)

    
    quit2battle = [90,40,170,115]
    uts.randomclick(quit2battle)
    sleep(3+abs(random.normalvariate(0.1,  0.2)))
    uts.randomclick(quit2battle)

    print(time()-t)
    print(datetime.now())
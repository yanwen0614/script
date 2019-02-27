import pyautogui
import uts
import random
from time import sleep,time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [983, 545]
airport = [1625,490]


round1_aim = [(515,858), (530,386), (1174,500), (1168,806),(1720,765),(1710,480)]
round2_aim = [(1535,360),(1540,647), (995,680),(340,732)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=120))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=120))
    pyautogui.click()


def round1end():
    x = uts.get_color(pos=(1155, 417))
    if x != 13360495:
        return False
    return True


def round2end():
    x = uts.get_color(pos=(440, 463))
    if x != 13360495:
        return False
    return True





def battle():

    uts.checkload(uts.check_start, "check start")
    sleep(0.5+abs(random.normalvariate(0.3,  0.1)))
    clicklocoal_commd()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.start_mission()
    sleep(6+random.random()+random.random())
    isload = False
    #uts.supply(clickairport)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    
    isload = False
    print("supplying",end="")
    while not isload:
        isload = uts.checkisload()
        print(".",end="")
        sleep(0.3)
    print(".")
    #uts.army_back(clickairport, isselect=True)
    pyautogui.moveTo(*uts.random_cyclic((1740,555),maxr=20), duration=0.2+random.random()/3)
    pyautogui.dragRel(-1170,390,duration=2.5+random.random()/2)

    print("round 1")


 

    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    for step,aim in enumerate(round1_aim):
        uts.click_aim(aim)
        sleep(0.5+random.random()/2)



    sleep(0.5+random.random()/2)
    uts.start_plain()   

    basic_delay = 90+abs(random.normalvariate(10, 5))
    print("basic_delay",basic_delay)
    sleep(basic_delay)
    print("judge round1end...")
    while 1:
        if round1end() and uts.checkEndPlan():
            print("Yes",end="")
            break
        else:
            print("No",end="")
            sleep(random.randint(1,3)+random.random())
    print()

    uts.start_mission() # end mission

    print("emeary turn")
    sleep(35+abs(random.normalvariate(0, 2)))
    while 1:
        if round1end():
            break
        else:
            sleep(random.randint(1,3)+random.random())
    # round 2
    print("round 2")
    sleep(random.randint(1,3)+random.random()) 
    pyautogui.moveTo(*uts.random_cyclic((765,750),maxr=20), duration=0.2+random.random()/3)
    pyautogui.dragRel(390+185,-185,duration=2.5+random.random()/2)
    
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    for aim in round2_aim:
        sleep(0.5+random.random()/2)
        uts.click_aim(aim)

    uts.start_plain()
    print("start plain")
    basic_delay =15+abs(random.normalvariate(5, 2))

    sleep(basic_delay)

    print("judge round2end...")
    while 1:
        if round2end():
            print("Yes")
            break
        else:
            print("No",end="")
            sleep(random.randint(1,3)+random.random())

    uts.army_back((330,587),isselect=True)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.restart()




def autobattle(num):
    sleep(2)
    for i in range(num):
        print(i+1, "turn")
        battle()
        sleep(3+abs(random.normalvariate(2, 2)/5))

  



if __name__ == '__main__':
    import sys
    
    t = time()
  
    autobattle(10)
    print(time()-t)
    print(datetime.now())
    


"""127.0.0.1		    localhost
204.246.56.80 adr.transit.gf.ppgame.com
218.11.1.163 ios.transit.gf.ppgame.com"""
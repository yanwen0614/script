import pyautogui
import uts
import random
from time import sleep,time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [1560,695 ]
airport = [1630,253]


round1_aim = [(1600,465), (1465,677), (1485,890), (1277,820)]



def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()




def round1end():
    x = uts.get_color(pos=(1405, 320))
    if x != 13360495:
        return False
    return True


def battle():
    
    sleep(0.5+random.random())
    clicklocoal_commd()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()

    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.scroll_y(700)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    #uts.supply(clickairport)
    sleep(1.931+abs(random.normalvariate(0.2, 0.1)))
    
    sleep(1+random.random())
    uts.start_mission()
    sleep(4+random.random()/2)
    #uts.army_back(clickairport, isselect=True)

    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()

    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))
    
    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))
    issroll = 0
    for step,aim in enumerate(round1_aim):
        if step ==2:
            uts.randomclick([1456,858,68,30])
        else:
            uts.click_aim(aim)
        sleep(0.4+random.random()/2)

    uts.start_plain()   
    sleep(6)
    tag = 0
    while 1:
        if round1end():
            sleep(2.5)
            if round1end():
                break
        if uts.checkinbattle():
            uts.randomclick([906,37,146,62])
            sleep(0.2+random.random()/4)
            uts.randomclick([503,39,352,66])
            sleep(9)
            break
        sleep(0.3)
        tag+=1
        if tag > 180:
            x = random.normalvariate(900, 300)
            y = random.normalvariate(550, 200)
            pyautogui.moveTo(x, y, duration=0.25)
            pyautogui.click()
    sleep(1.5+random.random()/2)


    
    print("restart mission")
    uts.restart()  # restart mission



def autobattle(loop_num):
    sleep(2)
    for i in range(loop_num):
        print(i+1, "turn")
        uts.checkload(uts.check_start, "check start")
        battle()
        sleep(2+abs(random.normalvariate(2, 2)/5))



if __name__ == '__main__':
    import sys
    
    loop_num =  int(sys.argv[1])
    
    t = time()
    #entry46()
    autobattle(loop_num)
    print(time()-t)
    print(datetime.now())
    if random.random()>0.0:
        quit2battle = [90,40,170,115]
        uts.randomclick(quit2battle)

"""127.0.0.1		    localhost
204.246.56.80 adr.transit.gf.ppgame.com
218.11.1.163 ios.transit.gf.ppgame.com"""
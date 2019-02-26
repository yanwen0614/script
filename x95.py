import pyautogui
import uts
import random
from time import sleep,time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [287,678 ]
airport = [443,574]


round1_aim = [(581,781), (666,723), (755,663), (925,550)]
round2_aim = round1_aim[::-1][:3]+[(596,618),(525,515)]
round3_aim = [(525,530),(596,624),(666,740),(581,795),(443,587)]



def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=30))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=30))
    pyautogui.click()






def battle():
    if random.random()<0.7:
        uts.scroll_y(-100)
    sleep(0.5+random.random())
    clicklocoal_commd()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()

    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.start_mission()
    sleep(5+random.random()/2)
    #uts.army_back(clickairport, isselect=True)

    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))
    uts.supply(clickairport)
    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.3)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    
    sleep(1+random.random())

    uts.planTask()

    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))
    #clickairport()
    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))
    
    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))

    for aim in round1_aim:
        uts.click_aim(aim,25)
        sleep(0.4+random.random()/2)

    uts.start_plain()   
    sleep(30)
    while 1:
        if uts.checkEndPlan():
            sleep(0.5)
            break
    
    uts.start_mission() # end mission

    uts.EmeryTurnFunc()
    sleep(0.683+abs(random.normalvariate(0.3, 0.1)))
    uts.planTask()

    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))

    for aim in round2_aim:
        uts.click_aim(aim,25)
        sleep(0.4+random.random()/2)

    uts.start_plain()   

    sleep(40)
    while 1:
        if uts.checkEndPlan():
            sleep(0.5)
            break
    
    uts.start_mission() # end mission
    uts.EmeryTurnFunc()
    sleep(0.683+abs(random.normalvariate(0.3, 0.1)))
    uts.planTask()

    sleep(0.483+abs(random.normalvariate(0.2, 0.1)))

    for aim in round3_aim:
        uts.click_aim(aim,25)
        sleep(0.4+random.random()/2)

    uts.start_plain()   
    sleep(8)
    while 1:
        if uts.checkEndPlan():
            sleep(0.5)
            break
    
    uts.army_back(clickairport,isselect=True)
    sleep(0.6+random.random()/2)
    print("restart mission")
    uts.restart()  # restart mission



def autobattle(loop_num):
    sleep(2)
    for i in range(loop_num):
        print(i+1, "turn")
        battle()
        sleep(2+abs(random.normalvariate(2, 2)/5))



if __name__ == '__main__':
    import sys
    try:
        loop_num =  int(sys.argv[1])
    except :
        
        loop_num = 3
    
    t = time()
    #entry46()
    autobattle(loop_num)
    print(time()-t)
    print(datetime.now())
    if random.random()>0.0:
        quit2battle = [95,45,170,100]
        uts.randomclick(quit2battle)
        sleep(2+abs(random.normalvariate(2, 2)/5))
        quit2battle = [90,40,170,115]
        uts.randomclick(quit2battle)

"""127.0.0.1		    localhost
204.246.56.80 adr.transit.gf.ppgame.com
218.11.1.163 ios.transit.gf.ppgame.com"""
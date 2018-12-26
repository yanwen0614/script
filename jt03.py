import pyautogui
import uts
import random
from time import sleep, time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [1282, 812]  #[1315,660,225,60    ]
airport = [443,795]

go_aim = [(1110,625),(945,468)]
back_aim = [(945,538),(1110,695), (1282,882)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry01():
    local = [582,690,410,200]
    uts.randomclick(local)
    sleep(0.63+random.random()/2)
    enrtylocal = (875,795,210,100)
    uts.randomclick(enrtylocal)


def emeryroundend():
    x = uts.get_color(pos=(1525,950))
    if x != 436990:
        return False
    return True

def planend(pos):
    x = uts.get_color(pos)
    if x != 13360495:
        return False
    return True



def battle():
    
    sleep(3+2*random.random())

    clicklocoal_commd()
    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.531+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(1.331+abs(random.normalvariate(0.2, 0.1)))
    uts.start_mission()
    sleep(4.431+abs(random.normalvariate(0.2, 0.1)))
    uts.supply(clicklocoal_commd)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    
    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.3)
    
    sleep(1.431+abs(random.normalvariate(0.2, 0.1)))

    print("round 1")
    uts.plainTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(go_aim[0])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(go_aim[1])
    sleep(0.7+random.random()/2)
    uts.start_plain()
    sleep(55)
    while 1:
        print("check_out_plan")
        if planend((1104, 396)):
            print("yes")
            break
        sleep(1)
    uts.plainTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    for aim in back_aim:
    
        uts.click_aim(aim)
        sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    
    sleep(0.7+random.random()/2)
    uts.start_plain()
    sleep(5+abs(random.normalvariate(0.7, 1)))
    uts.army_back(clicklocoal_commd)
    sleep(0.7+random.random()/2)
    uts.restart()  # restart mission



def autobattle(num,):
    sleep(2)
    entry01()
    for i in range(num):
        print(i+1,"turn")
        battle()
        sleep(2+random.normalvariate(2, 2)/5)
        #roundgap()
        



    

if __name__ == '__main__':
    import sys
    loop_num= 20#int(sys.argv[1])
    t = time()
    autobattle(loop_num)
    print(time()-t)
    print(datetime.now())
    if random.random()>0.4:
        quit2battle = [90,40,170,115]
        uts.randomclick(quit2battle)
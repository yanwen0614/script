import pyautogui
import uts
import random
from time import sleep, time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [1620, 795] #540]  #[1315,660,225,60    ]


round1_aim = [(1234,293), ]
round2_aim = [(880,400),(680,575), (380,430)]



def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry01():
    local = [1270,290,410,200]
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


def mistake(error_coor,correct_coor):
    """ 
    para: error_coor,correct_coor
    """
    if random.random()>random.normalvariate(0.80,0.05):
        print("mistake")
        uts.click_aim(error_coor)
        sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(correct_coor)
        sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(error_coor)



def battle():
    entry01()
    sleep(3+2*random.random())
    sroll_y = 300
    while sroll_y > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(300, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(50, 20)
        dy = abs(random.normalvariate(sroll_y+50, 50))
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= dy
    sleep(1.68+random.random()/2)
    clicklocoal_commd()
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(1.331+abs(random.normalvariate(0.2, 0.1)))
    uts.start_mission()

    #uts.supply(clickairport)
    sleep(1.431+abs(random.normalvariate(0.2, 0.1)))
    
    isload = False
    print("supplying")
    while not isload:
        isload = uts.checkisload()
        sleep(0.5)
    else:
        print("supplied")

    print("round 1")

    sleep(2.431+abs(random.normalvariate(0.2, 0.1)))
    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))


    uts.click_aim(round1_aim[0])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plan()
    sleep(10)

    while 1:
        print("check_out_plan")
        if planend((1350, 150)) :
            print("yes")
            break
        sleep(1)

    sleep(2+random.random()/2)
    uts.addamry(locoal_commd)
    print("supplying")
    while not isload:
        isload = uts.checkisload()
        sleep(0.5)
    else:
        print("supplied")
    sleep(3+random.random()/2)
    uts.start_mission() # end mission

    print("emeary turn")
    sleep(5)
    while 1:
        if emeryroundend():
            print("Yes")
            break
        if uts.checkinbattle():
            sleep(0.3)
            while uts.checkinbattle():
                sleep(0.3)
            else:
                sleep(2)
                for i in range(4):
                    sleep(0.5)
                    x = random.normalvariate(900, 300)
                    y = random.normalvariate(550, 200)
                    pyautogui.moveTo(x, y, duration=0.25)
                    pyautogui.click()
                    sleep((0.383+abs(random.normalvariate(0.2, 0.1))))
        sleep(0.3)
    sleep(3.5)

    print("round 2")
    sleep(2.5)
    isload = False
    print("supplying")
    while not isload:
        isload = uts.checkisload()
        sleep(0.5)
    else:
        print("supplied")

    uts.planTask()
    
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round1_aim[0])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round2_aim[0])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round2_aim[1])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round2_aim[2])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plan()
    sleep(25)

    while 1:
        sleep(1)
        print("check_out_plan")
        if planend((450, 298)) :
            print("yes")
            break
        

    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(0.6+abs(random.normalvariate(2, 2)/5))


def roundgap():
    num = 0
    is_return = uts.is_returnbattlemeun()
    sleep(abs(random.normalvariate(3, 1)))

    while not is_return:
        num+=1
        if num%10==0:
            uts.start_mission() # end mission
        is_return = uts.is_returnbattlemeun()
        print("ending_screen")
        uts.end_click()
        sleep(abs(random.normalvariate(0.5, 0.2)))
    sleep(1.5+abs(random.normalvariate(2, 5)))


def autobattle(num,):
    sleep(2)
    for i in range(num):
        print(i+1,"turn")
        battle()
        sleep(3+random.normalvariate(2, 2)/5)
        roundgap()
        



    

if __name__ == '__main__':
    import sys
    loop_num= 10#int(sys.argv[1])
    t = time()
    autobattle(loop_num)
    print(time()-t)
    print(datetime.now())
    if random.random()>0.4:
        quit2battle = [90,40,170,115]
        uts.randomclick(quit2battle)
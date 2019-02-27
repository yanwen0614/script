import pyautogui
import uts
import random
from time import sleep,time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [341, 451]
airport = [1461,240]

round1_aim = [(431,648),(585,776),(710,883)] 
round1_aim_2 = [904,896]
round2_aim = [(906,650),(841,503),(824,309),(935,242),(1006,358)]

def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()


def roundend(pos):
    x = uts.get_color(pos=pos)
    if x != 13360495:
        return False
    return True

def emeryroundend():
    x = uts.get_color(pos=(1525,950))
    if x != 436990:
        return False
    return True



def battle():
    sleep(5+random.random())

    clicklocoal_commd()
    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))
    # 在左下机场下补给队

    sleep(.631+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.531+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    # 以上为在左上机场下练级队
    sleep(1+random.random())
    uts.start_mission()
    sleep(5+random.random()+random.random())

    uts.supply(clicklocoal_commd)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.3)

    print("round 1")

    """
    if (battle_num ==0 or fairy_state == 0) or (battle_num ==1 or fairy_state == 1):
        fairy_state = (fairy_state+1)%2
        uts.fairy(locoal_commd)
        sleep(0.656+abs(random.normalvariate(0.2, 0.1)))
    """

    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    for aim in round1_aim:
        sleep(0.5+random.random()/2)
        uts.click_aim(aim)
    sleep(0.5+random.random()/2)
    uts.start_plain()   

    basic_delay = 25+random.normalvariate(5, 10)
    print("basic_delay",basic_delay)
    sleep(basic_delay)
    print("judge round1end...")
    while 1:
        if roundend((795,496)):
            print("Yes")
            break
        else:
            print("No")
            sleep(random.randint(1,3)+random.random())

    # 救援人质
    uts.click_aim((841,750),maxr=30)  # 人质位置
    sleep(0.41+abs(random.normalvariate(0.2, 0.1)))
    backbtn = [840-240,750-30,225,60]
    uts.randomclick(backbtn)
    sleep(2.5+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(round1_aim_2)
    sleep(0.5+random.random()/2)
    uts.start_plain()   
    basic_delay = 15+abs(random.normalvariate(5, 10))
    print("basic_delay",basic_delay)
    sleep(basic_delay)
    print("judge round1_2end...")
    while 1:
        if roundend((1016,503)):
            print("Yes")
            break
        else:
            print("No",end="")
            sleep(random.randint(1,3)+random.random())
    sleep(random.randint(1,3)+random.random()) 

    print("emeary turn")
    uts.start_mission() # end mission
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
                    x = random.normalvariate(900, 50)
                    y = random.normalvariate(550, 50)
                    if y<40:
                        y+=40
                    if x<154:
                        x+=154
                    pyautogui.moveTo(x, y, duration=0.25)
                    pyautogui.click()
                    sleep((0.383+abs(random.normalvariate(0.2, 0.1))))
        sleep(0.3)
    sleep(3.5)
    # round 2
    print("round 2")
    sleep(3+random.random()) 
    
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    for aim in round2_aim:
        sleep(0.5+random.random()/2)
        uts.click_aim(aim)
    uts.start_plain()
    
    print("start plain")
    sleep(30)
    while 1:
        if roundend((1156,388)):
            print("Yes")
            break
        else:
            print("No",end="")
            sleep(random.randint(1,3)+random.random())
    sleep(5)
    uts.restart()

if __name__ == '__main__':
    import sys
    loop_num =  int(sys.argv[1])
    sleep(3+abs(random.normalvariate(0.1,  0.2)))
    t = time()
    for i in range(loop_num):
        uts.checkload(uts.check_start, "check start")
        battle()


    sleep(3+abs(random.normalvariate(0.1,  0.2)))
    print(time()-t)
    print(datetime.now())

import pyautogui
import uts
import random
from time import sleep,time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [1005, 540]
airport = [450,525]


round1_aim = [(783,402), (834,818), (1023,532), (816,398)]
round1_error = [(1225,323),(1230,670)]
round2_aim = [(816,398),(1220,395), (1480,450)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()


def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()


def entry02():
    uts.select_battle(2)
    sleep(0.63+random.random()/2)
    uts.entry_mission()


def change_battler(battle_num,  start):
    clicklocoal_commd()
    sleep(1+random.random())
    uts.amry_editor()
    while 1:
        sleep(0.3)
        print("check_into_amry_editor")
        if uts.check_into_amry_editor():
            break
    sleep(0.5+abs(random.normalvariate(0.3,  0.1)))
    army_label = [90, 191, 160, 90]
    if battle_num%2 == 0:
        army_label[1]+=125
        uts.randomclick(army_label)
        sleep(0.5+abs(random.normalvariate(0.3,  0.1)))

    formation_editor =  [1618, 911, 240, 70]
    uts.randomclick(formation_editor)
    sleep(0.8+abs(random.normalvariate(1,  0.2)))

    formation_preset = [1785 , 365,  95,  110]
    uts.randomclick(formation_preset)
    sleep(0.3+abs(random.normalvariate(1,  0.2)))

    pre_formation = [1110, 65, 720, 140]
    if battle_num==1:
        uts.randomclick(pre_formation)
    else:
        pre_formation[1]+=175
        uts.randomclick(pre_formation)
    sleep(0.8+abs(random.normalvariate(1,  0.2)))

    use_preset = [1515, 860, 320, 125]
    uts.randomclick(use_preset)
    if start:
        uts.randomclick([863, 590, 60, 60])
        start = 0
    uts.randomclick(use_preset)
    sleep(0.8+abs(random.normalvariate(1,  0.2)))

    sure = [1605, 855, 225, 140]
    uts.randomclick(sure)
    sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
    while 1:
        sleep(0.5)
        if uts.check_into_amry_editor():
            break


    quit2battle = [90, 40, 170, 115]
    uts.randomclick(quit2battle)
    sleep(3+abs(random.normalvariate(0.1,  0.2)))

    if battle_num ==1:
        clicklocoal_commd()
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        #if warmfulhurted:
        #    uts.repair(5)
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        uts.checkamry()
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        clickairport()
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        uts.checkamry()
    else:
        clickairport()
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        uts.checkamry()
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        clicklocoal_commd()
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        #if warmfulhurted:
        #    uts.repair(5)
        sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
        uts.checkamry()
    return start


def round1end():
    x = uts.get_color(pos=(940, 265))
    if x != 13360495:
        return False
    return True


def round2end():
    x = uts.get_color(pos=(1592, 314))
    if x != 13360495:
        return False
    return True


def mistake(error_coor, correct_coor):
    """ 
    para: error_coor,correct_coor
    """
    if random.random()>random.normalvariate(0.96, 0.05):
        print("mistake")
        uts.click_aim(error_coor)
        sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(correct_coor)
        sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(error_coor)


def battle(start, battle_num,fairy_state,nodelay):
    entry02()
    sleep(5+random.random())

    start = change_battler(battle_num, start)

    sleep(1+random.random())
    uts.start_mission()
    sleep(5+random.random()+random.random())

    uts.supply(clickairport)
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

    uts.plainTask()

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    
    mistake(round1_error[0],round1_aim[0])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    issroll = 0
    for step,aim in enumerate(round1_aim):
        sleep(0.5+random.random()/2)
        if step ==3:
            mistake(round1_error[1],aim)
            sleep(0.5+random.random()/2)
        uts.click_aim(aim)
        sleep(0.5+random.random()/2)
        if step ==0:
            sroll_y = 800
            while sroll_y > 0:  
                x = random.normalvariate(1300, 100)
                y = random.normalvariate(300, 30)
                pyautogui.moveTo(x, y, duration=0.25)
                dx = random.normalvariate(50, 20)
                dy = random.normalvariate(400, 50)
                pyautogui.dragRel(-dx,dy,duration=1+random.random())
                sroll_y -= dy


    sleep(0.5+random.random()/2)
    uts.start_plain()   

    basic_delay = 110+random.normalvariate(5, 10)
    print("basic_delay",basic_delay)
    sleep(basic_delay)
    print("judge round1end...")
    while 1:
        if round1end():
            print("Yes")
            break
        else:
            print("No")
            sleep(random.randint(1,3)+random.random())

    radnum = random.random()
    print("radnum_round1",radnum)
   
    delaytime = 0
    if nodelay:
        radnum = 0
    if radnum >0.999:
        delaytime = 180+abs(random.normalvariate(20, 80))
    elif radnum >0.9848:
        delaytime = 60+abs(random.normalvariate(20, 40))
    elif radnum >0.91354:
        delaytime = 40+abs(random.normalvariate(15, 20))
    elif radnum >0.85:
        delaytime = 20+abs(random.normalvariate(10, 10))
        

    print("sleep ",delaytime)
    sleep(delaytime)

    uts.start_mission() # end mission

    print("emeary turn")
    sleep(15+abs(random.normalvariate(0, 2)))
    while 1:
        if round1end():
            break
        else:
            sleep(random.randint(1,3)+random.random())
    # round 2
    print("round 2")
    sleep(random.randint(1,3)+random.random()) 
    
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.plainTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    for aim in round2_aim:
        sleep(0.5+random.random()/2)
        uts.click_aim(aim)
    uts.start_plain()
    print("start plain")
    basic_delay =60+abs(random.normalvariate(5, 2))
    print("basic_delay",basic_delay)
    sleep(basic_delay)

    print("judge round2end...")
    while 1:
        if round2end():
            print("Yes")
            break
        else:
            print("No")
            sleep(random.randint(1,3)+random.random())

    radnum = random.random()    
    print("radnum_round2",radnum)
   
    delaytime = 0
    if nodelay:
        radnum = 0
    if radnum >0.99:
        delaytime = 180+abs(random.normalvariate(20, 80))
    elif radnum >0.9648:
        delaytime = 60+abs(random.normalvariate(20, 40))
    elif radnum >0.88354:
        delaytime = 40+abs(random.normalvariate(15, 20))
    elif radnum >0.85:
        delaytime = 20+abs(random.normalvariate(10, 10))
    
    print("sleep ", delaytime)
    sleep(delaytime)
    print("end mission")
    uts.start_mission()  # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(0.5+abs(random.normalvariate(2, 2)/5))
    return start, battle_num,fairy_state


def roundgap():
    num = 0
    is_return = uts.is_returnbattlemeun()
    sleep(abs(random.normalvariate(0, 1)))

    while not is_return:
        num+=1
        if num%10==0:
            uts.start_mission() # end mission
        is_return = uts.is_returnbattlemeun()
        print("ending_screen")
        uts.end_click()
        sleep(abs(random.normalvariate(0.5, 0.2)))
    sleep(1.5+abs(random.normalvariate(2, 5)))


def autobattle(num, start, battle_num,fairy_state,nodelay ):
    sleep(2)
    for i in range(num):
        print(i+1, "turn")
        start, battle_num,fairy_state = battle(start, battle_num,fairy_state,nodelay)
        sleep(1+abs(random.normalvariate(2, 2)/5))
        roundgap()
        battle_num += 1
        battle_num = battle_num % 2  
    return battle_num, start


if __name__ == '__main__':
    import sys
    start, battler_num, loop_num = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    print("start,battle_num:", start, battler_num, sep=",") 
    t = time()
    fairy_state,nodelay = 0.0,1
    battler_num, start = autobattle(loop_num, start, battler_num,fairy_state,nodelay)
    print(time()-t)
    print(datetime.now())
    print("start,battle_num:", start, battler_num, sep=",") 
    if random.random()>0.0:
        quit2battle = [90,40,170,115]
        uts.randomclick(quit2battle)

"""127.0.0.1		    localhost
204.246.56.80 adr.transit.gf.ppgame.com
218.11.1.163 ios.transit.gf.ppgame.com"""
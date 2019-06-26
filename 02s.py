import pyautogui
import uts
import random
from time import sleep,time
from datetime import datetime
pyautogui.FAILSAFE = True
locoal_commd = [1372, 787]
airport = [560,770]

aim = [(1097, 602), (2061, 666)]

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
        sleep(0.5)
        print("check_into_amry_editor")
        if uts.check_into_amry_editor():
            break
    sleep(1+abs(random.normalvariate(0.3,  0.1)))
    army_label = [1, 280, 228, 120]
    if battle_num%2 == 0:
        army_label[1]+=180
        uts.randomclick(army_label)
        sleep(0.5+abs(random.normalvariate(0.3,  0.1)))


    formation_editor =  [2265, 1345, 400, 120]
    uts.randomclick(formation_editor)
    sleep(0.3+abs(random.normalvariate(1,  0.2)))

    formation_preset = [2540 , 525,  130,  175]
    uts.randomclick(formation_preset)
    sleep(0.3+abs(random.normalvariate(1,  0.2)))

    pre_formation = [1520, 100, 1090, 220]
    if battle_num==1:
        uts.randomclick(pre_formation)
    else:
        pre_formation[1]+=250
        uts.randomclick(pre_formation)
    sleep(0.4+abs(random.normalvariate(1,  0.2)))

    use_preset = [2120, 1280, 470, 180]
    uts.randomclick(use_preset)
    if start:
        uts.randomclick([1135, 875, 80, 80])
        start = 0
    uts.randomclick(use_preset)
    sleep(0.3+abs(random.normalvariate(1,  0.2)))

    sure = [2255, 1255, 340, 190]
    uts.randomclick(sure)
    sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
    while 1:
        sleep(0.5)
        if uts.check_into_amry_editor():
            break


    quit2battle = [20, 70, 240, 140]
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
    x = uts.get_color(pos=(1180, 402))
    if x != 13426032:
        return False
    return True


def roundend():
    x = uts.get_color(pos=(2173, 483))
    if x != 13492079:
        return False
    return True


def mistake(error_coor, correct_coor):
    """ 
    para: error_coor,correct_coor
    """
    if random.random()>random.normalvariate(0.80, 0.05):
        print("mistake")
        uts.click_aim(error_coor)
        sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(correct_coor)
        sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(error_coor)


def battle(start, battle_num):
    entry02()
    sleep(5+random.random())
    uts.checkload(uts.check_start, "check into battle", 4)
    start = change_battler(battle_num, start)

    sleep(1+random.random())
    uts.start_mission()
    sleep(5+random.random()+random.random())

    uts.supply(clickairport)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.checkload(uts.checkisload, "supplying", 0.5)


    print("round 1")

    # if random.random()>0.35:
    #     if battle_num == 0:
    #         uts.fair(locoal_commd)
    #         sleep(0.456+abs(random.normalvariate(0.2, 0.1)))
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clicklocoal_commd()

    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    uts.planTask()

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.scroll_y(1200)
    sleep(2+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(aim[0])
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(aim[1])

    sleep(1+random.random()/2)
    uts.start_plan()

    basic_delay = 180+random.normalvariate(5, 10)
    print("basic_delay",basic_delay)
    sleep(basic_delay)
    print("judge round end...")
    while 1:
        if roundend():
            print("Yes")
            break
        else:
            print("No")
            sleep(random.randint(1,3)+random.random())

    radnum = random.random()    
    print("radnum_round",radnum)
   
    delaytime = 0
    
    if radnum >0.99:
        delaytime = 60+abs(random.normalvariate(20, 80))
    elif radnum >0.9648:
        delaytime = 30+abs(random.normalvariate(20, 40))
    elif radnum >0.88354:
        delaytime = 15+abs(random.normalvariate(15, 20))
    elif radnum >0.85:
        delaytime = 5+abs(random.normalvariate(10, 10))
    
    print("sleep ", delaytime)
    sleep(delaytime)
    print("end mission")
    uts.start_mission()  # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(0.5+abs(random.normalvariate(2, 2)/5))
    return start, battle_num


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


def autobattle(num, start, battle_num ):
    sleep(2)
    for i in range(num):
        print(i+1, "turn")
        start, battle_num = battle(start, battle_num)
        sleep(1+random.normalvariate(2, 2)/5)
        roundgap()
        battle_num += 1
        battle_num = battle_num % 2
    return battle_num, start


if __name__ == '__main__':
    import sys
    start, battler_num, loop_num = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    print("start,battle_num:", start, battler_num, sep=",") 
    t = time()
    battler_num, start = autobattle(loop_num, start, battler_num)
    print(time()-t)
    print(datetime.now())
    print("start,battle_num:", start, battler_num, sep=",") 
    if random.random()>0.4:
        quit2battle = [90,40,170,115]
        uts.randomclick(quit2battle)
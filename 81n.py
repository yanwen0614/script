import pyautogui
import uts
import random
from time import sleep, time
from datetime import datetime
from sys import stdout
pyautogui.FAILSAFE = True
locoal_commd = [340, 826]  #[1315,660,225,60    ]
locoal_commd_after_scroll = [340,936]
airport = [425,200]

go_aim = [(290,444),(510,768)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=30))
    pyautogui.click()


def clicklocoal_commd(locoal_commd=locoal_commd):
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=30))
    pyautogui.click()

def clicklocoal_commd__(locoal_commd=locoal_commd_after_scroll):
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=30))
    pyautogui.click()



def entry01():
    uts.select_battle(1)
    sleep(0.63+random.random()/2)
    uts.entry_mission()




def change_battler(battle_num):
    '''打手编号，受损高的zas为0 另一个为1'''
    dolllist = [[362,196,207,392],[362+255,196,207,392]]
    if battle_num == 0:
        dolllist = dolllist[::-1]
    clicklocoal_commd()
    sleep(1+random.random())
    uts.amry_editor()
    while 1:
        sleep(0.5)
        print("check_into_amry_editor")
        if uts.check_into_amry_editor():
            break
    sleep(0.5+abs(random.normalvariate(0.3,  0.1)))
    # 进入梯队编辑 补给队

    doll1 = [295,200,227,801-175] # 260
    uts.randomclick(doll1)
    sleep(1+abs(random.normalvariate(0.6,  0.2)))
    # 选择第一个人形

    orderlist = [1633,195,211,127]
    uts.randomclick(orderlist)
    sleep(0.5+abs(random.normalvariate(0.3,  0.1)))
    Damagedorderlist = [1350,815,215,85]
    sleep(1+abs(random.normalvariate(0.6,  0.2)))
    uts.randomclick(Damagedorderlist)
    # 点入受损序列
    sleep(0.431+abs(random.normalvariate(0.2,  0.1)))
    uts.randomclick(dolllist[0])
    #换人
    
    sleep(0.531+abs(random.normalvariate(0.2,  0.1)))
    while 1:
        sleep(0.5)
        print("check_into_amry_editor")
        if uts.check_into_amry_editor():
            break
        stdout.flush()
    # 

    army_label = [90, 191, 160, 90]
    army_label[1]+=125
    uts.randomclick(army_label)
    sleep(0.7+abs(random.normalvariate(0.3,  0.1)))
    #点入打手队

    doll2 = [295+260,200,227,801-175] # 260为相邻人形的水平位移
    uts.randomclick(doll2)
    sleep(1+abs(random.normalvariate(0.6,  0.2)))
    # 选择第二个人形

    uts.randomclick(dolllist[1])
    #换人

    sleep(0.5+abs(random.normalvariate(0.2,  0.1)))
    while 1:
        sleep(0.5)
        print("check_into_amry_editor")
        if uts.check_into_amry_editor():
            break
    stdout.flush()
    quit2battle = [90, 40, 170, 115]
    uts.randomclick(quit2battle)
    sleep(3+abs(random.normalvariate(0.1,  0.2)))



def battle(battle_num):
    
    isload = False
    print("check_start",end="")
    while not isload:
        isload = uts.check_start()
        print(".",end="")
        sleep(0.3)
        stdout.flush()
    print(".")
    stdout.flush()
    
    sleep(3+2*random.random())

    change_battler(battle_num)

    isload = False
    print("check_start_after_change_battler",end="")
    while not isload:
        isload = uts.check_start()
        print(".",end="")
        sleep(0.3)
        stdout.flush()
    print(".")

    clicklocoal_commd()
    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))
    # 在左下机场下补给队

    sroll_y = 180
    while sroll_y > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(300, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(50, 20)
        dy = 180 + abs(random.normalvariate(50, 50))
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= dy
    # 以上为屏幕下拉

    sleep(.631+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    sleep(0.531+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    # 以上为在左上机场下练级队

    sleep(1.331+abs(random.normalvariate(0.2, 0.1)))
    uts.start_mission()
    sleep(5.431+abs(random.normalvariate(0.2, 0.1)))
    isload = False
    print("load..")
    while not isload:
        isload = uts.checkisload()
        print(".",end="")
        sleep(0.3)
        stdout.flush()
    stdout.flush()
    uts.supply(clicklocoal_commd__)
    sleep(0.431+abs(random.normalvariate(0.2, 0.1)))
    
    isload = False
    print("supplying",end="")
    while not isload:
        isload = uts.checkisload()
        print(".",end="")
        sleep(0.3)
        stdout.flush()
    print(".")
    stdout.flush()

    uts.army_back(clicklocoal_commd__,isselect=True)
    sleep(1.431+abs(random.normalvariate(0.2, 0.1)))

    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clickairport()
    for aim in go_aim:
        sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
        uts.click_aim(aim, maxr=30)
    uts.start_plan()
    sleep(65+abs(random.normalvariate(20, 10)))
    while 1:
        first_no = True
        if uts.PlanEnd(pos=(651,519)):
            print("Yes")
            break
        else:
            if first_no:
                print("No",end="")
            else:
                print(".",end="")
        stdout.flush()
        sleep(random.randint(1,3)+random.random())
    print(".")
    uts.restart()  # restart mission



def autobattle(num,battler):
    sleep(2)
    entry01()
    for i in range(num):
        
        print(i+1,"turn")
        battle(battler)
        sleep(2+random.normalvariate(2, 2)/5)
        #roundgap()
        battler +=1 
        battler = battler%2
        print("battler"+"       "+str(battler))
        
    return battler


    

if __name__ == '__main__':
    import sys
    loop_num= int(sys.argv[2])
    battler = int(sys.argv[1])
    t = time()
    battler = autobattle(loop_num,battler)

    
    quit2battle = [90,40,170,115]
    uts.randomclick(quit2battle)
    sleep(3+abs(random.normalvariate(0.1,  0.2)))
    uts.randomclick(quit2battle)

    print(time()-t)
    print(datetime.now())
    print(battler)
import pyautogui
import uts
import random
from time import sleep, time
from datetime import datetime
from sys import stdout
pyautogui.FAILSAFE = True

locoal_commd = (980,555)
locoal_commd__ = (1430,555)

airports = [(1430,555),(1400,255)]

go_aim = (980,255)

end_pos = [(980,649-13),(1294,649-13)]


def clickairport(airport, maxr=60):
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=maxr))
    pyautogui.click()



def clicklocoal_commd(locoal_commd=locoal_commd, maxr=60):
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=maxr))
    pyautogui.click()



def entry115():
    uts.select_battle(5)
    sleep(0.63+random.random()/2)
    uts.entry_mission()



def change_doll(aim_central,ranknum : int, dollnum: int,dollpos: int, intorank:int,):
    """
    ranknum 第几梯队 
    dollnum 人形在梯队的位置 
    dollpos 人形在编辑时的在第一排顺位 
    intorank 进入时位于第几梯队
    """
    dolllist = [[362+255*(dollpos-1),196,207,392]] # [362,196,207,392]
    uts.click_aim(aim_central)
    sleep(1+random.random())
    uts.amry_editor()
    print("check_into_amry_editor",end="")
    while 1:
        sleep(0.5)
        print(".",end="")
        if uts.check_into_amry_editor():
            print(" ")
            break
        
    sleep(0.5+abs(random.normalvariate(0.3,  0.1)))
    if ranknum != intorank:
        army_label = [90, 191+(ranknum-1)*125, 160, 90]
        uts.randomclick(army_label)
        sleep(0.7+abs(random.normalvariate(0.3,  0.1)))
    #点入第三梯队
    # 进入梯队编辑 补给队

    doll1 = [295+260*(dollnum-1),200,227,801-175] # 260
    uts.randomclick(doll1)
    sleep(1+abs(random.normalvariate(0.6,  0.2)))
    # 选择人形
    uts.randomclick(dolllist[0])
    #换人
    
    sleep(0.531+abs(random.normalvariate(0.2,  0.1)))
    while 1:
        sleep(0.5)
        print("check_into_amry_editor")
        if uts.check_into_amry_editor():
            break

    quit2battle = [90, 40, 170, 115]
    uts.randomclick(quit2battle)
    sleep(2)
    if uts.check_into_amry_editor():
        uts.randomclick(quit2battle)
        sleep(2)
    sleep(1+abs(random.normalvariate(0.1,  0.2)))

def change_sop_to_supply(aim_central):
    change_doll(aim_central,3, 1,1, 4)

def change_sop_to_battle(aim_central):
    change_doll(aim_central,4, 2,1, 3)


def battle():
    
    sleep(3+2*random.random())



    clicklocoal_commd()
    sleep(0.631+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(.631+abs(random.normalvariate(0.2, 0.1)))
    # 在左下机场下补给队

    for airport in airports:
        clickairport(airport)
        sleep(0.531+abs(random.normalvariate(0.2, 0.1)))
        uts.checkamry()
        sleep(.631+abs(random.normalvariate(0.2, 0.1)))


    uts.start_mission()
    sleep(5.431+abs(random.normalvariate(0.2, 0.1)))
    isload = False
    while not isload:
        isload = uts.checkisload()
        print("loading")
        sleep(0.3)


    uts.planTask()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    clickairport(airports[1],maxr=40)

    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(go_aim, maxr=40)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))

    clicklocoal_commd()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    
    backbtn = [980-240,555-30,225,60]
    uts.randomclick(backbtn)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.start_plan()
    sleep(65+abs(random.normalvariate(20, 10)))

    checkload("checked plan end")

    sleep(5.583+abs(random.normalvariate(0.1, 0.05)))

    uts.army_back(clicklocoal_commd, isselect=False)
    sleep(0.583+abs(random.normalvariate(0.1, 0.05)))
    checkload("checked amry back")
    sleep(2.583+abs(random.normalvariate(0.1, 0.05)))
    uts.click_aim(locoal_commd)
    sleep(0.183+abs(random.normalvariate(0.1, 0.05)))
    change_sop_to_supply(locoal_commd)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.click_aim(locoal_commd__)
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.checkamry()
    sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
    uts.supply(locoal_commd__)
    sleep(1.583+abs(random.normalvariate(0.2, 0.1)))
    checkload("sop supply",pos = (1194,438))

    uts.army_back(locoal_commd__, isselect=True)
    sleep(0.583+abs(random.normalvariate(0.1, 0.1)))
    checkload("checked amry back",pos = (1194,438))
    sleep(2.583+abs(random.normalvariate(0.1, 0.05)))
    uts.click_aim(locoal_commd__)
    sleep(0.183+abs(random.normalvariate(0.1, 0.05)))
    change_sop_to_battle(locoal_commd__)

    checkload(pos = (1194,438))
    sleep(10+abs(random.normalvariate(5, 4)))
    uts.restart()  # restart mission

def checkload(sss="",pos = (657,437)):
    print(sss)
    while 1:
        first_no = True
        if uts.PlanEnd(pos=pos):
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
        sleep(10+abs(random.normalvariate(5, 4)))
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
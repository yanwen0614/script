import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [1550, 790]
airport =   [1593, 284]


round_aim = [(1288,255), (1045,333), (755,290), (450,335)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry56():
    uts.select_battle(6)
    sleep(1+random.random())
    uts.entry_mission()


def battle():
    entry56()
    sleep(3+random.random())
    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    sroll_y = 800
    while sroll_y > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(150, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(100, 20)
        dy = random.normalvariate(500, 50)
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= dy

    clickairport()
    sleep(1+random.random())
    uts.checkamry()
    uts.start_mission()
    sleep(3+2*random.random())

    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.1)

    clickairport()
    uts.plainTask()
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[0])
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[1])
    sleep(0.5+random.random()/2)

    uts.click_aim(round_aim[2],maxr=30)
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[3],maxr=90)
    sleep(1+random.random()/2)

    uts.start_plain()
    print("start_plain")
    radnum = abs(random.normalvariate(0,1))
    print("radnum",radnum)
    if radnum>3.5:
        sleep(180+abs(random.normalvariate(10, 5)))
    elif radnum>2:
        sleep(150+abs(random.normalvariate(10, 5)))
    elif radnum>1:
        sleep(90+abs(random.normalvariate(10, 5)))
    else:
        sleep(60+abs(random.normalvariate(10, 5)))
    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(1.5+random.normalvariate(5, 2)/5)


def roundgap():
    is_return = False
    while not is_return:
        is_return = uts.is_returnbattlemeun()
        print("ending_screen")
        sleep(0.3)
    sleep(1.5)


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        roundgap()


def main():
    autobattle(4)

if __name__ == '__main__':
    t = time()
    autobattle(8)
    print(time()-t)
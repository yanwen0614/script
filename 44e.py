import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [1215, 545]
airport =   [1360, 490]


round_aim = [(660,485), (145,500), (1460,540), (700,520)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd))
    pyautogui.click()

def entry44e():
    uts.select_e()
    uts.select_battle(4)
    sleep(1+random.random())
    uts.entry_mission()


def battle():
    entry44e()
    sleep(3+random.random())
    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    sroll_y = 2400
    while sroll_y > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(150, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(100, 20)
        dy = random.normalvariate(700, 50)
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= dy

    clickairport()
    sleep(1+random.random())
    uts.checkamry()
    uts.start_mission()
    sleep(5+2*random.random())

    clickairport()
    uts.plainTask()
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[0],maxr=60)
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[1],maxr=60)
    sleep(0.5+random.random()/2)

    sroll_x = 2400
    while sroll_x > 0:  
        x = random.normalvariate(375, 20)
        y = random.normalvariate(555, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(700, 20)
        dy = random.normalvariate(100, 50)
        pyautogui.dragRel(dx,dy,duration=1+random.random())
        sroll_x -= dx

    sleep(1+random.random()/2)
    uts.click_aim(round_aim[2],maxr=50)
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[3],maxr=90)
    sleep(1+random.random()/2)

    uts.start_plain()
    print("start_plain")
    sleep(110+abs(random.normalvariate(10, 5)))
    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.click_aim(round_aim[3],maxr=10)
        sleep(1.5+random.normalvariate(5, 2)/5)


def roundgap():
    sleep(4+random.normalvariate(5, 2))


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        roundgap()


def main():
    autobattle(4)

if __name__ == '__main__':
        main()
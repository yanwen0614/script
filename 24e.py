import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [480, 785]



round_aim = [(435,545), (610,350), (920,380), (1115,490)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport, maxr=50))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd, maxr=50))
    pyautogui.click()

def entry24():
    uts.select_e()
    uts.select_battle(4)
    sleep(0.63+random.random()/2)
    uts.entry_mission()


def battle():
    entry24()
    sleep(5+random.random())



    sroll_y = 250
    while sroll_y > 0:  
        x = random.normalvariate(1300, 100)
        y = random.normalvariate(600, 30)
        pyautogui.moveTo(x, y, duration=0.25)
        dx = random.normalvariate(50, 20)
        dy = random.normalvariate(300, 50)
        pyautogui.dragRel(-dx,dy,duration=1+random.random())
        sroll_y -= dy

    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    sleep(1+random.random())
    uts.start_mission()
    sleep(3+2*random.random())

    isload = False
    while not isload:
        isload = uts.checkisload()
        print("supplying")
        sleep(0.3)

    print("round 1")
    clicklocoal_commd()
    uts.plainTask()
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[0])
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[1])
    sleep(0.5+random.random()/2)
    uts.start_plain()
    sleep(40+abs(random.normalvariate(2, 1)))

    uts.start_mission() # end mission
    print("emeary turn")
    sleep(50+abs(random.normalvariate(2, 1)))
    x = random.normalvariate(1300, 100)
    y = random.normalvariate(600, 30)
    pyautogui.moveTo(x, y, duration=0.25)
    pyautogui.click()
    sleep(10+abs(random.normalvariate(5, 3)))

    # round 2
    print("round 3")

    uts.fairy(round_aim[1])

    uts.plainTask()
    uts.click_aim(round_aim[1])
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[2],maxr=40)
    sleep(0.5+random.random()/2)
    uts.click_aim(round_aim[3],maxr=50)
    sleep(1+random.random()/2)

    uts.start_plain()
    radnum = abs(random.normalvariate(0,1))
    print("radnum",radnum)
    if radnum>3.5:
        sleep(180+abs(random.normalvariate(10, 5)))
    elif radnum>2:
        sleep(70+abs(random.normalvariate(10, 5)))
    elif radnum>1:
        sleep(45+abs(random.normalvariate(10, 5)))
    else:
        sleep(35+abs(random.normalvariate(5, 2)))
    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(1.5+random.normalvariate(5, 2)/5)


def roundgap():
    num = 0
    is_return = False
    while not is_return:
        num+=1
        if num%10==0:
            uts.start_mission() # end mission
        is_return = uts.is_returnbattlemeun()
        print("ending_screen")
        uts.end_click()
        sleep(0.3)
    sleep(1.5)


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        roundgap()


def main():
    for i in range(5):
        num = random.randint(4,8)
        autobattle(num)
        sleep(sleep(300+abs(random.normalvariate(100, 80))))
    

if __name__ == '__main__':
    t = time()
    autobattle(8)
    print(time()-t)
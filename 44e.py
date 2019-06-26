import pyautogui
import uts
import random
from time import sleep,time
pyautogui.FAILSAFE = True
locoal_commd = [1550, 690]
airport =   [1620, 260]


round_aim = [(390,275)] #[(660,485), (145,500), (1460,540), (700,520)]


def clickairport():
    pyautogui.moveTo(*uts.random_cyclic(airport,maxr=25))
    pyautogui.click()



def clicklocoal_commd():
    pyautogui.moveTo(*uts.random_cyclic(locoal_commd,maxr=25))
    pyautogui.click()

def entry44e():
    #uts.select_e()
    uts.select_battle(4)
    sleep(1+random.random())
    uts.entry_mission()


def roundend():
    x = uts.get_color(pos=(439, 137))
    if x != 13360495:
        return False
    return True

def battle():
    entry44e()
    sleep(3+random.random())
    clicklocoal_commd()
    sleep(1+random.random())
    uts.checkamry()

    sroll_y = 1200
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
    sleep(0.5+random.random()/2)
    uts.planTask()
    sleep(0.5+random.random()/2)

    for aim in round_aim:
        uts.click_aim(aim,maxr=25)

    sleep(1+random.random()/2)

    uts.start_plan()
    print("start_plan")
    sleep(100+abs(random.normalvariate(10, 5)))

    print("judge roundend...")
    while 1:
        if roundend():
            print("Yes")
            break
        else:
            print("No",end="")
            sleep(random.randint(1,3)+random.random())
    
        
    print("end mission")
    uts.start_mission() # end mission
    sleep(12+random.normalvariate(3, 1))
    print("end mission  click")
    for i in range(4):
        uts.end_click()
        sleep(0.5+abs(random.normalvariate(2, 2)/5))




def roundgap():
    sleep(4+random.normalvariate(5, 2))


def autobattle(num):
    sleep(5)
    for i in range(num):
        print(i+1,"turn")
        battle()
        roundgap()


def main():
    autobattle(12)

if __name__ == '__main__':
        main()
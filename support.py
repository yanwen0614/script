import pyautogui
import uts
import random
from time import sleep, time
from datetime import datetime
from sys import stdout 

points = [(193,590),(466,603)]
color = 16777215

def check_support_return():
    tag = 1
    for point in points:
        if uts.get_color(point) != color:
            tag = 0
    if tag ==1:
        return True
    else:
        return False

def check_main_frame():
    print("check_net_connect.",end="")
    while uts.get_color((155,69)) != color:
        print(".",end="")
        sleep(0.5)
        stdout.flush()
    print("")
    print("checked!")
        



def reorder_support():
    if check_support_return():
        if random.random()>0.5:
            uts.random_cyclic((1330,505),200) 
        else:
            uts.random_cyclic((1200,511),200) 
        sleep(1.8+abs(random.normalvariate(0.2, 0.1)))
        uts.randomclick([1017,685,220,80])
        sleep(0.583+abs(random.normalvariate(0.2, 0.1)))
        uts.randomclick([1017,685,220,80])  
        return True
    return False

def auto_support(gap_min):
    tag = 1
    while tag:
        sleeptime = gap_min*60+abs(random.normalvariate(gap_min*8,gap_min*5))
        randompara = abs(random.normalvariate(1,0.2))
        sleeptime=randompara*sleeptime
        stdout.write("\r")
        for i in range(4):
            if reorder_support():
                check_main_frame()
        stdout.write("\t".join([str(tag), str(sleeptime),]))
        stdout.flush()
        

        tag+=1
        sleep(sleeptime)

if __name__ == "__main__":
    auto_support(0.8)

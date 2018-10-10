import time

import cozmo

import random


def backpacklights(robot: cozmo.robot.Robot):
    i=random.randrange(1,5,1)
    if i==1:
        robot.set_all_backpack_lights(cozmo.lights.red_light)
        time.sleep(1.5)
    elif i==2:
        robot.set_all_backpack_lights(cozmo.lights.green_light)
        time.sleep(1.5)
    elif i==3:
        robot.set_all_backpack_lights(cozmo.lights.blue_light)
        time.sleep(1.5)
    elif i==4:
        robot.set_all_backpack_lights(cozmo.lights.white_light)
        time.sleep(1.5)
 
counter=0
while counter<5:
    cozmo.run_program(backpacklights)

    

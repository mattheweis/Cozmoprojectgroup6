import time

import cozmo

import random

def backpacklight(robot: cozmo.robot.Robot):
    i=random.randrange(1,5,1)
    if i==1:
        robot.set_all_backpack_lights(cozmo.lights.red_lights)
        time.sleep(1)
    elif i==2:
        robot.set_all_backpack_lights(cozmo.lights.green_lights)
        time.sleep(1)
    elif i==3:
        robot.set_all_backpack_lights(cozmo.lights.blue_lights)
        time.sleep(1)
    elif i==4:
        robot.set_all_backpack_lights(cozmo.lights.white_lights)
        time.sleep(1)

cozmo.run_program(backpacklight)

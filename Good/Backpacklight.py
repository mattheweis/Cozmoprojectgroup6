import time
import cozmo
import random
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def backpacklight(robot: cozmo.robot.Robot):
    # cubecolors(robot)
    while True:
        cubecolors(robot)
        i=random.randrange(1,4,)
        if i==1:
            robot.set_all_backpack_lights(cozmo.lights.red_light)
            time.sleep(1)
        elif i==2:
            robot.set_all_backpack_lights(cozmo.lights.green_light)
            time.sleep(1)
        elif i==3:
            robot.set_all_backpack_lights(cozmo.lights.blue_light)
            time.sleep(1)

def cubecolors(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)  
    cube2 = robot.world.get_light_cube(LightCube2Id)  
    cube3 = robot.world.get_light_cube(LightCube3Id)
    a=[cozmo.lights.red_light,cozmo.lights.green_light,cozmo.lights.blue_light]
    # while True:
    cube1.set_lights(random.choice(a))
    cube2.set_lights(random.choice(a))
    cube3.set_lights(random.choice(a))
    time.sleep(1)

cozmo.run_program(backpacklight)

        

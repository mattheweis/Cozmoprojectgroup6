import time
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import random

def cubecolors(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)  
    cube2 = robot.world.get_light_cube(LightCube2Id)  
    cube3 = robot.world.get_light_cube(LightCube3Id)
    a=[cozmo.lights.red_light,cozmo.lights.green_light,cozmo.lights.blue_light]
    while True:
        cube1.set_lights(random.choice(a))
        cube2.set_lights(random.choice(a))
        cube3.set_lights(random.choice(a))
        time.sleep(1.5)

cozmo.run_program(cubecolors)
    

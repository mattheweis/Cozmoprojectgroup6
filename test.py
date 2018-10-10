import time
import random
import cozmo
#from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id


    
def backpacklight(robot: cozmo.robot.Robot):
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

##def cubelights(robot: cozmo.robot.Robot):
##    cube1 = robot.world.get_light_cube(LightCube1Id)
##    cube2 = robot.world.get_light_cube(LightCube2Id)
##    cube3 = robot.world.get_light_cube(LightCube3Id)
##    i=random.range(1,5,1)
##    


    
counter=0
        
while counter<5:
    cozmo.run_program(backpacklight)

    




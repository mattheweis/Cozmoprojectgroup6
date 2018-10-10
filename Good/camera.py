#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Display Cozmo's camera feed back on his face (like a mirror)
'''

import sys
import time
import imageio
try:
    import numpy as np
except ImportError:
    sys.exit("Cannot import numpy: Do `pip3 install --user numpy` to install")

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import cozmo




def calc_pixel_threshold(image: Image):
    '''Calculate a pixel threshold based on the image.

    Anything brighter than this will be shown on (light blue).
    Anything darker will be shown off (black).
    '''

    # Convert image to gray scale
    grayscale_image = image.convert('L')

    # Calculate the mean (average) value
    mean_value = np.mean(grayscale_image.getdata())
    return mean_value


def cozmo_face_mirror(robot: cozmo.robot.Robot):
    '''Continuously display Cozmo's camera feed back on his face.'''

    robot.camera.image_stream_enabled = True
    

  

    print("Press CTRL-C to quit")

    #while True:
    duration_s = 0.1  # time to display each camera frame on Cozmo's face

    latest_image = robot.world.latest_image
    while(1):
        if latest_image :
            # Scale the camera image down to fit on Cozmo's face
            im = np.array(latest_image.raw_image)
            imageio.imwrite('astronaut-gray.jpg', im[:, :, 0])
            break

    print ('Finish')
        

    time.sleep(duration_s)


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_face_mirror)

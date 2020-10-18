# py3ssc32
A Python3 Version of the pysc32 python3 module.  Communicate with your Lynxmotion SSC32 board with Python3!

# Overview
This implementation is based on the Python 2 implemntation by Vladimir Ermakov.  I've used it for several projects to control the Lynxmotion SSC32 board.  However, it appears the project and source code are no longer being maintained.  See here:
https://pypi.org/project/pyssc32/

Python 3 support has been added with no obvious issues.

# Installation
Clone this repo and run the install within this folder with the command:
```
sudo apt-get install python3-pip
pip3 install .
```

# Usage
Once installed, commands be used to driver the various servo channels.
```
import math
from pyssc32 import ssc32

# Windows Example
ssc = ssc32.SSC32('COM8', 115200, count=32)

# Linux Example
ssc = ssc32.SSC32('/dev/ttyUSB0', 115200, count=32)

ssc[2].position = 2000
ssc[3].name = 'pan'
ssc[4].name = 'tilt'
pan_servo = ssc['pan']
tilt_servo = ssc['tilt']
pan_servo.degrees = 0
tilt_servo.radians = math.pi/4
ssc.commit(time=1000)
ssc.is_done()
False
ssc.is_done()
True
ssc.description = 'My camera's pan/tilt'
ssc.save_config('my_pantilt.cfg')
```

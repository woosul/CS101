from cs1robots import *
import time
import os

current_directory = os.getcwd()
print("Current working directory:", current_directory)

# C:\Share\30 Share\30 PROJECT\120 PYTHON\STUDY\CS101_Python_Programming_Basics\CS101\02\robots
# load_world("C:\\Share\\30 Share\\30 PROJECT\\120 PYTHON\STUDY\\CS101_Python_Programming_Basics\\CS101\\02\\worlds\\amazing2.wld")
load_world("./02/worlds/amazing2.wld")
hubo = Robot(beepers = 10)
hubo.set_trace("blue")
sleep_time = 0.5

def turn_right():
  for i in range(3):
    hubo.turn_left()

#---------------------------------------------------

time.sleep(sleep_time)
hubo.drop_beeper()
time.sleep(sleep_time)
hubo.move()
while not hubo.on_beeper():
  if hubo.front_is_clear():
    time.sleep(sleep_time)
    hubo.move()
  else:
    time.sleep(sleep_time)
    hubo.turn_left()
  

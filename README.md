This is a ROS2 foxy repo for controlling the Robotiq_85 gripper.
Package dependencies include : PickNikRobotics/robotiq_85_gripper (https://github.com/PickNikRobotics/robotiq_85_gripper)

Build the gripper_control package. Source it and then navigate to <workspace>/src/gripper_control/gripper_control to access the gripper_control.py script

To run, open two terminals. In the first one start the robotiq_85_driver by:
$ ros2 launch robotiq_85_driver gripper_driver.launch.py

In the next terminal, run the python script to close, ope max, close and open max/2 gripper positions. 
$ python3 gripper_control.py

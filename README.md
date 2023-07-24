<h2 align="center">Teleoperation of a Humanoid Robot using a Motion-Capture Suit</h1>
<h4 align="center">Selma Dissing</h4>

<br>
<br>

## Content
This repository contains the code utilized in my thesis research, investigating the performance and usability of a motion-capture suit system in comparison to a 2D vision-based system for the teleoperation of humanoid robots, specifically the NAO robot. The code includes data collection, processing, and analysis scripts, along with the visualization tools employed to evaluate the performance of both systems.

## Usage 
Programming language: Python3 (recommended version is 3.7 or above) and Python2.7
<br>
<br>
Download the repo robot_client from https://github.com/SIRCourse/Robot_Cient/tree/main/robot_client
<br>
Run the following command in the environment with Python2.7 as the interpreter (NAOqi only support Python2.7). Change the IP address to the NAO's IP address.
<br>
<br>
$ python robot_client.py --ip=192.168.0.164 
<br>
<br>
Then run both separately
- main.py in python 3.7 (or higher) for acquiring motion-capture data from Axis Neuron 
- robot_joint_control.py in the "RobotJointControl" folder in python 3.7 (or higher) for the NAO robot

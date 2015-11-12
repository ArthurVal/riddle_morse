#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <riddle_pr2> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from riddle_pr2.builder.robots import Mug
from riddle_pr2.builder.robots import Medic
from riddle_pr2.builder.robots import Penholder

#--------------------------------------------------------

#Robots declaration & initial pose
	#PR2
robot_pr2 = BasePR2()
robot_pr2.translate(0.0, 0.0, 0.0)
robot_pr2.rotate(0.0, 0.0, 0.0)

	#Mug
N_MUG = 10
robot_mug_list = []

name = ""
i = 1
while i <= N_MUG:
	name = "robot_mug_" + str(i)
	robot_mug_list.append(Mug(name,False))
	robot_mug_list[i-1].translate(i-1,0,-1)
	robot_mug_list[i-1].rotate(0,0,0)
	i += 1

	#Medic

N_MEDIC = 10
robot_medic_list = []

name = ""
i = 1
while i <= N_MEDIC:
	name = "robot_medic_" + str(i)
	robot_medic_list.append(Medic(name,False))
	robot_medic_list[i-1].translate(i-1,1,-1)
	robot_medic_list[i-1].rotate(0,0,0)
	i += 1

	#penHolder

N_PENHOLDER = 10
robot_penholder_list = []

name = ""
i = 1
while i <= N_PENHOLDER:
	name = "robot_penholder_" + str(i)
	robot_penholder_list.append(Penholder(name,False))
	robot_penholder_list[i-1].translate(i-1,2,-1)
	robot_penholder_list[i-1].rotate(0,0,0)
	i += 1

#--------------------------------------------------------

#Robots Sensors definition
	#PR2
		#Odometry sensor
odometry = Odometry()
odometry.add_interface('ros',topic="/morse_odom_PR2")
robot_pr2.append(odometry)
		#Pose sensor
pose_pr2 = Pose()
pose_pr2.add_interface('ros',topic="/morse_pose_PR2")
robot_pr2.append(pose_pr2)

	#Mug
		#Pose sensor
i = 1
for robot_mug in robot_mug_list:
	topic_name="/morse_pose_mug_" + str(i)
	robot_mug.pose.add_interface('ros',topic=topic_name)
	i += 1

	#Medic
		#Pose sensor
i = 1
for robot_medic in robot_medic_list:
	topic_name="/morse_pose_medic_" + str(i)
	robot_medic.pose.add_interface('ros',topic=topic_name)
	i += 1

	#penHolder
		#Pose sensor
i = 1
for robot_penholder in robot_penholder_list:
	topic_name="/morse_pose_penholder_" + str(i)
	robot_penholder.pose.add_interface('ros',topic=topic_name)
	i += 1
#--------------------------------------------------------

#Robots Actuator definition
	#PR2
		#Motion VW actuator
motion = MotionXYW()
motion.properties(ControlType = 'Position')
motion.add_interface('ros',topic="/morse_motion_PR2")
robot_pr2.append(motion)
		#Keyboard control 
keyboard = Keyboard()
robot_pr2.append(keyboard)

	#Mug
		#Teleport actuator
i = 1
for robot_mug in robot_mug_list:
	topic_name="/morse_TP_mug_" + str(i)
	robot_mug.teleport.add_interface('ros',topic=topic_name)
	i += 1

	#Medic
		#Teleport actuator
i = 1
for robot_medic in robot_medic_list:
	topic_name="/morse_TP_medic_" + str(i)
	robot_medic.teleport.add_interface('ros',topic=topic_name)
	i += 1

	#penHolder
		#Teleport actuator
i = 1
for robot_penholder in robot_penholder_list:
	topic_name="/morse_TP_penholder_" + str(i)
	robot_penholder.teleport.add_interface('ros',topic=topic_name)
	i += 1

#--------------------------------------------------------


# set 'fastmode' to True to switch to wireframe mode
env = Environment('apartment')
env.set_camera_rotation([1.0470, 0, 0.7854])


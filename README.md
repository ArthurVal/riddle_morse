# RIDDLE_Morse

This git repo contains all files created on Morse & Ros for the RIDDLE demonstration on December 2015.

##DESCRIPTION: 

It contains both MORSE configuration files and the ork_ros_morse bridge created between ORK object recognition and Morse.
The main goal of this is to display in real time objects detected by the ORK node within MORSE simulator.

- MORSE: (More details on: https://www.openrobots.org/morse/doc/stable/morse.html)

Morse create the ADREAM environment with the PR2 robot in it.

PR2 robot has: 

	- a pose sensor, which indicate the position of PR2 within Morse (MORSE global coordinates frame); 

		-> Automatically publishing to ROS topic named /morse_pose_PR2

	- an odom sensor, which indicate the position of PR2 relatively to its initial position and also create a frame on TF ;

		-> Automatically publishing to ROS topic named /morse_odom_PR2

	- a motion actuator, that can control PR2 within MORSE ;

		-> Can be used through ROS topic named /morse_motion_PR2 (MSG = geometry_msgs::Twist)
		
Every object that you wish to detect are initially positionned under the ground. There are 10 entities of each object in case of multiple detection of the same object.

Each objects are represented as a 'robot' for Morse.

Every objects have: 

	- a pose sensor, which indicate the position of an object within Morse (MORSE global coordinates frame)

		-> Automatically publishing to ROS topic named /pose_<nameObject>_<numObject> with <numObject> = {1, 2, 3, ... , 9, 10}

	- a teleport actuator, which enable you to teleport an object wherever you want (relatively to the global frame of Morse) ;

		-> Can be used through ROS topic named /morse_TP_<nameObject>_<numObject> with <numObject> = {1, 2, 3, ... , 9, 10} (MSG = geometry_msgs::Pose)

- ORK_ROS_INTERFACE NODE:
This node is a bridge between ORK and MORSE.

It subscribes to both /linemod_recognized_object_array & /tabletop_recognized_object_array topics, listen this topics and autoomatically publishes to the /morse_TP_.. topics.

Each object that has been detected in MORSE automatically disappear according to their timeout timers (can be dynamically change with rqt_reconfigure). 

For each detection of ORK, it compares the current detection (from ORK) to detections already published on MORSE. 

A new object will appear in MORSE if the current detection is not located within a box of 5 cm³ and its angle is different by 10 degrees (for each DOF).

When ORK detects an object, it publishes its ID within the couchDB database. The ORK_ROS_INTEFACE node needs this information to teleport the right object in MORSE. You can modify online the ID of each objects thanks to rqt_reconfigure.


##RUN DEMO:
	
- Inside a terminal, run roscore first:
```
roscore
```
- Then launch the RGBD camera driver (openni or freenect):
```
roslaunch openni_launch openni.launch depth_registration:=true
```
OR
```
roslaunch openni2_launch openni2.launch depth_registration:=true
```
OR
```
roslaunch freenect_launch freenect.launch depth_registration:=true
```
- Don't forget to enable depth registration (use rqt_reconfigure)

- Launch the TF tree of PR2 if you are not working with the robot:
```
roslaunch ork_morse_interface tf_pr2.launch
```
- Launch ORK:
```
roslaunch object_recognition_core detection.launch tabletop:=0 linemod:=1 --screen
```
- Run the interface node: 
```
rosrun ork_morse_interface ork_morse_interface_node
```
- You can run again rqt_reconfigure to see the dynamical reconfiguration of object ID within ORK_MORSE_node reconfi param.

- Run morse:
```
morse run riddle_pr2
```

##ADD NEW OBJECTS:
	
To add new objects, you will need to modify both MORSE files and ORK_ROS_INTERFACE node files.
-> MORSE:
- First, add a new robot to the MORSE file :
```
morse add robot "objectName" riddle_pr2
```
It will automatically create files corresponding to your robot (sensors/actuators of your robots and the mesh file corresponding to its shape).

- Add the teleport actuator to your new robot. Open the file /riddle_pr2/src/riddle_pr2/builder/robots/"objectName".py and add thoses lines under the motion actuator:

*self.teleport = Teleport()*
*self.append(self.teleport)*

- You can change the mesh file that will be used by MORSE to display your robot within the /riddle_pr2/data/riddle_pr2/robots/"objectName".blend file.

- Open the default.py file of you morse project. First add at the top of the file the line: 

*from riddle_pr2.builder.robots import "objectName"*

Then copy what has been done for other objects to the new one (dont forget to change names of variables !)
/!\ Don't forget to change the initial pose of your object /!\

-> ORK_MORSE_INTERFACE:
Open file /riddle_pr2/ork_ros_morse/src/ork_morse_interface/src/main.cpp.

First add your object to the N_OBJECT define const and add #define "objectName" "NUM" under other defines corresponding to the other objects.

Copy each variables associated to the other objects for your object. You will then need to modify:
- void callback_detection function: Add new if()else condition;
- void callback_chgParams function: Add your id param to be able to change it online;
- main function : Create your publisher etc ... and add your object to switch case condition.

Don't forget to change /riddle_pr2/ork_ros_morse/src/ork_morse_interface/cfg/ORKMorse.cfg to add your object ID param.




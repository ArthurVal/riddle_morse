from morse.builder import *

class Mug(GroundRobot):
    """
    A template robot model for mug, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # mug.blend is located in the data/robots directory
        GroundRobot.__init__(self, 'riddle_pr2/robots/mug.blend', name)
        self.properties(classpath = "riddle_pr2.robots.mug.Mug")

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        self.motion = MotionVW()
        self.append(self.motion)

        self.teleport = Teleport()
        self.append(self.teleport)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            keyboard.properties(ControlType = 'Position')
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)


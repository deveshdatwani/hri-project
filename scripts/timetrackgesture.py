#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ModelStates  
from std_msgs.msg import String
from time import time


class Tracker():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.record = False
        rospy.init_node('timer', anonymous=False)
        self.start_time = time() 
        self.end_time = float('inf')
        rospy.Subscriber('/gazebo/model_states', ModelStates, self.callback)
        rospy.spin()        

    def callback(self, data):
        self.x = data.pose[3].position.x
        self.y = data.pose[3].position.y
        
        if (4.5 < self.x < 5.5 and 4.5 < self.y < 5.5 ) and not self.record:
            now = rospy.get_time()
            record = str(now)
            with open('/home/deveshdatwani/hridata/gesturecontroller.txt', 'a') as f:
                f.write(record + "\n")
            self.record = True

if __name__ == "__main__":
    turtlebot3_trakcer = Tracker()


#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from matplotlib import pyplot as plt
from math import cos, sin
from sensor_msg import LaserScan
#from math import deg2rad

def callback(data):
    print("hello")
    theta = data.angle_increment
    data_ranges = data.ranges
    mapp = [(i_val*cos(theta), i_val*sin(theta)) for i_val in data_ranges]
    
    for val in mapp:
        plt.scatter(val)

    plt.show()

    return None


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    rospy.shut

if __name__ == '__main__':
    listener()

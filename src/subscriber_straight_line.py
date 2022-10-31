#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def callback1(data):
    print("Received velocity for rear left motor - ", data.data)

def callback2(data):
    print("Received velocity for rear right motor - ", data.data)
    print("------------------------------------------------------------------------")

def sub():
    rospy.init_node('subscriber_straight_line')
    sub1 = rospy.Subscriber("/mobile_robot/rear_wheel_controller/command", Float64, callback1, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        sub()
    except rospy.ROSInterruptException:
        pass
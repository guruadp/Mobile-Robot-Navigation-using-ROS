#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def callback1(data):
    print("Received velocity for rear left motor - ", data.data)

def callback2(data):
    print("Received velocity for rear right motor - ", data.data)

def callback3(data):
    print("Received position for front left castor - ", data.data)

def callback4(data):
    print("Received position for front right castor - ", data.data)
    print("------------------------------------------------------------------------")

def sub():
    rospy.init_node('subscriber_circle')
    sub1 = rospy.Subscriber("/mobile_robot/rear_wheel_controller/command", Float64, callback1, queue_size=10)
    sub2 = rospy.Subscriber("/mobile_robot/left_steer_controller/command", Float64, callback2, queue_size=10)
    sub3 = rospy.Subscriber("/mobile_robot/rear_wheel_controller/command", Float64, callback3, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        sub()
    except rospy.ROSInterruptException:
        pass
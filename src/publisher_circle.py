#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def pub():
    rospy.init_node('publisher_circle')
    move_forward = rospy.Publisher('/mobile_robot/rear_wheel_controller/command', Float64, queue_size=10)
    steer_left = rospy.Publisher('/mobile_robot/left_steer_controller/command', Float64, queue_size=10)
    steer_right = rospy.Publisher('/mobile_robot/rear_wheel_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(1)
    for i in range(30):
        move_forward.publish(5.0)
        steer_left.publish(5)
        steer_right.publish(5)
        print("Publishing velocity - 5 ; position - 0.3")
        rate.sleep()
    
    move_forward.publish(0.0)
    print("Stopped")

if __name__ == '__main__':
    try:
        pub()
    except rospy.ROSInterruptException:
        pass
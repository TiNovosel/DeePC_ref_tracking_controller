#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry #for subscribing onto meassured values (controller output)
from uav_ros_msgs.msg import AttitudeCommand #for publising commands (controller input)
import time 
import tf
import tf.transformations

def odometry_callback(msg):

    position = msg.pose.pose.position
    orientation = msg.pose.pose.orientation
    (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])

    rospy.loginfo("Received odometry message:")
    rospy.loginfo("Position:(%.2f, %.2f, %.2f)" % (position.x, position.y, position.z))
    rospy.loginfo("Orientation:(%.2f, %.2f, %.2f)" % (roll,pitch,yaw))

def node_start():
    rospy.init_node('odometry_subscriber', anonymous=True)
    rospy.Subscriber('/red/mavros/local_position/odom', Odometry, odometry_callback)
    rospy.spin()



if __name__ == '__main__':
    node_start()


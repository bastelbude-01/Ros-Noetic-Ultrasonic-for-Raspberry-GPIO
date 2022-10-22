#!/usr/bin/env python3

#MarkusMesserschmidt
#22.10.22

import rospy
from std_msgs.msg import Float64
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
trigger = 6
echo = 5


GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)



def distanc():
    GPIO.output(trigger,True)
    time.sleep(0.00001)
    GPIO.output(trigger,False)
    
    Start=time.time()
    Stop=time.time()
    
    while GPIO.input(echo) == 0:
        Start = time.time()
        
    while GPIO.input(echo) == 1:
        Stop = time.time()
        
    einstein = Stop - Start
    distanz = (einstein * 34300)/2
    return distanz



if __name__=='__main__':
    rospy.init_node("ultrasonic")
    rospy.loginfo("Node has been started")
    pub = rospy.Publisher('distanz',Float64,queue_size=10)
    
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        x = distanc()
        rospy.loginfo("Distanz is = %.1f" & x)
        rospy.loginfo(x)
        pub.publish(x)
        rate.sleep()
        
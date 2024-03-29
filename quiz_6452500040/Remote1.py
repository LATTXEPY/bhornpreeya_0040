#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

forward = "forward"
backward = "backward"
turnleft = "turnleft"
turnright = "turnright"

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x300")

rospy.init_node("Remote1")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pubb = rospy.Publisher("std_msgs/String",String, queue_size=10)

def fw():
    print("forward")
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= 0.0
    pub.publish(cmd)
    cmdd = String(forward)
    pubb.publish(cmdd)
        
def bw():
    print("backward")
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z= 0.0
    pub.publish(cmd)
    cmdd = String(backward)
    pubb.publish(cmdd)
       
def lt():
    print("turnleft")
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= AngularVel.get()
    pub.publish(cmd)
    cmdd = String(turnleft)
    pubb.publish(cmdd)
   
def rt():
    print("turnright")
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= -AngularVel.get()
    pub.publish(cmd)
    cmdd = String(turnright)
    pubb.publish(cmdd)
    
LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1) # 1 is defult value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1) # 1 is defult value for scale
AngularVel.pack()

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=180)

frame.mainloop()    
        

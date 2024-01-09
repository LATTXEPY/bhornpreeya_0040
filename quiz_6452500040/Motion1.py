#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_srvs.srv import Empty

data = String()

root = Tk()
root.geometry("300x300")
root.title(" Show Action ")

def clearToTextInput():
    ActOut.delete("1.0","end")
    rs()

def run(val):
    
    ActOut.insert(END, val.data + "\n")

def rs():
    print("Reset")
    rospy.wait_for_service('/reset')  
    try:
        reset_service = rospy.ServiceProxy('/reset', Empty)
        response = reset_service()
        rospy.loginfo("Reset Turtlesim Service Response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == "__main__":
    
    rospy.init_node("Motion1")
    sub = rospy.Subscriber("std_msgs/String",String,callback= run) 
    
    

    ActLabel = Label(text = "Motion1", font = ("",18))
    ActLabel.place(x=113, y=10)
    ActOut = Text(root, height = 7, width = 10, bg = "light cyan", font = ("",16))
    ActOut.place(x=83, y=50)

    ClearBtn=Button(root,height=1,width=10,text="Clear",command=clearToTextInput)
    ClearBtn.place(x=103, y=250)

    mainloop()

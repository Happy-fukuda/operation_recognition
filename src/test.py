#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
# Title: 使用頻度が高いrespeakerの処理をまとめたPythonスクリプト
# Author: fukuda nao
# Date: 2021/02/24
#--------------------------------------------------------------------

import rospy
import time
from visualization_msgs.msg import Marker, MarkerArray


#保存するデータの制限(１回/publish)
max_angle_data=20
#人の1idが認識できない許容回数
error_max=3
class ShakeHandRecognition():
   def __init__(self):
       rospy.init_node("test_openpose",anonymous=False)
       #Subscriber
       rospy.Subscriber('/visualization', MarkerArray, self.shakeRecognision)
       self.flag = False
       self.hand_pos={}
       self.error_cnt=error_max+1
       self.shake_person=int()
       rospy.spin()

   def shakeRecognision(self,receive_msg):
       #0body 1hand 2legs
       '''
            { 0,      "Nose"},    {13,      "LKnee"}
            { 1,      "Neck"},    {14,     "LAnkle"}
            { 2, "RShoulder"},    {15,       "REye"}
            { 3,    "RElbow"},    {16,       "LEye"}
            { 4,    "RWrist"},    {17,       "REar"}
            { 5, "LShoulder"},    {18,       "LEar"}
            { 6,    "LElbow"},    {19,    "LBigToe"}
            { 7,    "LWrist"},    {20,  "LSmallToe"}
            { 8,    "MidHip"},    {21,      "LHeel"}
            { 9,      "RHip"},    {22,    "RBigToe"}
            {10,     "RKnee"},    {23,  "RSmallToe"}
            {11,    "RAnkle"},    {24,      "RHeel"}
            {12,      "LHip"},    {25, "Background"}
        hands_ids = [4, 3, 2, 1, 5, 6, 7]
        '''
       print(receive_msg.markers[1].points)
       print(len(receive_msg.markers[1].points))
    # if(not receive_msg[-1].text):
       #    self.error_cnt=0

       #if(receive_msg[-1].text or self.error_cnt=<error_max):
        #   self.error_cnt+=1
          # if(receive_msg[1][0].points.y>)

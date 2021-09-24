#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
# Title: 使用頻度が高いrespeakerの処理をまとめたPythonスクリプト
# Author: fukuda nao
# Date: 2021/02/24
#--------------------------------------------------------------------

import rospy
import time
from ros_openpose.msg import AltMarker, AltMarkerArray


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
        checkParts=lambda x,ls:x in ls
        if(receive_msg.markers[].text):
           if(all([checkParts(x,receive_msg.markers[1]) for x in [4,3,2])):
               self.hand_pos.setdefault(receive_msg.markers[-1].text,[])

        else:

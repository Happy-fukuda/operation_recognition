#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
# Title: 使用頻度が高いrespeakerの処理をまとめたPythonスクリプト
# Author: fukuda nao
# Date: 2021/02/24
#comment：複数人認識し、対象者が入れ替わりもしくは減少してもros_openposeの仕様上、データは対応idに追加され続ける　
#--------------------------------------------------------------------

import rospy
import time
from ros_openpose.msg import AltMarker, AltMarkerArray


#保存するデータの制限(１回/publish)
max_angle_data=10
#人の1idが認識できない許容回数
error_max=3
#pubの1人あたりのデータ
data_h=3
class ShakeHandRecognition():
    def __init__(self):
        rospy.init_node("rec_openpose",anonymous=False)
        self.pub = rospy.Publisher("/rec_openpose", MarkerArray)
        #Subscriber
        rospy.Subscriber('/visualization', AltMarkerArray, self.shakeRecognision)
        self.flag = False
        #human_pos={}
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
        print([i.text for i in receive_msg.markers])
        data_len=len(receive_msg.markers)-1
        receive_msg=receive_msg.markers
        cnt=1
        hand_up=False
        human_pos={}
        #手を上げているかいないか
        while 0<=data_len:
            hand_up=False
            if(receive_msg[data_len].text):
                #human_ls.append(receive_msg[data_len].text)
                #print(type(receive_msg[data_len-2].body_part[0]))
                if(all([i in receive_msg[data_len-2].body_part for i in [4,2]])):
                    if(receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(4)].y<=receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(2)].y):
                        hand_up=True

                elif(all([i in receive_msg[data_len-2].body_part for i in [5,7]])):
                    if(receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(7)].y<=receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(5)].y):
                        hand_up=True
                human_pos[receive_msg[data_len].text]=hand_up
                data_len-=4
            else:
                data_len-=3

        print(human_pos)

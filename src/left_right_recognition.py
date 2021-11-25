#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
# Title:
# Author: fukuda nao
# Date: 2021/09/24
#comment：複数人認識し、対象者が入れ替わりもしくは減少してもros_openposeの仕様上、データは対応idに追加され続ける　
#そのうち座標から姿勢を推論させる
#--------------------------------------------------------------------

import rospy
import time
from ros_openpose.msg import AltMarker, AltMarkerArray
from std_msgs.msg import String
#from happymimi_recognition_msgs.srv from PositionEstimator
#保存するデータの制限(１回/publish)
max_angle_data=10
#人の1idが認識できない許容回数
error_max=3
#pubの1人あたりのデータ
data_h=3
class ShakeHandRecognition():
    def __init__(self):
        rospy.init_node("left_right_recognition",anonymous=False)
        self.pub = rospy.Publisher("/left_right_recognition", String,queue_size=1)
        #Subscriber
        rospy.Subscriber('/visualization', AltMarkerArray, self.shakeRecognision)
        self.flag = False
        #self.realsence=rospy.ServiceProxy('/detect/depth',PositionEstimator)
        #human_pos={}
        self.body_parts=4+10 #id、上半身、下半身、腕＋指x10
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
        #print([i.body_part for i in receive_msg.markers])
        data_len=len(receive_msg.markers)-1
        receive_msg=receive_msg.markers
        cnt=1
        distance=10
        human_pos=""
        #手を上げているかいないか
        while 0<=data_len:
            direction=""
            if(receive_msg[data_len].text and receive_msg[data_len].pose.position.z<distance):
                distance=receive_msg[data_len].pose.position.z
                #human_ls.append(receive_msg[data_len].text)
                #print(type(receive_msg[data_len-2].body_part[0]))
                #yは下のほうが+
                #print(receive_msg[data_len-2].body_part)
                if(all([i in receive_msg[data_len-2].body_part for i in [4,3,7,6]])):

                    if(receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(4)].y<=receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(7)].y):
                        if (receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(4)].x>=receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(3)].x):
                            human_pos[receive_msg[data_len].text]="left"
                        else:
                            human_pos[receive_msg[data_len].text]="right"

                    else:
                        if (receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(7)].x<=receive_msg[data_len-2].points[receive_msg[data_len-2].body_part.index(6)].x):
                            human_pos[receive_msg[data_len].text]="right"
                        else:
                            human_pos[receive_msg[data_len].text]="left"
                else:
                    human_pos[receive_msg[data_len].text]="False"
                #data_len-=4
                data_len-=self.body_parts
            else:
                #data_len-=3
                data_len-=(self.body_parts-1)


        self.pub.publish("1:"+human_pos)
        rospy.loginfo("1:"+human_pos)
        #self.pub(human_pos)
        #print(human_pos)

if __name__=="__main__":
    ShakeHandRecognition()

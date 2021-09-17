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

class ShakeHandRecognition():
   def __init__(self):
       #Subscriber
       rospy.Subscriber('/visualization', MarkerArray, self.shakeRecognision)
       self.flag = False
       self.hand_pos=[]


   def shakeRecognision(self,receive_msg):
       print(receive_msg)
      

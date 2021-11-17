# operation_recognition

## Overview
openposeから簡単な姿勢推定が必要になったため急遽作ったパッケージ

## Description

### Features this package has(src)

- ### left_right_recognition
> カメラに写った人が手で示す方向を左右で返す
- ### recognition_shake_hand.py 
> 手を上げているか否かを判断する

### 今後
現在は座標から手動で推定しているが機械学習を使って推定を行いたい

#### ビジョン
- 特徴値として使う部位を絞る→学習データや実際に使用するとき特徴値が存在しないと使えない
- 基準となる部位からの相対座標で特徴値とする→座標のが重要ではなく、それぞれの部位の位置関係が重要であり、かつ通常時の座標では値が大きすぎる 

### Technology used
- openpose

## Requirement
ros_openposeとopenposeが必要
環境構築はそれぞれのgithubを参照



## How to build enviroment

```
catkin build
```


## Usag
```
roslaunch ros_openpose run.launch
rosrun operation_recognition [それぞれのノード]
```

## Topic msg
- ### left_right_recognition
std_msgs/String
```
---
#判定に使う部位の認識がない場合False
string data #"人のid:left or right or False" 
```

- ### recognition_shake_hand.py
std_msgs/String
```
---
string data #"人のid:True or False" 
```

## EDITER
- 福田 直央(2019年度参加)

## ros_openpose Citation
@misc{ros_openpose,
    author = {Joshi, Ravi P. and van den Broek, Marike K and Tan, Xiang Zhi and Choi, Andrew and Luo, Rui},
    title = {{ROS OpenPose}},
    year = {2019},
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/ravijo/ros_openpose}}
}

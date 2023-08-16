#This is a test of using code for RPM rather than the usual x/y move coordinate system.
#The movement, at least with the DJI robot, is very inconsistent in regards to movement on the Y axis
#AKA Moving directly left and right. 
#Readerpath here can be changed to whatever is needed to test the movement.
#It is currently set to the path for pixil-frame-0(7).png



import time
import robomaster
from robomaster import robot
from robomaster import chassis
from robomaster import robotic_arm
from robomaster import gripper

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

readerpath=[(0.0, 1), (0.0, 1), (1, 0.0), (1, 0.0), (1, 0.0), (0.0, -1), (0.0, -1), (1, 0.0), (1, 0.0), (0.0, 1), (0.0, 1), (0.0, 1), (0.0, 0.0)]
def robogo(readerpath):
    print("working")
    if __name__ == '__main__':
        ep_robot = robot.Robot()
        ep_robot.initialize(conn_type="ap")

        for coords in readerpath:
            ep_chassis = ep_robot.chassis
            if coords==(1,0):
                ep_chassis.drive_wheels( w1=60 , w2=60 , w3=60 , w4=60 , timeout=None)
                time.sleep(4)
                ep_chassis.drive_wheels( w1=0 , w2=0, w3=0 , w4=0 , timeout=None)
            elif coords==(-1,0):
                ep_chassis.drive_wheels( w1=-60 , w2=-60 , w3=-60 , w4=-60 , timeout=None)
                time.sleep(4)
                ep_chassis.drive_wheels( w1=0 , w2=0, w3=0 , w4=0 , timeout=None)
            elif coords==(0,1):
                ep_chassis.drive_wheels( w1=-150 , w2=150 , w3=-150 , w4=150 , timeout=None)
                time.sleep(2)
                ep_chassis.drive_wheels( w1=0 , w2=0, w3=0 , w4=0 , timeout=None)
            elif coords==(0,-1):
                ep_chassis.drive_wheels( w1=150 , w2=-150 , w3=150 , w4=-150, timeout=None)
                time.sleep(2)
                ep_chassis.drive_wheels( w1=0 , w2=0, w3=0 , w4=0 , timeout=None)
            time.sleep(1)
            #ep_chassis.move(x=coords[0],y=coords[1],z=0,xy_speed=0.5,z_speed=0).wait_for_completed()

        ep_robot.close()
robogo(readerpath)

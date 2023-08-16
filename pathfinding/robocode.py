import time
from attr import NOTHING
import robomaster
from robomaster import robot
from robomaster import chassis
from robomaster import robotic_arm
from robomaster import gripper

def sub_esc_info_handler(esc_info): #organizes the information given
    speed, angle, timestamp, state = esc_info
    print("chassis esc: speed:{0}, angle:{1}, timestamp:{2}, state:{3}".format(speed, angle, timestamp, state))

#readerpath=[(0, 0), (0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (1, 0), (1, 0), (0, 1), (1, 0), (1, 0), (1, 0), (0, 1), (0, 1), (0, 1)]
def robogo(readerpath,readerpath2):
    print(readerpath)
    print("working")
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_chassis = ep_robot.chassis

    ep_chassis.sub_esc(freq=5, callback=sub_esc_info_handler) #gives information about the 4 motors for the wheels
    for coords in readerpath:
        ep_chassis.move(x=coords[0],y=coords[1],z=0,xy_speed=1.2,z_speed=0).wait_for_completed()
        #time.sleep(0)
    ep_arm = ep_robot.robotic_arm
    ep_gripper=ep_robot.gripper
    ep_arm.moveto(x=250, y=-90).wait_for_completed() #moveto is absolute position
    ep_gripper.close(power=90)
    time.sleep(1)
    ep_arm.moveto(x=-300, y=50).wait_for_completed()
    for coords in readerpath2:
        ep_chassis.move(x=coords[0],y=coords[1],z=0,xy_speed=1.2,z_speed=0).wait_for_completed()
    ep_arm.moveto(x=-300, y=50).wait_for_completed()
    ep_arm.moveto(x=250, y=-90).wait_for_completed()
    ep_gripper.open(power=60)
    time.sleep(1)
    ep_arm.moveto(x=-300, y=50).wait_for_completed() 
    ep_chassis.unsub_esc() #ends the information gathering


    ep_robot.close()

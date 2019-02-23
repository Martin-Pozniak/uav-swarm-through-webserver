#=============================slaveX.py===================================================================
# Author: Martin Pozniak
# Desc: This script controls the behavior of the slave drone in flight.
# Creation Date: 12/~/2017
# Latest Functionality: Script is used to takeoff the slave and follow the master's movements
#============================================================================================================= 
from droneBrain import Drone
import time
#import netifaces as ni

ipAddr = "192.168.1.3" # This is set in case you are on windows and the following code can't get the ip dynamically
#============This Can Only Be Done On Linux!!==================
# ni.ifaddresses('wlan0')
# ipAddr = ni.ifaddresses('waln0')[ni.AF_INET][0]['addr']
#==============================================================

#====Set Arg To True For Sitl on Port=====
#====Set To False For Physical Drone======
print("=====================SLAVE 2 : ID 3=======================")
print("==================="+ipAddr+"===================")
drone = Drone(useSitl=False,port="5790",ID='3',ip=ipAddr) #make sure IP specified here matches IP of the device

drone.set_airspeed(1)

print("Adding Drone To Swarm")
drone.add_to_swarm()
print("Printing The Current Nodes In Swarm")
print("===================================")
print("Swarm:", drone.get_swarm_data())
print("===================================")

#===============MISSION====================

#drone.arm_formation()

print("===========WAITING_FOR_MASTER=============")
drone.wait_for_drone_reach_altitude(droneID='1',altitude=2)
print("=========================================")

print("===========TAKING_OFF====================")
drone.arm_and_takeoff(float(drone.get_data_from_server("/dronedata", {'droneID':'1'})['altitude']))
print("=========================================")

print("=======FOLLOWING MASTERS MOVEMENTS=======")
drone.follow_in_formation("triangle")
print("=========================================")

print("===========DRONE_LANDING=================")
drone.land_vehicle()
print("=========================================")

print("===========SHUTTING_DOWN=================")
drone.shutdown()
print("=========================================")

#==========================================
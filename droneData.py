#=============================droneData.py===================================================================
# Author: Martin Pozniak
# Desc: This class is used by server.py to control and keep track of the swarm data.
# Creation Date: 12/~/2017
#============================================================================================================= 
import json
import time

#--------------What the Drone data structure will look like--------------
#-------This is not the actual object used to store active drones--------
# ----a one element list, which contains a dictionary--------------------
#-----whose keys are the Drone ID, and whose value is another dict containing the params------
Drones = [
            {
            "id":'1',
            "ip":"192.168.x.x",
            "latitude":"~",
            "longitude":"~",
            "altitude":"~",
            "armed":"False"
            },
            {
            "id":'2',
            "ip":"192.168.x.x",
            "latitude":'~',
            "longitude":'~',
            "altitude":'~',
            "armed":"False"
            }
        ]
#--------------------^^For Visual Aid Only^^----------------------------

#=============================SWARM CLASS | CONTAINS SWARM OPERATIONS===================================
#=======================================================================================================
class Swarm(object) :   

    #=============================SWARM CONSTRUCTOR=========================================================
    #=======================================================================================================       
    def __init__(self): 
        self.swarm = []

    #=============================MEMBER FUNCTIONS==========================================================
    #======================================================================================================= 
    def addDrone(self,data):
        #This function is used to add a drone to the swarm.
        self.swarm.append(data)
        print("\nAdded a drone with params",data,"\n")
        print("Current Swarm Stats\n----------------------\n",self.swarm,"\n")

    def removeDrone(self,data):
        index = 0
        indxDroneToRemove = self.getIndexOfDroneByID(data["id"])
        self.swarm[indxDroneToRemove] = None
        self.swarm.remove(None)
        print("\nRemoved a drone with params",data,"\n")
        print("Current Swarm Stats\n----------------------\n",self.swarm,"\n")

    def findDroneByID(self,value):
        index=0
        for drone in self.swarm:
            if(drone["id"]==value):
                return drone
            index=index+1
        return None

    def getIndexOfDroneByID(self,value):
        index=0
        for drone in self.swarm:
            # for attribute, value in drone.items():
            #      if(attribute == "id"):
            if(drone["id"]==value):
                return index
            index=index+1
        return None

    def getNumNodesInSwarm(self):
        return self.swarm.count

    def updateDroneInfo(self,data):
        index = 0
        #print("Data received in update: ",data," TYPE: ",type(data))
        #print("UPDATING DRONE #",data["id"])
        indxDroneToUpdate = self.getIndexOfDroneByID(data["id"])
        if self.swarm[indxDroneToUpdate] :
            print("\nSuccessfully Updated Drone: ",self.swarm[indxDroneToUpdate])
            self.swarm[indxDroneToUpdate]=data
            #print("Current Swarm Stats\n----------------------\n", self.getSwarmData(),"\n")
            return self.swarm[indxDroneToUpdate]
        else:
            print("\nDid not find drone by id, no record updated\n")
            return  "NO_DATA"

    def getSwarmData(self):
        return self.swarm

    def getDroneInfo(self,idOfDrone):
        #print("\n\n DRONE PARAMS TO RETURN: ",self.findDroneByID(idOfDrone),"\n\n")
        return self.findDroneByID(idOfDrone)     
#=============================server.py===================================================================
# Author: Martin Pozniak
# Desc: This script controls the server routing and handling of HTTP requests from the drones...
# Creation Date: 12/~/2017
#============================================================================================================= 
from flask import Flask, request, render_template
import json 
from droneData import Swarm
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

#=============================CREATE A SWARM INSTANCE===================================================
#=======================================================================================================
swarm = Swarm()

#=============================HANDLE REQUESTS FOR ADDING DRONE TO SWARM=================================
#=======================================================================================================
@app.route('/adddrone', methods=['GET', 'POST'])
def clientIsAddingDrone():
    if request.method == 'POST':
        print("\n=================ADDING_DRONE=============================")
        swarm.addDrone(request.get_json(force=True))
        print("==============================================================\n")
        return swarm.getDroneInfo(request.get_json(force=True)["id"])
    print("==============================================================\n")
    return "NO_DATA"

#=============================HANDLE REQUESTS FOR REMOVING DRONE FROM SWARM=================================
#===========================================================================================================
@app.route('/removedrone', methods=['POST'])
def clientIsRemovingDrone():
    if request.method == 'POST':
        print("\n=================REMOVING_DRONE=============================")         
        swarm.removeDrone(request.get_json(force=True))
        print("======================PASS=================================\n")
        return swarm.getSwarmData()
    print("======================NO_DATA=================================\n")
    return "NO_DATA"

#=============================HANDLE REQUESTS FOR DRONE DATA============================================
#=======================================================================================================
@app.route('/dronedata', methods=['GET', 'POST'])
def clientRequestedDroneData():
    if request.method == 'POST':
        print("\n=================POST_DRONE_DATA=============================")
        print("Data To Post: ", request.data)
        try:
            drone = swarm.updateDroneInfo(request.get_json(force=True))
            if drone != "NO_DATA":
                print("======================PASS====================================") 
                return drone
        except:
            print("\nError Occured While Attempting To Update Drone Data\nError is likely due to drone no longer in swarm, or error occured in droneData.py > updateDroneData()")
            print("=====================NO_DATA=================================")
            return "NO_DRONE_DATA" 


    if request.method == 'GET':
        print("\n=================GET_DRONE_DATA=============================")
        print("\nGETTING DATA FOR DRONE : ",request.data['droneID'], type(request.data['droneID']))
        droneToReturn = swarm.getDroneInfo(request.data['droneID'])
        if droneToReturn is not None :
            print("==================PASS===================================")
            return swarm.getDroneInfo(request.data['droneID'])

    print("==========================NO_DATA============================")
    return "NO_DRONE_DATA"

#=============================HANDLE REQUESTS FOR SWARM DATA============================================
#=======================================================================================================
@app.route('/swarmdata', methods=['GET'])
def clientRequestedSwarmData():
    if request.method == 'GET':
        print("\n=================GET_SWARM_DATA=============================")
        swarmToReturn = swarm.getSwarmData()
        print("RETURNING: ",swarmToReturn)
        print("=======================PASS===============================")
        if swarmToReturn is not None :
            return swarmToReturn
    print("=======================NO_SWARM_DATA===============================")    
    return "NO_SWARM_DATA"

#=============================PROVIDE A GUI FOR THE SYSTEM============================================================
#=====================================================================================================================
@app.route('/', methods=['GET'])
def clientRequestedGui():
    return render_template("index.html")

#=============================RUN THE SERVER============================================================
#=======================================================================================================
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False)
from device import device 
from dashboard import dashboard
import time
import sys

def main(isGraphicalMode):
    dashb = dashboard()
    dev = device()
    sensorData = []    
    while True:
        response = dev.retrieveStatistics()
        if response == None:
            continue
        (average, max, count, lastSensorData) = response
        sensorData.append(lastSensorData)
        if(isGraphicalMode):
            dashb.updateDashboard(average, max, count, sensorData)
        else:
            print("Average: " + str(average) + " Max: " + str(max) + " Count: " + str(count) + " Last sensor data: " + str(lastSensorData[1]))
        time.sleep(1)

if __name__ == "__main__":
    sys.argv
    if(len(sys.argv) > 1 and sys.argv[1] == "graph"):
        print("graphs")
        time.sleep(1)
        main(True)
    else:
        main(False)
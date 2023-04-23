import random

class sensor:
    def getData(self):
        sensorValue = random.randint(0,1000)
        if sensorValue == 999:
            raise Exception('Sensor not working')
        return sensorValue % 100
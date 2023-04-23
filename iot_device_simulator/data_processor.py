 
class data_processor:
    def __init__(self):
        self.average = 0
        self.count = 0
        self.max = 0

    def processData(self, sensorData):
        self.average = (self.average * self.count + sensorData) / (self.count + 1)
        self.count += 1
        if sensorData > self.max:
            self.max = sensorData
    
    def getAverage(self):
        return self.average
    
    def getMax(self):
        return self.max
    
    def getCount(self):
        return self.count
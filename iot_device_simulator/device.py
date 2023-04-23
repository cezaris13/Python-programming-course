from sensor import sensor
from communication import communication
from data_processor import data_processor

class device:
    def __init__(self):
        self.sensor = sensor()
        self.communication = communication()
        self.data_processor = data_processor()

    def retrieveStatistics(self):
        try:
            sensorData = self.sensor.getData()
            response = self.communication.communicateWithServer(sensorData)
            (_, communication) = response
            self.data_processor.processData(communication)
            return (self.data_processor.getAverage(), self.data_processor.getMax(), self.data_processor.getCount(), response)
        except:
            print ("Error: Sensor not working")
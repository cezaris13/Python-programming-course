import termplotlib as tpl
import os

class dashboard:
    def updateDashboard(self, average, max, count, sensorData):
        lastHundredRecords = sensorData[-100:]
        x = range(0, len(lastHundredRecords))
        y = [element for (_,element) in lastHundredRecords]
        fig = tpl.figure()
        fig.plot(x, y, label="sensor data", width=100, height=30)
        os.system('cls' if os.name == 'nt' else 'clear')
        fig.show()
        print("Maximum: " + str(max))
        print("Average: " + str(round(average,2)))
        print("Total sensor data: " + str(count))
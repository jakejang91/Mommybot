import time
import csv
import pandas as pd

class LogManager():
    def __init__(self):
        self.logs = pd.read_csv("logs.csv")
        print(self.logs.tail())
    
    def getYesterdaySleep(self):
        try:
            return self.logs.tail(1)['t2-01'].values[0]
        except:
            print("NONO YESTERDAY1")
    
    def getLasydaysSleep(self):
        try:
            return self.logs.tail(1)['t2-02'].values[0]
        except:
            print("NONO YESTERDAY2")
    
    def saveLog(self, data):
        try:
            
            with open('logs.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            print('file saved')
        except:
            print('file saving error')
            
print("Module Loaded : log manager")
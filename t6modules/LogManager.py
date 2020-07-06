# This module consists of defined functions to be used in the main code. 

import time
import csv
import pandas as pd

class LogManager():
    def __init__(self): #to open CSV file.
        self.logs = pd.read_csv("logs.csv")
        print(self.logs.tail())
    
    def getYesterdaySleep(self): #to record how many hours user slept last night.
        try:
            return self.logs.tail(1)['t2-01'].values[0]
        except:
            print("NONO YESTERDAY1")
    
    def getLastdaysSleep(self): #to record how many hours on average user slept until today's date.
        try:
            return self.logs.tail(1)['t2-02'].values[0]
        except:
            print("NONO YESTERDAY2")
    
    def saveLog(self, data): # to record & save variables on opened csv file.
        try:
            
            with open('logs.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            print('file saved')
        except:
            print('file saving error')
            
print("Module Loaded : log manager")
import time

class TimeManager():
    
    def __init__(self, starttime):
        self.t = 0
        
        self.sh = starttime
        
    def l2t(self,t):
        try:
            h = time.localtime(t).tm_hour
            m = time.localtime(t).tm_min
            if h*60+m < self.sh:
                return h*60+m + 24*60
            else:
                return h*60+m
        except:
            print("Not a linux time")
            return 0
    
    def hm2t(self, data):
        try:
            h = data[0]
            m = data[1]
            if h*60+m < self.sh:
                return h*60+m + 24*60
            else:
                return h*60+m
        except:
            print("something Wrong")
            return 0
        

    def isStart(self, nowtime = time.time()):
        h = time.localtime(nowtime).tm_hour
        m = time.localtime(nowtime).tm_min
        
        if h*60+m > self.sh :
            return False
        else:
            return True
        
        
print("Module Loaded : time manager")
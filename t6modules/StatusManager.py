class StatusManager():

    def __init(self):
        self.status = []
        
    def reset(self):
        self.status = []
        
    def checkStatus(self):
        if self.status.__len__() < 5:
            return "Not enough"
        else:
            try:
                temp = self.status[0]
                isSame = True
                for i in self.status:
                    if i != temp:
                        isSame = False
                        break
                print(str(temp) + ' in ' + str(self.status))
                if isSame:
                    return temp
                else:
                    return 'NotSame'
            except:
                print('check temp error')
                return 'error'

    def updateLastStatue(self, data):
        print("I got this data : " + str(data))
        if self.status.__len__() == 5:
            self.status.pop(0)
        try:
            if self.status.__len__() < 5:
                self.status.append(data)
        except:
            print("len?")
        
        
        print("now I have this : " + str(self.status))
        
print("Module Loaded : Status Manager")
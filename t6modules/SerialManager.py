import serial

class SerialManager():
    
    def __init__(self):
        self.port = '/dev/ttyUSB0'
        self.isUsed = False
    
    def readSerial(self):
        try:
            with serial.Serial(self.port, 9600) as ser:
                return ser.readline()
        except:
            print("error:Can't read serial")

    def writeSerial(self, sentence = ""):
        try:
            with serial.Serial(self.port, 9600) as ser:
                print("I sent message" + sentence)
                ser.write(bytes(sentence, encoding='ascii'))
                return True
        except:
            print("error:Can't send message on serial")


        
if __name__ == '__main__':
    sm = SerialManager()
    print(sm.readSerial)
    print(sm.writeSerial("hello world!"))
    
print("Module Loaded : serial manager")
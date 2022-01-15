from re import M
import winsound
from mapsound import soundofmusic
from time import sleep

class MakeSound():
    
    def __init__(self,scale = "C8"):

        self.freq = soundofmusic[scale]
        print(scale + ' : ' + str(self.freq))
        print("**************************************************************************")
    
    def getSound(self, duration = 750):
        sleep(0.5)
        winsound.Beep(int(self.freq + 0.5), duration)
        return self.freq
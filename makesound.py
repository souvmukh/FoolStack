from re import M
import winsound
from mapsound import soundofmusic
from time import sleep

class MakeSound():
    
    def __init__(self):
        pass
    
    def oneNote(self,note="C8", duration=750):
        self.freq = soundofmusic[note]
        self.duration = duration
        print(note + ' : ' + str(self.freq))
        print("**************************************************************************")
        return self.getSound()
    
    def getSound(self):
        winsound.Beep(int(self.freq + 0.5), self.duration)
        return self.freq
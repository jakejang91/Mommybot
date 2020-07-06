# This module is to play music.
#Setting alarm
import datetime
import os
import time
import vlc

class MusicPlayer():
    
    def __init__(self, filename):
        try:
            self.p = vlc.MediaPlayer(filename) #to start a music file
        except:
            print("error:initializing")

    def playMusic(self): #to start a music
        try:
            print("MusicPlaying")
            self.p.play()
        except:
            print("playing error")

    def stopMusic(self): # to stop music
        try:
            print("MusicStop")
            self.p.stop()
        except:
            print("Stopping error")
            
            
            
if __name__ == '__main__': # mp3 file put on the same directory
    mp = MusicPlayer("Wishful_Thinking.mp3")
    mp.stopMusic()
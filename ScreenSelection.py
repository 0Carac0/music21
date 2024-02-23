from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.lang import Builder
from os import listdir
from Finale import *
from selmorceau import *

DEBUG = True

kv = Builder.load_file('HudPiano.kv')

class CustPopup(Popup):
    pass

class ScreenSelectionMenu(Screen):

    def callback(instance, n):
        if n == 1:
            ScreenMaster.current = 'JukeBoxPage'
            if DEBUG:
                print(ScreenMaster.current)
        elif n == 2:
            ScreenMaster.current = 'TrainingPage'
            if DEBUG:
                print(ScreenMaster.current)     
        elif n == 3:
            ScreenMaster.current = 'RecordingPage'
            if DEBUG:
                print(ScreenMaster.current)


kv = Builder.load_file('HudPiano.kv')


class JukeBoxMode(Screen):


    pianostop = False
    
    musicList = []
    musdir = r'/home/pi/Desktop/Music21/midi/'
    muslist = listdir(musdir)
    for file in muslist:
        if file.endswith('.mid'):
            musicList.append(file[:-4])

    if DEBUG:
        print(musicList)

    musicList.sort()

    if DEBUG:
        print(musicList)
    
    def playPiano(self):

        dicmusic = {self.musicList.index(self.ids['spin'].text): self.ids['spin'].text}

        if DEBUG:
            print(dicmusic)

        song, fin, instr, seq = infoMorceau(dicmusic[0])

        print(song, fin, instr, seq)
    
    def pianoStop(self):
        
        pianostop = True
        print('oe nan gros flm')
        return pianostop
            
class TrainingMode(Screen):
    pass


class RecordingMode(Screen):
    pass


class ScreenMaster(ScreenManager):
    pass


class HudPianoApp(App):
    def build(self):
        return JukeBoxMode()
#         return ScreenMaster()

if __name__ == '__main__':
    HudPianoApp().run()
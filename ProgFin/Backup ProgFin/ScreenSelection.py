from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from os import listdir
import Finale

DEBUG = True

kv = Builder.load_file('HudPiano.kv')


class ScreenSelectionMenu(Screen):
    
    def callback(instance, n):
        if n == 1:
            ScreenMaster.current = 'JukeBoxPage'
            print(ScreenMaster.current)
        elif n == 2:
            ScreenMaster.current = 'TrainingPage'
            print(ScreenMaster.current)     
        elif n == 3:
            ScreenMaster.current = 'RecordingPage'
            print(ScreenMaster.current)

    
class JukeBoxMode(Screen):
    
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
    
    def showSelection(self):
        if DEBUG:
            print(self.musicList.index(self.ids['spin'].text),self.ids['spin'].text)

        return self.musicList.index(self.ids['spin'].text)



class TrainingMode(Screen):
    pass


class RecordingMode(Screen):
    pass


class ScreenMaster(ScreenManager):
    pass


class HudPianoApp(App):
    def build(self):
        return ScreenMaster()

if __name__ == '__main__': #Autorise le lancement de la musique si celle-ci porte le même nom que celui enregistré dans la variable 'name' 
    HudPianoApp().run()
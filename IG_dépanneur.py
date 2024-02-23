### 01.10.20
### Victor Oppliger
### Ce programme sert à choisir le numèro de la musique qu'on uniquement fait pour dépanner en cas de problème.


from kivy.app import App
from kivymd.app import MDApp
from kivy.app import runTouchApp
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivymd.uix.list import OneLineListItem, ThreeLineIconListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
import sys
from Liste import *
from kivy.uix.scrollview import ScrollView
import subprocess
from kivy.properties import StringProperty
from Pi_MCP23S17 import MCP23S17
from gpiozero import LED

x=0
piano = "Finale_manuel.py"
securite_1 = 0
securite_2 = 0
# led = LED(26)
led = LED(12)
led.on()

class Ecran3(GridLayout):
    def __init__(self, **kwargs):
        super(Ecran3, self).__init__(**kwargs)
        self.cols = 2

        self.choix_musique = TextInput(hint_text="numéro de chanson", multiline=False)

        self.music = Button(text="Play!", width=Window.size[0] * 0.4, size_hint_x=None)
        self.music.bind(on_press=self.play_music)

        self.stop = Button(text="Stop!", width=Window.size[0] * 0.6, size_hint_x=None)
        self.stop.bind(on_press=self.stop_music)
        self.music.add_widget(self.stop)
        

        mid_line = GridLayout(cols=2)
        mid_line.add_widget(self.choix_musique)
        mid_line.add_widget(self.music)
        self.add_widget(mid_line)

    def play_music(self, instance):
        global securite_1
        if self.choix_musique.text!="" and securite_1==0:
            securite_1 = 1
            value = int(self.choix_musique.text)
            print("Play", value)
            self.p = subprocess.Popen(["python3", piano, "%s" % value])



    def stop_music(self, instance):
        global securite_1
        if securite_1 == 1:
            securite_1 = 0
            print("Stop")
            subprocess.call(['kill', str(self.p.pid)])
            SetBoard()
            led.off
            quit()
        
class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.jukebox_page = Ecran3()
        screen = Screen(name="Jukebox_choice")
        screen.add_widget(self.jukebox_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager

def SetBoard():
    # master control program/protocol (?)
    mcp = []
    # ajouter les chip aux chips-maitres
    mcp.append(MCP23S17(ce=0x00, deviceID=0x00)) # chip A (ce =0x00 pour ce=0x01 si on change de chip sur les cartes de 128GPIO)
    mcp.append(MCP23S17(ce=0x00, deviceID=0x01)) # chip B ()
    mcp.append(MCP23S17(ce=0x00, deviceID=0x02)) # chip C
    mcp.append(MCP23S17(ce=0x00, deviceID=0x03)) # chip D
    mcp.append(MCP23S17(ce=0x00, deviceID=0x04)) # chip E
    mcp.append(MCP23S17(ce=0x00, deviceID=0x05)) # chip F
    mcp.append(MCP23S17(ce=0x00, deviceID=0x06)) # chip G
    mcp.append(MCP23S17(ce=0x00, deviceID=0x07)) # chip H

    N = len(mcp)

    for I in range(N):
        mcp[I].open()

    for I in range(N):
        for x in range(16):
            mcp[I].setDirection(x, mcp[I].DIR_OUTPUT)
            mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
    print("RAZ des sorties")
    del mcp
    
if __name__ == '__main__':
    chat_app = MainApp()
    chat_app.run()
# Progamme de VOR il ne fait pas grand chose 29.09.20
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.list import OneLineListItem, ThreeLineIconListItem, IconRightWidget
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.button import Button
from Liste import liste_numero, liste_nom, liste_duree, liste_date, liste_type, liste_image
from kivy.uix.slider import Slider
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout, MDAdaptiveWidget
from Pi_MCP23S17 import MCP23S17
import subprocess

securite_1 = 0
image_number = 0
piano = "Finale_manuel.py"


screen_helper = """
ScreenManager:  
    MenuScreen:
    Jukebox_ChoiceScreen:
    PasswordScreen:
    NoScreen:
    Jukebox_ImageScreen:
<PasswordScreen>:
    name: 'password'
    GridLayout:
        cols:1

        GridLayout:
            cols: 2

            Label:
                text: "Password: "

            TextInput:
                id: passw
                multiline: False

        Button:
            text: "Submit"
            on_release:
                app.root.current = "menu" if passw.text == "0000" else "password"
            

<MenuScreen>:
    name: 'menu'
    MDFillRoundFlatButton:
        text: 'Jukebox'
        font_size: 40
        pos_hint: {'center_x':0.25,'center_y':0.75}
        size_hint: (0.4,0.4)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'jukebox_choice'
    
    MDFillRoundFlatButton:
        text: 'Training'
        font_size: 40
        pos_hint: {'center_x':0.75,'center_y':0.75}
        size_hint: (0.4,0.4)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    
    MDFillRoundFlatButton:
        text: 'Record'
        font_size: 40
        pos_hint: {'center_x':0.25,'center_y':0.25}
        size_hint: (0.4,0.4)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    
    MDFillRoundFlatButton:
        text: 'Coop'
        font_size: 40
        pos_hint: {'center_x':0.75,'center_y':0.25}
        size_hint: (0.4,0.4)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'

<Jukebox_ChoiceScreen>:
    name: 'jukebox_choice' 
    ScrollView:
        MDList:
            id: container
    MDRectangleFlatButton:
        text: "Retour"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = "right" 
            root.manager.current = 'menu'
<NoScreen>
    name: "noscreen"
    MDLabel:
        text: "Il n'y a rien pour le moment."
        halign: 'center'
        font_size: 30
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDRectangleFlatButton:
        text: "Retour"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = "right" 
            root.manager.current = 'menu'
<Jukebox_ImageScreen>
    name: "jukebox_image"
    Image:
        id: container2
    MDRectangleFlatButton:
        text: "Arrêter la musique"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.stop_music()
            root.manager.transition.direction = "right" 
            root.manager.current = 'jukebox_choice'


"""


class PasswordScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class Jukebox_ChoiceScreen(Screen):
    def play_music(self, threelineiconlistitem):
        value = int(threelineiconlistitem.text[3:6])
        print("Play", value)
        global image_number
        image_number = liste_image[value-1]
        self.manager.p = subprocess.Popen(["python3", piano, "%s" % liste_numero[value-1]])
        self.manager.transition.direction = "left"
        self.manager.current = "jukebox_image"


    def on_enter(self):
        global securite_1
        if securite_1 == 0:
            securite_1 = 1
            x = 0
            for i in liste_nom:
                icon = IconLeftWidget(icon="music")
                x = x + 1
                if x<10:
                    espaces = "  "
                elif x<100:
                    espaces = " "
                item = ThreeLineIconListItem(text='No ' + espaces + str(x) + ' - ' + str(i),
                                             secondary_text="Durée : " + str(liste_duree[x - 1]) + " sec",
                                             tertiary_text="Date : " + str(liste_date[x - 1]),
                                             on_release=self.play_music)
                item.add_widget(icon)
                self.ids.container.add_widget(item)
            return self.ids.container

class NoScreen(Screen):
    pass

class Jukebox_ImageScreen(Screen):

    def stop_music(self):
        print("Stop")
        subprocess.call(['kill', str(self.manager.p.pid)])
        SetBoard()

    def on_enter(self):
        global image_number
        ig = Image(source=image_number)
        ig.pos = (self.center_x - ig.center_x, self.center_y - ig.center_y)
        ig.allow_stretch = True
        self.ids.container2.add_widget(ig)
        return self.ids.container2






# Create the screen manager
sm = ScreenManager()
sm.add_widget(PasswordScreen(name='password'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Jukebox_ChoiceScreen(name='jukebox_choice'))
sm.add_widget(NoScreen(name="noscreen"))
sm.add_widget(Jukebox_ImageScreen(name="jukebox_image"))


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Programme VOR"
        self.theme_cls.theme_style = "Dark"  # "Light" "Dark"
        # self.theme_cls.primary_color =
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

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
    MainApp().run()
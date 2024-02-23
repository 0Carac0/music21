# Progamme de VOR 05.11.20 Deuxième version non finalisé mais qui permet de choisir les musiques via une liste.

# toutes les importations (toutes sont nécessaires).
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from Pi_MCP23S17 import MCP23S17
import subprocess
import sqlite3
from kivy.core.window import Window
from gpiozero import LED
from time import sleep


# Création de la taille de l'écran qui prend toute la place (Fullscreen).
Window.size = (700, 400)
Window.fullscreen = False

# Différente variable.
# très important pour que le programme ne soit pas lent et buggé.
securite_1 = 0

# Création de la variable qui allume le boîtier d'alimentation
led = LED(26)
led.on()

# pour savoir quelle image prendre
image_number = 0

# Cette variable évite juste de réecrire "Finale_manuel.py".
piano = "Finale_manuel.py"


# Pour se connecter au fichier .db
connection = sqlite3.connect("Base de données/Liste_des_musiques.db")
cursor = connection.cursor()

liste_musique = cursor.execute("SELECT * FROM Musique_Liste_VOR").fetchall()

# Langage kivy, et écrit comment son fait les écrans.
screen_helper = """
ScreenManager:  
    MenuScreen:
    Jukebox_ChoiceScreen:
    PasswordScreen:
    NoScreen:
    Jukebox_ImageScreen:
    BlindTest1:
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
        text: "quitter"
        font_size: 20
        pos_hint: {'center_x':0.5,'center_y':0.1}
        size_hint: (0.1,0.1)
        on_press: quit()
    MDFillRoundFlatButton:
        text: 'Jukebox'
        font_size: 40
        pos_hint: {'center_x':0.25,'center_y':0.75}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'jukebox_choice'
    
    MDFillRoundFlatButton:
        text: 'Training'
        font_size: 40
        pos_hint: {'center_x':0.75,'center_y':0.75}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    
    MDFillRoundFlatButton:
        text: 'Record'
        font_size: 40
        pos_hint: {'center_x':0.25,'center_y':0.25}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    
    MDFillRoundFlatButton:
        text: 'Blind Test'
        font_size: 40
        pos_hint: {'center_x':0.75,'center_y':0.25}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'blindtest_screen'

<Jukebox_ChoiceScreen>:
    name: 'jukebox_choice' 
    ScrollView:
        MDList:
            id: container
    MDRoundFlatButton:
        text: "Retour"
        pos_hint: {'center_x':0.8,'center_y':0.1}
        size_hint: (0.1,0.1)
        on_press:
            root.manager.transition.direction = "right" 
            root.manager.current = 'menu'
<NoScreen>:
    name: "noscreen"
    MDLabel:
        text: "Il n'y a rien pour le moment."
        halign: 'center'
        font_size: 30
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDRoundFlatButton:
        text: "Retour"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = "right" 
            root.manager.current = 'menu'
<Jukebox_ImageScreen>:
    name: "jukebox_image"
    md_bg_color: 1, 1, 1, 1
    Image:
        id: container2
    MDRoundFlatButton:
        text: "Arrêter la musique"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        size_hint: (0.3,0.1)
        on_press:
            root.stop_music()
            root.manager.transition.direction = "right" 
            root.manager.current = 'jukebox_choice'            
<BlindTest1>:
    name: "blindtest_screen"
    MDFillRoundFlatButton:
        text: "quitter"
        font_size: 20
        pos_hint: {'center_x':0.5,'center_y':0.1}
        size_hint: (0.1,0.1)
        on_press: quit()
    MDFillRoundFlatButton:
        text: 'Start'
        font_size: 20
        pos_hint: {'center_x':0.25,'center_y':0.75}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    MDFillRoundFlatButton:
        text: 'Ça va être tout noir !'
        font_size: 20
        pos_hint: {'center_x':0.75,'center_y':0.75}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    MDFillRoundFlatButton:
        text: 'Est-ce la votre ultime bafouille'
        font_size: 15
        pos_hint: {'center_x':0.25,'center_y':0.25}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    MDFillRoundFlatButton:
        text: 'D- La réponse D'
        font_size: 20
        pos_hint: {'center_x':0.75,'center_y':0.25}
        size_hint: (0.3,0.3)
        on_press:
            root.manager.transition.direction = "left"  
            root.manager.current = 'noscreen'
    

        

"""

# écran avec le mot de passe, non utiliser et finaliser pour le moment.
class PasswordScreen(Screen):
    pass

# Le menu pricipale par lequel on choisit les différents mode, assez inutile pour le moment vu que un seul mode fonctionne.
class MenuScreen(Screen):
    pass

# La page pour le blindtest en cours de préparation
class BlindTest1(Screen):
    pass

# La liste de toute les musiques pour pouvoir les écouter au piano.
class Jukebox_ChoiceScreen(Screen):
    
    # Cette fonction sert à jouer les musiques.
    def play_music(self, threelineiconlistitem):
        value = int(threelineiconlistitem.text[3:6])
        print("Play", value)
        global image_number
        image_number = liste_musique[value-1][6]
        self.manager.p = subprocess.Popen(["python3", piano, "%s" % liste_musique[value-1][1]])
        self.manager.transition.direction = "left"
        self.manager.current = "jukebox_image"

    # Cette fonction lance la liste au début du programme
    def on_enter(self):
        # Cette securité sert à charger la liste qu'une seul et unique
        # fois sinon à chaque musique la liste dois se recharger.
        global securite_1
        if securite_1 == 0:
            securite_1 = 1
            x = 0
            for row in liste_musique:
                icon = IconLeftWidget(icon="music")
                # limite de 999 musique pour le moment
                x = x + 1
                if x<10:
                    espaces = "  "
                elif x<100:
                    espaces = " "
                else:
                    espaces = ""
                item = ThreeLineIconListItem(text='No ' + espaces + str(x) + ' - ' + str(row[2]),
                                             secondary_text="Durée : " + str(row[3]) + " sec",
                                             tertiary_text="Date : " + str(row[4]),
                                             on_release=self.play_music)
                
                item.add_widget(icon)
                self.ids.container.add_widget(item)
            return self.ids.container

# écran qui sert à informer qu'il n'y a rien pour le moment.
class NoScreen(Screen):
    pass

# l'écran où il y aura l'image de l'album de la musique en question. Aussi pour arrêter la musique.
class Jukebox_ImageScreen(Screen):
    
    # Cette fonction sert à arrêter les musiques et à reset les touches.
    def stop_music(self):
        print("Stop")
        subprocess.call(['kill', str(self.manager.p.pid)])
        SetBoard()

    # Cette fonction crée l'écran avec l'image de la musique en question.
    def on_enter(self):
        global image_number
        global text_number
        ig = Image(source=image_number, size=(400, 400))
        ig.pos = (self.center_x - ig.center_x, self.center_y - ig.center_y)
        self.ids.container2.add_widget(ig)
        return self.ids.container2


# Création du manager d'écrans qui permet de faire les lien entre le langage python et kivy
# et de changer d'écrans.

sm = ScreenManager()
sm.add_widget(PasswordScreen(name='password'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Jukebox_ChoiceScreen(name='jukebox_choice'))
sm.add_widget(NoScreen(name="noscreen"))
sm.add_widget(Jukebox_ImageScreen(name="jukebox_image"))
sm.add_widget(BlindTest1(name="blindtest"))

# Class fondamentale qui crée la fenêtre.
class MainApp(MDApp):
    
    # Fonction qui initialise le programme.
    def __init__(self, **kwargs):
        self.title = "Programme VOR"
        self.theme_cls.theme_style = "Dark"  # "Light" "Dark"
        # self.theme_cls.primary_color =
        super().__init__(**kwargs)
    
    # Fonction qui construit les écrans.
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    
# Vraiment je dois expliquer cette foncion ?
def Exit():
    led.off()
    sleep(1)
    quit()
    
# Cette fonction sert à mettre les sorties de la raspberry pi à 0 sinon les touches de piano reste enfoncé et les
# électroaimants brule.
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
    # très important de del mcp pour qu'on puisse jouer de muique encore après.
    del mcp

# Le run du programme
if __name__ == '__main__':
    MainApp().run()

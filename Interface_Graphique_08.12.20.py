# Programme de VOR 10.12.20 Quatrième version.
# permet de choisir les musiques via une liste et d'avoir un blindtest.

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
from kivy.clock import Clock
import random
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
# Importe également 'Finale_manuel.py' (cf lignes 47 et 386)


# Création de la taille de l'écran qui prend toute la place (Fullscreen)  EDIT : full screen désactivé par souci de praticité. Pour réactiver ; supprimer le '#' au début de la 25ème ligne.
Window.size = (1280, 720)
# Window.fullscreen = True  # Normalement active. Désactivée pour tests.

# Différente variable.
# très important pour que le programme ne soit pas lent et buggé.
securite_1 = 0

# pour qu'une foisle blindtest lancé on ne revienne plus dessus une fois quitter.
securite_2 = 0

# Création de la variable qui allume le boîtier d'alimentation
# led = LED(26)
led = LED(12)
led.on()

# pour savoir quelle image prendre
image_number = 0

# Compteur de points pour le blindtest
compteur_points = 0

# Cette variable évite juste de réecrire "Finale_manuel.py".
piano = "Finale_manuel.py"

# Pour se connecter au fichier .db
connection = sqlite3.connect("Base de données/Liste_des_musiques.db")
cursor = connection.cursor()

# crée la liste musique
liste_musique = cursor.execute("SELECT * FROM Musique_Liste_VOR").fetchall()

# crée la liste blindtest
liste_blindtest = cursor.execute("SELECT * FROM Musique_Liste_VOR WHERE BlindTest = '1'").fetchall()

# pour remettre à zéro si une musique à déjà été jouer pas nécessaire juste pour être sûr.
cursor.execute("UPDATE Musique_Liste_VOR SET DejaJouer = '0'")
connection.commit()

# Langage kivy, et écrit comment son fait les écrans.
screen_helper = """
ScreenManager:  
    MenuScreen:
    Jukebox_ChoiceScreen:
    PasswordScreen:
    NoScreen:
    Jukebox_ImageScreen:
    BlindtestScreen:
    Blindtest_ImageScreen:
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
        on_press: root.Exit()
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
            root.manager.transition.direction = "up"  
            root.manager.current = 'blindtest'

<Jukebox_ChoiceScreen>:
    name: 'jukebox_choice' 
    ScrollView:
        MDList:
            id: container
    MDFillRoundFlatButton:
        text: "Random"
        font_size: 20
        pos_hint: {'center_x':0.8,'center_y':0.8}
        size_hint: (0.15,0.15)
        on_press:
            root.random()
    MDFillRoundFlatButton:
        text: "Retour"
        font_size: 20
        pos_hint: {'center_x':0.8,'center_y':0.2}
        size_hint: (0.15,0.15)
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
        text_color: 0, 0, 0, 1
    MDRoundFlatButton:
        text: "Retour"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = "right" 
            root.manager.current = 'menu'
<Jukebox_ImageScreen>:
    name: "jukebox_image"
    BoxLayout:
        id: container2
    BoxLayout:
        pos_hint: {'center_x':0.5,'center_y':0.9}
        id: container5
    MDRoundFlatButton:
        text: "Arrêter la musique"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        size_hint: (0.3,0.1)
        on_press:
            root.stop_music()
            root.manager.transition.direction = "right" 
            root.manager.current = 'jukebox_choice'            
<BlindtestScreen>:
    name: 'blindtest'
    MDToolbar:
        title: "Blindtest"
        pos_hint: {"top": 1}
        id: compteur1
    MDFillRoundFlatButton:
        id: choix1
        pos_hint: {'center_x':0.25,'center_y':0.6}
        size_hint: (0.4,0.3)
    MDFillRoundFlatButton:
        id: choix2
        pos_hint: {'center_x':0.75,'center_y':0.6}
        size_hint: (0.4,0.3)
    MDFillRoundFlatButton:
        id: choix3
        pos_hint: {'center_x':0.25,'center_y':0.2}
        size_hint: (0.4,0.3)
    MDFillRoundFlatButton:
        id: choix4
        pos_hint: {'center_x':0.75,'center_y':0.2}
        size_hint: (0.4,0.3)
<Blindtest_ImageScreen>:
    name: 'blindtest_image'
    MDToolbar:
        id: compteur
        title: "Blintest"
        pos_hint: {"top": 1}
    BoxLayout:
        id: container3
    BoxLayout:
        id: container4
    MDRoundFlatButton:
        text: "Arrêter le blindtest"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        size_hint: (0.3,0.1)
        on_press:
            root.stop_music()
            root.manager.transition.direction = "down" 
            root.manager.current = 'menu'

"""

class Blindtest_ImageScreen(Screen):

    # Cette fonction sert à arrêter le blindtest et à reset les touches du piano.
    def stop_music(self):
        global compteur_points
        
        compteur_points = 0
        
        self.ids.compteur.remove_widget(self.label)
        if image_number != "Image/.jpg":
            self.ids.container3.remove_widget(self.ig)
        self.ids.container4.remove_widget(self.ig23)
        
        print("Stop blindtest")
        subprocess.call(['kill', str(self.manager.p.pid)])
        SetBoard()

        # pour remettre à zéro le blindtest
        cursor.execute("UPDATE Musique_Liste_VOR SET DejaJouer = '0'")
        connection.commit()
        
    # Cette fonction fait changer d'écran après 5 sec   
    def att_blindtest(self, instance):
        global liste_blindtest2
        subprocess.call(['kill', str(self.manager.p.pid)])
        SetBoard()
        if image_number != "Image/.jpg":
            self.ids.container3.remove_widget(self.ig)
        self.ids.container4.remove_widget(self.ig23)
        self.ids.compteur.remove_widget(self.label)
        if securite_2 == 0:
            if len(liste_blindtest2) > 1:
                self.manager.transition.direction = "left"
                self.manager.current = "blindtest"
            else:
                self.manager.transition.direction = "down"
                self.manager.current = "menu"
                
                # pour remettre à zéro le blindtest
                cursor.execute("UPDATE Musique_Liste_VOR SET DejaJouer = '0'")
                connection.commit()
        else:
            pass

    # Cette fonction crée l'écran avec l'image de la musique en question.
    def on_enter(self):
        
        # Importation
        global image_number
        global securite_2
        global rep
        global rep1
        global compteur_points
        
        securite_2 = 0
        
        lengthx = self.center_x * 2
        
        if image_number == None:
            self.ig = Image(source="Image/Pas-d'image.jpg", size=(500, 500))
            self.ig.pos = (self.center_x - self.ig.center_x, self.center_y - self.ig.center_y)
            self.ids.container3.add_widget(self.ig)
        elif image_number != "Image/.jpg":
            # création de l'image juste.
            self.ig = Image(source=image_number, size=(500, 500))
            self.ig.pos = (self.center_x - self.ig.center_x, self.center_y - self.ig.center_y)
            self.ids.container3.add_widget(self.ig)
        
        # Création d'une image en conséquence si la réponse est bonne ou pas.
        if rep == rep1:
            
            compteur_points = compteur_points + 1
            
            # la réponse est bonne un vu est crée.
            ig2 = Image(source="Image/Check.png", size=(160, 160))
            ig2.pos = ((lengthx / 4) - ig2.center_x, self.center_y - ig2.center_y)
            # self.ids.container4.add_widget(ig2)
            
            ig3 = Image(source="Image/Check.png", size=(160, 160))
            ig3.pos = (lengthx - lengthx / 4 - ig3.center_x, self.center_y - ig3.center_y)
            
            self.ig23 = MDLabel()
            self.ig23.add_widget(ig2)
            self.ig23.add_widget(ig3)
            self.ids.container4.add_widget(self.ig23)
        else:
            # la réponse est fausse une croix est créée.
            ig2 = Image(source="Image/Cross.png", size=(160, 160))
            ig2.pos = ((lengthx / 4) - ig2.center_x, self.center_y - ig2.center_y)
            # self.ids.container4.add_widget(ig2)
            
            ig3 = Image(source="Image/Cross.png", size=(160, 160))
            ig3.pos = (lengthx - lengthx / 4 - ig3.center_x, self.center_y - ig3.center_y)
            
            self.ig23 = MDLabel()
            self.ig23.add_widget(ig2)
            self.ig23.add_widget(ig3)
            self.ids.container4.add_widget(self.ig23)
        
        self.label = MDLabel(text=str(len(liste_blindtest)-len(liste_blindtest3))+"/"+str(len(liste_blindtest)),
                             theme_text_color="Custom",text_color=[1,1,1,1],  halign="right")
        
        self.label2 = MDLabel(text=str(compteur_points)+" points",
                             theme_text_color="Custom",text_color=[1,1,1,1],  halign="center")
        self.label2.pos = (self.center_x - self.label2.center_x, self.center_y + self.center_y - self.center_y / 4)
        
        self.label.add_widget(self.label2)
        self.ids.compteur.add_widget(self.label)
        
        # une tempo de 5 seconde puis changement d'écran.
        Clock.schedule_once(self.att_blindtest, 5)

class BlindtestScreen(Screen):
    
    # Récupère le texte du bouton et change d'écran
    def reponses(self, MDFillRoundFlatButton):

        # Récupération d'une variable.
        global rep1
        global rep
        global compteur_points

        # Récupération du texte du bouton choisi
        rep = str(MDFillRoundFlatButton.text[4:len(MDFillRoundFlatButton.text)])

        # Reset du texte des boutons, sinon le nouveau texte se superposera sur l'ancien.
        self.ids.choix1.remove_widget(self.button1)
        self.ids.choix2.remove_widget(self.button2)
        self.ids.choix3.remove_widget(self.button3)
        self.ids.choix4.remove_widget(self.button4)
        self.ids.compteur1.remove_widget(self.label)

        # Changement d'écran.
        self.manager.transition.direction = "left"
        self.manager.current = "blindtest_image"
    
    # Lance une musique aléatoirement de la liste blindtest et créer 4 boutons pour choisir une et juste trois sont fausses.
    def on_enter(self):
        
        # Récupération d'une variable.
        global image_number
        global liste_blindtest2
        global rep1
        global compteur_points
        global liste_blindtest3

        # Création de la liste 2 du blindtest.
        liste_blindtest2 = cursor.execute("SELECT * FROM Musique_Liste_VOR WHERE BlindTest = '1'AND DejaJouer = '0'").fetchall()
        
        # Sélection d'une musique du blindtest
        ras = random.randrange(len(liste_blindtest2))
        rep1 = liste_blindtest2[ras][2]
        print(rep1)
        sa = str(liste_blindtest2[ras][0])
        
        # La musique se joue.
        self.manager.p = subprocess.Popen(["python3", piano, "%s" % liste_blindtest2[ras][1]])
        image_number = liste_blindtest2[ras][6]
        
        # On mets à un dans la colonne déjà jouer la musique sélectionner
        cursor.execute("UPDATE Musique_Liste_VOR SET DejaJouer = '1' WHERE NombreDeMusique = ?", [sa])
        connection.commit()
        
        # Création de la liste 3 du blindtest, qui ne contient pas la musique sélectionner.
        liste_blindtest3 = cursor.execute(
            "SELECT * FROM Musique_Liste_VOR WHERE BlindTest = '1'AND DejaJouer = '0'").fetchall()
        
        # Aléatoirement choisi parmi ce qui reste si il n'y a pas assez on prend ceux déjà utiliser sans que ce soit le même que la réponse
        if len(liste_blindtest3) < 4:
            
            # boucle qui ne fini que si aucune musiques sélectionnées ne correspond à celle jouer.
            while True:
                rep2 = liste_blindtest[random.randint(0, int(len(liste_blindtest)/3))][2]

                rep3 = liste_blindtest[random.randint(int(len(liste_blindtest)/3)+1, int(len(liste_blindtest)/3*2))][2]

                rep4 = liste_blindtest[random.randint(int(len(liste_blindtest)/3*2)+1, len(liste_blindtest)-1)][2]

                if rep2 != rep1 and rep3 != rep1 and rep4 != rep1:
                    break
        else:
            
            # sélection àléatoire des noms de musique de la liste 3.
            rep2 = liste_blindtest3[random.randint(0, int(len(liste_blindtest3)/3))][2]

            rep3 = liste_blindtest3[random.randint(int(len(liste_blindtest3)/3)+1, int(len(liste_blindtest3)/3*2))][2]

            rep4 = liste_blindtest3[random.randint(int(len(liste_blindtest3)/3*2)+1, len(liste_blindtest3)-1)][2]
        
        # on fait une liste de tout les noms et on mélange.
        rep1234 = [rep1, rep2, rep3, rep4]
        random.shuffle(rep1234)
        
        # Création des boutons avec leur texte.
        self.button1 = MDFillRoundFlatButton(text="N°1 " + str(rep1234[0]), font_size=18, on_release=self.reponses)
        self.ids.choix1.add_widget(self.button1)

        self.button2 = MDFillRoundFlatButton(text="N°2 " + str(rep1234[1]), font_size=18, on_release=self.reponses)
        self.ids.choix2.add_widget(self.button2)

        self.button3 = MDFillRoundFlatButton(text="N°3 " + str(rep1234[2]), font_size=18, on_release=self.reponses)
        self.ids.choix3.add_widget(self.button3)

        self.button4 = MDFillRoundFlatButton(text="N°4 " + str(rep1234[3]), font_size=18, on_release=self.reponses)
        self.ids.choix4.add_widget(self.button4)
        
        self.label = MDLabel(text=str(len(liste_blindtest)-len(liste_blindtest3))+"/"+str(len(liste_blindtest)),
                             theme_text_color="Custom",text_color=[1,1,1,1], halign="right")
        
        self.label2 = MDLabel(text=str(compteur_points)+" points",
                             theme_text_color="Custom",text_color=[1,1,1,1],  halign="center")
        self.label2.pos = (self.center_x - self.label2.center_x, 685)
        
        self.label.add_widget(self.label2)
        self.ids.compteur1.add_widget(self.label)

        return self.ids.choix1 and self.ids.choix2 and self.ids.choix3 and self.ids.choix4 and self.ids.compteur1

# écran avec le mot de passe, non utiliser et finaliser pour le moment.
class PasswordScreen(Screen):
    pass

# Le menu pricipale par lequel on choisit les différents mode, assez inutile pour le moment vu que un seul mode fonctionne.
class MenuScreen(Screen):
    
    # Vraiment je dois expliquer cette foncion ?
    def Exit(self):
        led.off()
        SetBoard()
        sleep(1)
        print("Quittez")
        quit()
    
    # Pour bloquer le retour au blindtest.
    def on_enter(self):
        global securite_2
        securite_2 = 1

# La liste de toute les musiques pour pouvoir les écouter au piano.
class Jukebox_ChoiceScreen(Screen):
    
    def random(self):
        play_rand = random.randint(1,len(liste_musique)-1)
        print("Play", play_rand)
        global image_number
        global text_number
        text_number = liste_musique[play_rand - 1][2]
        image_number = liste_musique[play_rand - 1][6]
        self.manager.p = subprocess.Popen(["python3", piano, "%s" % liste_musique[play_rand - 1][1]])
        self.manager.transition.direction = "left"
        self.manager.current = "jukebox_image"

    # Cette fonction sert à jour les musiques.
    def play_music(self, threelineiconlistitem):
        value = int(threelineiconlistitem.text[3:6])
        print("Play", value)
        global image_number
        global text_number
        text_number = liste_musique[value - 1][2]
        image_number = liste_musique[value - 1][6]
        self.manager.p = subprocess.Popen(["python3", piano, "%s" % liste_musique[value - 1][1]])
        print("Send to Finale_manuel.py", liste_musique[value - 1][1]) #for debug
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
                if x < 10:
                    espaces = "  "
                elif x < 100:
                    espaces = " "
                else:
                    espaces = ""
                item = ThreeLineIconListItem(text='No ' + espaces + str(x) + ' - ' + str(row[2]),
                                             secondary_text="Type : " + str(row[5]),
                                             tertiary_text="Date : " + str(row[4]), font_style="H6",
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
        self.ids.container5.remove_widget(self.label)
        if image_number != "Image/.jpg":
            self.ids.container2.remove_widget(self.ig)
        subprocess.call(['kill', str(self.manager.p.pid)])
        SetBoard()

    # Cette fonction crée l'écran avec l'image de la musique en question.
    def on_enter(self):
        global image_number
        global text_number
        print(text_number)
        self.label = MDLabel(text="Actuellement en train de jouer\n" + str(text_number),
                             theme_text_color="Custom",text_color=[0,0,0,1], halign="center",)
        
        self.ids.container5.add_widget(self.label)
        
        if image_number == None:
            self.ig = Image(source="Image/Pas-d'image.jpg", size=(500, 500))
            self.ig.pos = (self.center_x - self.ig.center_x, self.center_y - self.ig.center_y)
            self.ids.container2.add_widget(self.ig)
        elif image_number != "Image/.jpg":
            self.ig = Image(source=image_number, size=(500, 500))
            self.ig.pos = (self.center_x - self.ig.center_x, self.center_y - self.ig.center_y)
            self.ids.container2.add_widget(self.ig)
            
        return self.ids.container2 and self.ids.container5

# Création du manager d'écrans qui permet de faire les lien entre le langage python et kivy
# et de changer d'écrans.

sm = ScreenManager()
sm.add_widget(PasswordScreen(name='password'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Jukebox_ChoiceScreen(name='jukebox_choice'))
sm.add_widget(NoScreen(name="noscreen"))
sm.add_widget(Jukebox_ImageScreen(name="jukebox_image"))
sm.add_widget(BlindtestScreen(name="blintest"))
sm.add_widget(Blindtest_ImageScreen(name="blintest_image"))


# Class fondamentale qui crée la fenêtre.
class MainApp(MDApp):

    # Fonction qui initialise le programme.
    def __init__(self, **kwargs):
        self.title = "Programme VOR"
        #self.theme_cls.theme_style = "Dark"  # "Light" "Dark"
        # self.theme_cls.primary_color =
        super().__init__(**kwargs)

    # Fonction qui construit les écrans.
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


# Cette fonction sert à mettre les sorties de la raspberry pi à 0 sinon les touches de piano reste enfoncé et les
# électroaimants brule.
def SetBoard():
    # master control program/protocol (?)
    mcp = []
    # ajouter les chip aux chips-maitres
    mcp.append(MCP23S17(ce=0x00, deviceID=0x00))  # chip A (ce =0x00 pour ce=0x01 si on change de chip sur les cartes de 128GPIO)
    mcp.append(MCP23S17(ce=0x00, deviceID=0x01))  # chip B ()
    mcp.append(MCP23S17(ce=0x00, deviceID=0x02))  # chip C
    mcp.append(MCP23S17(ce=0x00, deviceID=0x03))  # chip D
    mcp.append(MCP23S17(ce=0x00, deviceID=0x04))  # chip E
    mcp.append(MCP23S17(ce=0x00, deviceID=0x05))  # chip F
    mcp.append(MCP23S17(ce=0x00, deviceID=0x06))  # chip G
    mcp.append(MCP23S17(ce=0x00, deviceID=0x07))  # chip H

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
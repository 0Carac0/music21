'''
Importation des bibliothèques.
'gpiozero' sert à allumer l'alimentation
'Pi_MCP23S17' permet de contrôler le MCP (l'objet collé au Raspberry et qui permet d'activer les notes du piano)
'time' sert principalement à faire des temporisations
'''
from gpiozero import LED
from Pi_MCP23S17 import MCP23S17
from time import *

# Définition du pin de l'alimentation
led = LED(12)

def allumage() : # Création d'une fonction 'allumage()' qui allume l'installation
    led.on()
    sleep(0.4)
    print("\nInstallation allumée\n")
    
def arret() : # Création d'une fonction 'arret()' qui stoppe l'installation
    led.off()
    print("\nInstallation éteinte\n")

rythme = 0

# Déclaration des pins du MCP pour relier le programme aux sorties physiques du MCP (pour diriger les électro-aimants)
mcp = []
# Ajout de "modules" à la liste 'mcp'. Permet de contrôler des "zones" de clavier (16 touches par module)
mcp.append(MCP23S17(ce=0x00, deviceID=0x00))
mcp.append(MCP23S17(ce=0x00, deviceID=0x01))
mcp.append(MCP23S17(ce=0x00, deviceID=0x02))
mcp.append(MCP23S17(ce=0x00, deviceID=0x03))
mcp.append(MCP23S17(ce=0x00, deviceID=0x04))
mcp.append(MCP23S17(ce=0x00, deviceID=0x05))
mcp.append(MCP23S17(ce=0x00, deviceID=0x06))
mcp.append(MCP23S17(ce=0x00, deviceID=0x07))

N = len(mcp) # La variable 'N' prend une valeur équivalente au nombre d'éléments dans la liste 'mcp'

for I in range(N) : # "Ouvre les pins" : permet de déclarer les modules pour que le programme puisse s'en servir
    mcp[I].open()

for I in range(N):
    for x in range(16):
        mcp[I].setDirection(x, mcp[I].DIR_OUTPUT) # Génère les sorties (x = n° de touche, mcp[I] = octave)
        print(x, mcp[I])  # Affiche les notes si lancé depuis un terminal
        mcp[I].digitalWrite(x, MCP23S17.LEVEL_HIGH) # Joue la note sur le piano
        sleep(rythme) # Laisse la note jouer (si rythme < ~0.05, n'a pas le temps de jouer correctement) ATTENTION : Ne pas augmenter la tempo à plus d'une seconde !!
        mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW) # Désactive la note


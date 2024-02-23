'''
Programme ignoble qui simule la musique d'un enfant de 8 ans

ATTENTION : Ne pas activer directement depuis l'éditeur !!
Passer par un terminal vous donnera accès à la commande Ctrl+c
ce qui représente une manière très utile d'arrêter le programme !

'''

from gpiozero import LED
import random
from Pi_MCP23S17 import MCP23S17
from time import *
from xTestPiano import allumage
from xTestPiano import arret

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
        # génère les sorties (x = n° de touche, mcp[I] = octave)
        mcp[I].setDirection(x, mcp[I].DIR_OUTPUT)
        # désactive la note, au cas où
        mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
        
allumage()

# variables qui définissent la durée du programme
surdite = 0
stop = int(input('Durée approximative (un "accord" = 3)\n> '))
# définit la vitesse des notes et déclare des listes
T = 6
duree = []
temps = []
minu = []
maju = []

# génère les valeurs des listes (notes possibles)
for i in range (6) :
    temps.append(float((i+1)/T))
    
for i in range (16) :
    maju.append(i)
    
for i in range (6) :
    minu.append(i)
    
for i in range (7) :
    duree.append(i)

# joue des notes aléatoires, pour une durée aléatoire
while surdite < stop :
    # mélange les notes et les rythmes
    random.shuffle(temps)
    random.shuffle(minu)
    random.shuffle(maju)
    random.shuffle(duree)
    # "pioche" des notes et un rythme aléatoires
    rythme = temps[0]
    x = minu[0]
    y = minu[1]
    z = minu[2]
    X = maju[0]
    Y = maju[1]
    Z = maju[2]
    surdite = surdite + duree[0]
    print("Première note\nHauteur", x, ",", X)
    print("Deuxième note\nHauteur", y, ",", Y)
    print("Troisième note\nHauteur", z, ",", Z)
    if surdite >= stop :
        print("\nProgramme terminé")
    else :
        print("\nDurée :", surdite, "sur", stop, "\n")
    # active les sorties correspondantes
    mcp[x].digitalWrite(X, MCP23S17.LEVEL_HIGH)
    mcp[y].digitalWrite(Y, MCP23S17.LEVEL_HIGH)
    mcp[z].digitalWrite(Z, MCP23S17.LEVEL_HIGH)
    sleep(rythme)
    # désactive les notes
    mcp[x].digitalWrite(X, MCP23S17.LEVEL_LOW)
    mcp[y].digitalWrite(Y, MCP23S17.LEVEL_LOW)
    mcp[z].digitalWrite(Z, MCP23S17.LEVEL_LOW)

arret()

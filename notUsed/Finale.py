from extraction_notes_finale import *
from Pi_MCP23S17 import MCP23S17
from Notes_Pin import *
import time

DEBUG = False

# liste des morceaux

if DEBUG:
    print('''
1 = 4 non-blondes - What's up
2 = Adèle - Skyfall
3 = Adèle - Someone like you
4 = Alan Walker - Alone
5 = Alan Walker - Faded
6 = Alestorm - Nancy The Tavern wench
7 = Amélie poulain - Comptine d'un autre été
8 = Aqua - I'm a Barbie Girl
9 = BabyShark
10 = Beethoven - Bagatella Op33 n5
11 = Beethoven - Moonlight sonata (3rd mouvement)
12 = Boruto - Diver
13 = Boruto - Kakugo 
14 = Boruto - Opening 1 (Baton Road)
15 = Boruto - Spin and Burst (OST)
16 = Carl Douglas - Kung Fu Fighting
17 = Cascada - Every Time We Touch
18 = Case Closed - Detective Conan
19 = Chopin - Fantaisie impromptu (Op 66)
20 = Chopin - Polonaise in A
21 = Crazy Frog - Axel Foley
22 = Daft Punk - Get Lucky
23 = David Guetta - Dangerous
24 = David Guetta feat Martin Garrix - Like I do
25 = David Guetta feat Sia - She wolf falling to pieces
26 = David Guetta feat Sia - Titanium
27 = Different Heaven - Nekozilla
28 = Dimitri Vegas Like Mike vs David Guetta - Complicated
29 = Disfigure - Blank
30 = Don Omar - Danza Kuduro
31 = Dr. Dre feat Snoop Dogg - Still D.R.E
32 = Dr. Dre - What's the difference
33 = DragonForce - Through the fire and the flames
34 = Earth Wind and Fire - September
35 = Eiffel 65 - I'm Blue
36 = Elton John - Your song
37 = Eurythmics - Sweet Dreams
38 = Fairy tail - New Main Theme
39 = Game of thrones - Main Theme
40 = Ghost Busters - Main Theme
41 = Glen Caleb - Off the Shore
42 = Gravity falls - Opening Theme
43 = Harry Potter - Dolores Umbridge
44 = Imagine Dragons - Believer
45 = Imagine Dragons - Radioactive
46 = Inception - Time
47 = Indiana Jones - Main Theme
48 = Interstellar - Main Theme
49 = Israel Kamakawiwo'ole - Somewhere over the rainbow
50 = James Bay - Let it go
51 = Jojo' Bizarre adventure - Main Theme
52 = Jonnhy Haliday - Allumer le feu
53 = Jurassic park - Main Theme
54 = Justice - heavy metal
55 = Katy Perry - Fireworks
56 = Katy Perry - I kissed a girl
57 = Kiss - I was made for loving you
58 = La Casa De Papel - Bella Ciao
59 = La petit Sirène - Sous l'océan
60 = La Reine des neiges - Libéré délivré
61 = Laszlo - Fall to light
62 = Lazy Town - We are number one
63 = Lensko - Cetus 
64 = Linkin Park - Numb
65 = Liszt - La Campanella
66 = Luis Fonsi - Despacito
67 = Marron 5 - Payphone
68 = My Hero academia - Main Theme
69 = Naruto - Sadness and Sorrow
70 = Naruto Shippuden - Opening 3 (Blue Bird)
71 = Naruto Shippuden - Opening 16 (Silouhette)
72 = Naruto Shippuden - Vent
73 = Nyan Cat
74 = One Piece - We are
75 = O'Zone - Dragostea din tei
76 = Patrick Sebastien - Petit bonhomme en mousse
77 = Pirate des Caraïbes - Main Theme
78 = Pokemon - Littleroot Town
79 = Pokemon - Medley
80 = Portugal. The Man - Feel it Still
81 = Red Hot Chili Peppers - Californication
82 = Red Hot Chili Peppers - Snow
83 = Richard Clayderman - Mariage d'amour
84 = Rihanna feat Eminem - Love the way you lie
85 = Rihanna - Love on the Brain
86 = Rimsky-Korsakov - The flight of the Bumble Bee
87 = Roxette - Listen to your heart
88 = Rudimental - These Days
89 = Scylla - Le monde est à mes pieds
90 = Shakira - Waka Waka
91 = Star Wars - Imperial March
92 = Stromae - Formidable
93 = Tetris - Main Theme
94 = The FatRat - Time Lapse
95 = The FatRat - Unity
96 = The Godfather - Main Theme
97 = The Simpsons - Main Theme
98 = Undertale - Megalovania
99 = Undertale - Undertale
100 = Vangelis - Chariots of fire
101 = Vivaldi - Four Season (Summer)
102 = Wii - Main Theme
103 = Wiz Khalifa - See you again
104 = Yann Tiersen - La valse d'Amélie Poulain 
105 = Yuri on ice - Main Theme
106 = ''')

# a specifier dans parametres si autres besoins, sinon par defaut:<c
# path = 'H:/Music21/midi/morning-has-broken-flute-and-bassoon.mid'
# finesse = 0.5 => cadence (pas de temps du tableau) au demi temps (croche)
# debug = False (avec debug = True, la partition midi sera ouverte)

'''
print("Tableau des touches a enclencher par cadence de 'finesse':")
print(enclencher_touches)

print("Tableau des touches a declencher par cadence de 'finesse':")
print(declencher_touches)

print("Indice max des tableaux:")
print(NBR_CASES)
'''

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

    return N, mcp


def SetOutputs(NBR_C, mcp, finesse, dec, enc, tempo):


#    bpm1 = get_bpm(path, midi = converter.parse(path), \
#                   parts = instrument.partitionByInstrument(midi))
#
#    if bpm1 != None:
#        tempo = bpm1
#    else:
#        bpm1 = tempo
# v = volume.Volume(velocity=80)

    for i in range(NBR_C):
        # desactivation des sorties
        for sortie in dec[i]:
            # code pour declencher la sortie:            
            nSortie = sortie % 16
            Bank = int(sortie / 16)

            mcp[Bank].digitalWrite(nSortie,MCP23S17.LEVEL_LOW)
            #print(Bank, nSortie, 'OFF')

        # activation des sorties
        for sortie in enc[i]:
            # code pour enclencher la sortie:
            nSortie = sortie % 16
            Bank = int(sortie / 16)

            mcp[Bank].digitalWrite(nSortie,MCP23S17.LEVEL_HIGH)
            #print(Bank, nSortie, 'ON')

        # temporisation par rapport au tempo
        # code pour attendre (BPS * finesse)

        time.sleep(60/(tempo/finesse))

def fMain(path):

    enclencher_touches, declencher_touches, NBR_CASES = \
        extract_notes(path, finesse = finesse, debug=False,
                      instruments_interdits = instruments_interdits, sequence = sequence)

    try:
        N, mcp = SetBoard()
        SetOutputs(NBR_CASES, mcp, finesse, declencher_touches, enclencher_touches, tempo)

    except KeyboardInterrupt:
        print('\n Program stopped by keyboard.\n')

#        except:
#            print('\n Program stopped by an error. \n')
#     
    finally:
        for x in range(0, 16):
            for I in range(N):
                mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
#                     print(I,x,'OFF')

if __name__ == '__main__':
   main()
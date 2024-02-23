# -*- coding: utf-8 -*-

from extraction_notes_finale_manuel import *
from Pi_MCP23S17 import MCP23S17
from Notes_Pin import *
from rpi_ws281x import *
from typing import List
import sys
import time

# boucle de sélection du morceau
morceau = 0
# securite_2 = 0

while morceau == 0 :
    
    # morceau = str(input('\n\nMusique Numéro : ')) # Choix de la musique par l'utilisateur
    
    morceau = str(sys.argv[1])
    
    if morceau == '1':
        finesse = 0.03125
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/TEST touches.mid'
    elif morceau == '10':
        finesse = 0.03125
        tempo = 125 # BPM
        instruments_interdits = ['Church Bells', 'Trombone']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/4 non-blondes - Whats up.mid'
    elif morceau == '20':
        finesse = 0.03125 
        tempo = 75 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Adèle - Skyfall.mid'
    elif morceau == '30':
        finesse = 0.03125 
        tempo = 67 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Adèle - Someone like you.mid'
    elif morceau == '35':
        finesse = 0.03125 
        tempo = 128 # BPM
        instruments_interdits = ['StringInstrument','Clarinet','Contrabass','Acoustic Bass','Flute','Timpani','StringInstrument']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Aladin - Arabian night.mid'
    elif morceau == '40':
        finesse = 0.03125 
        tempo = 93 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Alan Walker - Alone.mid'
    elif morceau == '50':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Alan Walker - Faded.mid'
    elif morceau == '60':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Alestorm - Nancy The Tavern wench.mid'        
    elif morceau == '70':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Amélie Poulain - Comptine Dun autre été.mid'
    elif morceau == '80':
        finesse = 0.03125 
        tempo = 136 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Aqua - Im a Barbie Girl.mid'
    elif morceau == '81':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 2
        path = '/home/pi/Desktop/Music21/midi/Bach - PreludeAndFugueInCMajor.mid'    
    elif morceau == '90':
        finesse = 0.03125
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/BabyShark.mid'
    elif morceau == '100':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Beethoven - Bagatella Op33 n5.mid'    
    elif morceau == '110':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Beethoven - Moonlight sonata.mid'
    elif morceau == '111':
        finesse = 0.03125 
        tempo = 111 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Beethoven - Ode To Joy.mid'
    elif morceau == '120':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Diver.mid'
    elif morceau == '130':
        finesse = 0.03125
        tempo = 64 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Kakugo.mid'
    elif morceau == '140':
        finesse = 0.03125
        tempo = 162 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Opening 1 (Baton Road).mid'
    elif morceau == '150':
        finesse = 0.03125
        tempo = 180 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Spin and Burst (OST).mid'
    elif morceau == '160':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Carl Douglas - Kung Fu Fighting.mid'
    elif morceau == '170':
        finesse = 0.03125
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Cascada - Every Time We Touch.mid'
    elif morceau == '171':
        finesse = 0.0625
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Cascada-Wham - Last Christmas.mid'
    elif morceau == '190':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Fantaisie-impromptu_Op.66_-_Chopin.mid'
    elif morceau == '191':
        finesse = 0.03125 
        tempo = 170 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Chopin - Mazurka_in_D_major_Op._33_No._2_1838.mid'
    elif morceau == '200':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Chopin - Polonaise in A.mid'
    elif morceau == '205':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Coffin Dance Medley.mid'
    elif morceau == '210':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Crazy_Frog - Axel F.mid'
    elif morceau == '220':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Daft Punk - Get Lucky.mid'
    elif morceau == '230':
        finesse = 0.03125
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta - Dangerous.mid'
    elif morceau == '240':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta feat Martin Garrix - Like I do.mid'
    elif morceau == '250':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta feat Sia  - She wolf falling to pieces.mid'
    elif morceau == '261':
        finesse = 0.0078125
        tempo = 94 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Death Note - The World (opening 1).mid'
    elif morceau == '262':#        finesse = 0.03125
        finesse = 0.0078125
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Kimetsu no Yaïba(Demon Slayer) - Gurenge.mid'
    elif morceau == '263':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Detective Conan - Case Closed.mid'
    elif morceau == '270':
        finesse = 0.    
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Different Heaven - Nekozilla.mid'
    elif morceau == '280':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dimitri Vegas Like Mike vs David Guetta - Complicated.mid'
    elif morceau == '290':
        finesse = 0.03125
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Disfigure - Blank.mid'
    elif morceau == '291':
        finesse = 0.03125
        tempo = 142 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/DOOM - E1M1.mid'
    elif morceau == '300':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Don Omar - Danza Kuduro.mid'
    elif morceau == '310':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dr. Dre feat Snoop Dogg - Still D.R.E.mid'
    elif morceau == '320':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dr. Dre - Whats the Difference.mid'
    elif morceau == '321':
        finesse = 0.03125 
        tempo = 195 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dragon Ball Super - Limit Break X Survivor.mid'
    elif morceau == '322':
        finesse = 0.0078125 
        tempo = 154 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dragon Ball Z - Cha la.mid'
    elif morceau == '323':
        finesse = 0.0078125 
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dragon Ball GT - Dan Dan.mid'
    elif morceau == '330':
        finesse = 0.0078125 
        tempo = 180 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/DragonForce - Through the fire and the flames.mid'
    elif morceau == '340':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Earth Wind and Fire - September.mid'
    elif morceau == '350':
        finesse = 0.03125 
        tempo = 254 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Eiffel 65 - Im Blue.mid'
    elif morceau == '360':
        finesse = 0.03125 
        tempo = 62 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Elton John - Your song.mid'
    elif morceau == '370':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 6
        path = '/home/pi/Desktop/Music21/midi/Eurythmics - Sweet Dreams.mid'
    elif morceau == '371':
        finesse = 0.03125 
        tempo = 126 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Evangelion _ A cruel Angel\'s Thesis.mid'
    elif morceau == '380':
        finesse = 0.03125 
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Fairy Tail - New Main Theme.mid'
    elif morceau == '381':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Final Fantasy - Victory Fanfare.mid'
    elif morceau == '382':
        finesse = 0.03125 
        tempo = 72 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Final Fantasy VII - Cloud theme.mid'
    elif morceau == '383':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Final Fantasy VII - One Winged Angel.mid'
    elif morceau == '384':
        finesse = 0.03125 
        tempo = 170 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Final Fantasy VII - Those who fight.mid'
    elif morceau == '385':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Final Fantasy X - To Zanarkand.mid'
    elif morceau == '389':
        finesse = 0.03125 
        tempo = 187 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Friends - Ill be there 4 you.mid'
    elif morceau == '390':
        finesse = 0.03125 
        tempo = 168 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Game of thrones - Main Theme.mid'
    elif morceau == '400':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['', 'Piano']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Ghost Busters - Main Theme.mid'
    elif morceau == '410':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Glen Caleb - Off the Shore.mid'
    elif morceau == '420':
        finesse = 0.03125 
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Gravity Falls - Opening Theme.mid'
    elif morceau == '421':
        finesse = 0.0625
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Hamster Dance.mid'
    elif morceau == '430':
        finesse = 0.03125
        tempo = 138 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Harry Potter - Dolores Umbridge.mid'
    elif morceau == '431':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Harry Potter - Hedwig theme.mid'
    elif morceau == '432':
        finesse = 0.03125
        tempo = 132 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Hatsune Mikku(Loituma) - Levan Polkka.mid'
    elif morceau == '435':
        finesse = 0.03125
        tempo = 165 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Hercule (Disney) - De Zéro en Héros.mid'
    elif morceau == '440':
        finesse = 0.0078125 
        tempo = 188 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Imagine Dragons - Believer.mid'
    elif morceau == '450':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Imagine Dragons - Radioactive.mid'
    elif morceau == '460':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Inception - Time.mid'
    elif morceau == '465':
        finesse = 0.03125
        tempo = 130 # BPM
        instruments_interdits = ['', 'Piano', 'StringInstrument', 'Timpani']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Indiana Jones - Main Theme.mid'
    elif morceau == '467':
        finesse = 0.03125
        tempo = 170 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Indochine - L aventurier.mid'
    elif morceau == '471':
        finesse = 0.03125
        tempo = 154 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Initial D - Déjà vu.mid'
    elif morceau == '472':
        finesse = 0.03125
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Initial D - Running in the 90\'s .mid'
    elif morceau == '480':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Interstellar - Main Theme.mid'
    elif morceau == '490':
        finesse = 0.03125
        tempo = 170 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Israel Kamakawiwoole - Somewhere over the rainbow.mid'
    elif morceau == '500':
        finesse = 0.03125
        tempo = 70 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/James Bay - Let it Go.mid'
    elif morceau == '510':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jojos Bizarre adventure - Main Theme.mid'
    elif morceau == '511':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jojo\'s Bizarre Adventure - Vento aureo (op1) .mid'
    elif morceau == '512':
        finesse = 0.03125 
        tempo = 147 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/JJBA - Opening 1.mid'
    elif morceau == '513':
        finesse = 0.03125 
        tempo = 222 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/EndOfTheWorld.mid'
    elif morceau == '514':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jack Stauber - Buttercup.mid'
    elif morceau == '519':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/JOPLIN-The entertainer.mid'      
    elif morceau == '520':
        finesse = 0.03125 
        tempo = 194 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jonnhy Haliday - Allumer le feu.mid'
    elif morceau == '521':
        finesse = 0.03125 
        tempo = 127 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/John Williams SCHINDLERS-LIST.mid'
    elif morceau == '530':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jurassic Park - Main Theme.mid'      
    elif morceau == '540':
        finesse = 0.03125
        tempo = 117 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Justice - Heavy Metal.mid'
    elif morceau == '550':
        finesse = 0.03125
        tempo = 125 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Katy Perry - Fireworks.mid'
    elif morceau == '560':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Katy Perry - I kissed a girl.mid'
    elif morceau == '561':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Kingdom Hearts - Dearly Beloved.mid'
    elif morceau == '562':
        finesse = 0.03125 
        tempo = 71 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Kingdom Hearts - Namine.mid'
    elif morceau == '563':
        finesse = 0.0078125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Utada Hikari - Simple and Clean.mid'
    elif morceau == '570':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Kiss - I was made for loving you.mid'
    elif morceau == '580':
        finesse = 0.03125 
        tempo = 136 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Fonola Band - Bella Ciao.mid'
    elif morceau == '590':
        finesse = 0.03125 
        tempo = 184 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Little mermaid - Under the sea.mid'
    elif morceau == '591':
        finesse = 0.0078125 
        tempo = 173 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/L\'arc-en-ciel (GTO) - Driver\'s high.mid'
    elif morceau == '600':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Frozen - Let It Go .mid'
    elif morceau == '610':
        finesse = 0.03125
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Laszlo - Fall to light.mid'
    elif morceau == '620':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Lazy Town - We are number one.mid'
    elif morceau == '621':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Legend of Zelda - Gerudo Valley.mid'
    elif morceau == '622':
        finesse = 0.03125 
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Legend of Zelda - Kokiri Forest.mid'
    elif morceau == '623':
        finesse = 0.03125
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Legend of Zelda - Lon Lon Ranch.mid'
    elif morceau == '630':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Lensko - Cetus.mid'
    elif morceau == '640':
        finesse = 0.03125 
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Linkin Park - Numb.mid'
    elif morceau == '650':
        finesse = 0.03125
        tempo = 120# BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Liszt - La Campanella.mid'
    elif morceau == '659':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Luigi\'s Mansion.mid'
    elif morceau == '660':
        finesse = 0.03125 
        tempo = 89 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Luis Fonsi - Despacito.mid'
    elif morceau == '670':
        finesse = 0.03125 
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Maroon 5 - Payphone.mid'
    elif morceau == '671':
        finesse = 0.03125 
        tempo = 125 # BPM
        instruments_interdits = ['Saxophone','Piano','Percussion']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Michel Sardou - Les lacs du Connemara.mid'
    elif morceau == '672':
        finesse = 0.0078125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Mozart - Rondo a la Turca.mid'
    elif morceau == '673':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Mulan - Comme un homme.mid'
    elif morceau == '679':
        finesse = 0.03125 
        tempo = 195 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/My hero Academia - Hero too.mid'
    elif morceau == '680':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/My Hero academia - Main Theme.mid'
    elif morceau == '681':
        finesse = 0.03125 
        tempo = 200 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/My Hero Academia - Peace Sign.mid'
    elif morceau == '682':
        finesse = 0.03125 
        tempo = 185 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/My hero Academia - The Day.mid'
    elif morceau == '685':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/My neighbor Totori - Ending.mid'
    elif morceau == '690':
        finesse = 0.03125 
        tempo = 72 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto - Sadness and Sorrow.mid'
    elif morceau == '700':
        finesse = 0.03125
        tempo = 152 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto Shippuden - Opening 3 (Blue Bird).mid'
    elif morceau == '710':
        finesse = 0.03125
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto Shippuden - Opening 16 (Silhouette).mid'
    elif morceau == '720':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto Shippuden - Vent.mid'
    elif morceau == '721':
        finesse = 0.03125
        tempo = 142 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/No Game No Life - This Game.mid'
    elif morceau == '722':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Nekozilla - Different Heaven.mid'
    elif morceau == '725':
        finesse = 0.03125
        tempo = 77 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Nier Automata - Weight of The world.mid'
    elif morceau == '730':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Nyan Cat.mid'
    elif morceau == '731':
        finesse = 0.00390625 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Olive et Tom - opening.mid'
    elif morceau == '740':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/One Piece - Saké de Binks.mid'
    elif morceau == '741':
        finesse = 0.03125
        tempo = 168 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/One Piece - We Are.mid'
    elif morceau == '749':
        finesse = 0.03125
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/One Punch Man - THE HERO!!.mid'
    elif morceau == '750':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/OZone - Dragostea din tei.mid'    
    elif morceau == '751':
        finesse = 0.03125
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pachelbel_Canon.mid'  
    elif morceau == '760':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['', 'Percussion', 'Piano']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Patrick Sebastien - Petit bonhomme en mousse.mid'
    elif morceau == '770':
        finesse = 0.03125 
        tempo = 200 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Pirates des Caraïbes - Main Theme.mid'
    elif morceau == '774':
        finesse = 0.03125 
        tempo = 180 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Battle Theme.mid'
    elif morceau == '775':
        finesse = 0.0078125
        tempo = 196 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Trainer Red.mid'
    elif morceau == '776':
        finesse = 0.03125 
        tempo = 180 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Gotta Catch\'em all.mid'
    elif morceau == '780':
        finesse = 0.03125 
        tempo = 107 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Littleroot Town.mid'
    elif morceau == '790':
        finesse = 0.03125
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Medley.mid'
    elif morceau == '791':
        finesse = 0.03125
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Rival.mid'
    elif morceau == '800':
        finesse = 0.03125 
        tempo = 168 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Portugal. The Man - Feel it still.mid'
    elif morceau == '810':
        finesse = 0.03125
        tempo = 95 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Red Hot Chili Peppers - Californication.mid'
    elif morceau == '820':
        finesse = 0.03125
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Red Hot Chili Peppers - Snow.mid'
    elif morceau == '830':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Richard Clayderman - Mariage Damour.mid'
    elif morceau == '840':
        finesse = 0.03125
        tempo = 87 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Rihanna feat Eminem - Love the way you lie.mid'
    elif morceau == '850':
        finesse = 0.03125
        tempo = 75 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Rihanna - Love on the Brain.mid'
    elif morceau == '860':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/RimskyKorsakov - Flight of the Bumblebee.mid'
    elif morceau == '870':
        finesse = 0.03125 
        tempo = 88 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Roxette - Listen to your heart.mid'
    elif morceau == '880':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Rudimental - These Days.mid'
    elif morceau == '885':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Scriabin - Etude Op2 No1.mid'
    elif morceau == '886':
        finesse = 0.03125 
        tempo = 105 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Scriabin - étude Op.8 No.12 in D-sharp minor.mid'
    elif morceau == '890':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Scylla - Le monde est à mes pieds.mid'
    elif morceau == '891':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Sergey Stepanov - Epic Sax Guy.mid'
    elif morceau == '900':
        finesse = 0.03125
        tempo = 127 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Shakira - Waka Waka.mid'
    elif morceau == '910':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Star Wars - Imperial March.mid'
    elif morceau == '920':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Stromae - Formidable.mid'
    elif morceau == '921':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Super Mario 64 - BobOmb Battlefield.mid'
    elif morceau == '929':
        finesse = 0.03125 
        tempo = 145 # BPM
        instruments_interdits = ['Flute', 'Oboe', 'Bassoon','Clarinet','Saxophone','Electric Bass','Trumpet','Trombone','Tuba','Steel Drum','Percussion']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Super Smash Bros Ultimate Lifelight (1).mid'
    elif morceau == '930':
        finesse = 0.03125 
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Tetris - Korobeiniki.mid'
    elif morceau == '940':
        finesse = 0.03125
        tempo = 127 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The FatRat - Time Lapse.mid'
    elif morceau == '950':
        finesse = 0.03125
        tempo = 104 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The FatRat - Unity.mid'
    elif morceau == '960':
        finesse = 0.03125
        tempo = 72 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The Godfather - Main Theme.mid'
    elif morceau == '961':
        finesse = 0.03125 
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/This_is_Halloween.mid'
    elif morceau == '970':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['percussion']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The Simpsons - Main Theme.mid'
    elif morceau == '971':
        finesse = 0.0078125 
        tempo = 184 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Toy Story - You\'ve Got a Friend in Me.mid'
    elif morceau == '974':
        finesse = 0.0078125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale - Bonetrousle.mid'
    elif morceau == '975':
        finesse = 0.0078125 
        tempo = 230 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale - Doge song.mid'
    elif morceau == '980':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale - Megalovania.mid'
    elif morceau == '985':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale - Spear of Justice.mid'
    elif morceau == '990':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale - Undertale.mid'
    elif morceau == '999':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Vanessa Carlton - A Thousand miles.mid'
    elif morceau == '1000':
        finesse = 0.03125 
        tempo = 126 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Vangelis - Chariots of fire.mid'
    elif morceau == '1010':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Vivaldi - Four season (summer).mid'
    elif morceau == '1020':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Wii - Main Theme.mid'
    elif morceau == '1030':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Wiz Khalifa - See you again.mid'
    elif morceau == '1040':
        finesse = 0.03125
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Yann Tiersen - La valse d amélie Poulain.mid'
    elif morceau == '1045':
        finesse = 0.03125
        tempo = 70 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Yiruma - River Flows in you.mid'
    elif morceau == '1050':
        finesse = 0.03125 
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Yuri on ice - Main Theme.mid'
    
    #else:
        #if securite_2 == 0:
            #print("\n\nCe numéro n'est pas valable\n")
            #morceau = 0
            #securite_2 = 1
    
    
    

    
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



# associer les sorties aux leds
# hypothese: "sortie" est un entier de 1 a n
# si hypothese incorrect, remplacer SORTIE_LEDS par un dict {1: [1,2], 2: [3,4]}
LISTE_LEDS = {
     [1, 2, 3],          # sortie A0 associees aux leds 1, 2, 3
     [4],                # sortie A#0 associees aux led 4
     [5, 6, 7],          # sortie B0 associees aux leds 5, 6, 7
     [8, 9],             # sortie C1 associees aux leds 8, 9
     [10],               # sortie C#1 associees aux led 10
     [11, 12, 13],       # sortie D1 associees aux leds 11,12,13
     [14],               # sortie D#1 associees aux led 14
     [15, 16, 17],       # sortie E1 associees aux leds 15,16,17
     [18, 19],           # sortie F1 associees aux leds 18,19
     [20],               # sortie F#1 associees aux led 20
     [21, 22, 23],       # sortie G1 associees aux leds 21,22,23
     [24],               # sortie G#1 associees aux led 24
     [25, 26, 27],       # sortie A1 associees aux leds 25,26,27
     [28],               # sortie A#1 associees aux led 28
     [29, 30],           # sortie B1 associees aux leds 29, 30
     [31, 32, 33],       # sortie C2 associees aux leds 31, 32, 33
     [34],               # sortie C#2 associees aux led 34
     [35, 36, 37],       # sortie D2 associees aux leds 35, 36, 37
     [38],               # sortie D#2 associees aux led 38
     [39, 40, 41],       # sortie E2 associees aux leds 39, 40, 41
     [42, 43],           # sortie F2 associees aux leds 42, 43
     [44],               # sortie F#2 associees aux led 44
     [45, 46, 47],       # sortie G2 associees aux leds 45, 46, 47
     [48],               # sortie G#2 associees aux led 48
     [49, 50, 51],       # sortie A2 associees aux leds 49, 50, 51
     [52],               # sortie A#2 associees aux led 52
     [53, 54],           # sortie B2 associees aux leds 53, 54
     [55, 56],           # sortie C3 associees aux leds 55, 56
     [57, 58],           # sortie C#3 associees aux leds 57, 58
     [59, 60, 61],       # sortie D3 associees aux leds 59, 60, 61
     [62],               # sortie D#3 associees aux led 62
     [63, 64],           # sortie E3 associees aux leds 63, 64
     [65, 66, 67],       # sortie F3 associees aux leds 65, 66, 67
     [68],               # sortie F#3 associees aux leds 68
     [69, 70],           # sortie G3 associees aux leds 69, 70
     [71],               # sortie G#3 associees aux led 71
     [72, 73, 74],       # sortie A3 associees aux leds 72, 73, 74
     [75],               # sortie A#3 associees aux led 75
     [76, 77, 78],       # sortie B3 associees aux leds 76, 77, 78
     [79, 80],           # sortie C4 associees aux leds 79, 80
     [81, 82],           # sortie C#4 associees aux leds,81, 82
     [83, 84, 85],       # sortie D4 associees aux leds 83, 84, 85
     [86],               # sortie D#4 associees aux led 86
     [87, 88],           # sortie E4 associees aux leds 87, 88
     [89, 90],           # sortie F4 associees aux leds 89, 90
     [91, 92],           # sortie F#4 associees aux leds 91, 92
     [93, 94],           # sortie G4 associees aux leds 93, 94
     [95, 96],           # sortie G#4 associees aux leds 95, 96
     [97, 98],           # sortie A4 associees aux leds 97, 98
     [99],               # sortie A#4 associees aux led 99
     [100, 101, 102],    # sortie B4 associees aux leds 100, 101, 102
     [103, 104],         # sortie C5 associees aux leds 103, 104
     [105],              # sortie C#5 associees aux led 105
     [106, 107, 108],    # sortie D5 associees aux leds 106, 107, 108
     [109],              # sortie D#5 associees aux led 109
     [110, 111, 112],    # sortie E5 associees aux leds 110, 111, 112
     [113, 114],         # sortie F5 associees aux leds 113, 114
     [115],              # sortie F#5 associees aux led 115
     [116, 117, 118],    # sortie G5 associees aux leds 116, 117, 118
     [119],              # sortie G#5 associees aux led 119
     [120, 121, 122],    # sortie A5 associees aux leds 120, 121, 122
     [123],              # sortie A#5 associees aux led 123
     [124, 125],         # sortie B5 associees aux leds 124, 125
     [126, 127, 128],    # sortie C6 associees aux leds 126, 127, 128
     [129],              # sortie C#6 associees aux led 129
     [130, 131, 132],    # sortie D6 associees aux leds 130, 131, 132
     [133],              # sortie D#6 associees aux led 133
     [134, 135],         # sortie E6 associees aux leds 134, 135
     [136, 137, 138],    # sortie F6 associees aux leds 136, 137, 138
     [139],              # sortie F#6 associees aux led 139
     [140, 141],         # sortie G6 associees aux leds 140, 141
     [142, 143],         # sortie G#6 associees aux leds 142, 143
     [144, 145],         # sortie A6 associees aux leds 144, 145
     [146],              # sortie A#6 associees aux led 146
     [147, 148],         # sortie B6 associees aux leds 147, 148
     [149, 150, 151],    # sortie C7 associees aux leds 149, 150, 151
     [152],              # sortie C#7 associees aux led 152
     [153, 154, 155],    # sortie D7 associees aux leds 153, 154, 155
     [156],              # sortie D#7 associees aux led 156
     [157, 158, 159],    # sortie E7 associees aux leds 157, 158, 159
     [160, 161],         # sortie F7 associees aux leds 160, 161
     [162],              # sortie F#7 associees aux led 162
     [163, 164, 165],    # sortie G7 associees aux leds 163, 164, 165
     [166],              # sortie G#7 associees aux led 166
     [167, 168, 169],    # sortie A7 associees aux leds 167, 168, 169
}

# LED strip configuration:
LED_COUNT = 169       # Number of LED pixels. LED = 169
LED_PIN = 10           # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()


def set_leds(strip: PixelStrip, leds: List[int], color: Color) -> None:
    """Set specific leds from strip to a certain color.

    :param strip: led strip to operat on
    :param leds: list of leds position to set
    :param color: color in which to set the leds
    """
    
    
    for i in leds:
        strip.setPixelColor(i, color)
       
    strip.show()

def SetOutputs(NBR_C, mcp, PixelStrip, finesse, dec, enc):
    
    
#    bpm1 = get_bpm(path, midi = converter.parse(path), \
#                   parts = instrument.partitionByInstrument(midi))
#    
#    if bpm1 != None:
#        tempo = bpm1
#    else:
#        bpm1 = tempo
# v = volume.Volume(velocity=80)   
    
    for i in range(NBR_C):

        for sortie in dec[i]:   # desactivation des sorties
                                # code pour declencher la sortie:
            nSortie = sortie % 16
            Bank = int(sortie / 16)
            
            mcp[Bank].digitalWrite(nSortie,MCP23S17.LEVEL_LOW)
            # set led off for the specified output
            # éteindre la led dont le numéro est nSortie -> tab_led[nSortie] -> (0,0,0)
            set_leds(strip, LISTE_LEDS[sortie], Color(0, 0, 0))
            #print(Bank, nSortie, 'OFF')
            

        for sortie in enc[i]:   # activation des sorties
                                # code pour enclencher la sortie:
            nSortie = sortie % 16
            Bank = int(sortie / 16)
            
            mcp[Bank].digitalWrite(nSortie,MCP23S17.LEVEL_HIGH)
            # allumer la led dont le numéro est nSortie -> tab_led[nSortie] -> (255,255,255)
            # set led on for specified output
            set_leds(strip, LISTE_LEDS[sortie], Color(255, 255, 255))

            #print(Bank, nSortie, 'ON')
    
        # temporisation par rapport au tempo
        # code pour attendre (BPS * finesse)
        
        time.sleep(60/(tempo/finesse))
   
def main():
    
    
    enclencher_touches, declencher_touches, NBR_CASES = \
        extract_notes(path, finesse = finesse, debug=False, instruments_interdits = instruments_interdits, sequence = sequence)

    try:
        N, mcp = SetBoard()
        SetOutputs(NBR_CASES, mcp, strip, finesse, declencher_touches, enclencher_touches)
    
    except KeyboardInterrupt:
        print('\n Program stopped by keyboard.\n')

#     except:
#         print('\n Program stopped by an error. \n')
        
    finally:
        for x in range(0, 16):
            for I in range(N):
                mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
#                print(I,x,'OFF')
    
if __name__ == '__main__':
    main()
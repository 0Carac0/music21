# -*- coding: utf-8 -*-

from extraction_notes_finale_manuel import *
from Pi_MCP23S17 import MCP23S17
from Notes_Pin import *
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
        instruments_interdits = ['','Church Bells', 'Trombone']
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

def SetOutputs(NBR_C, mcp, finesse, dec, enc):
    
    
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
            
            # éteindre la led dont le numéro est nSortie -> tab_led[nSortie] -> (0,0,0)
            
            #print(Bank, nSortie, 'OFF')
            
        # activation des sorties
        for sortie in enc[i]:
            # code pour enclencher la sortie:
            nSortie = sortie % 16
            Bank = int(sortie / 16)
            
            mcp[Bank].digitalWrite(nSortie,MCP23S17.LEVEL_HIGH)
            
            # allumer la led dont le numéro est nSortie -> tab_led[nSortie] -> (255,255,255)
            
            #print(Bank, nSortie, 'ON')
    
        # temporisation par rapport au tempo
        # code pour attendre (BPS * finesse)
        
        time.sleep(60/(tempo/finesse))
   
def main():
    
    
    enclencher_touches, declencher_touches, NBR_CASES = \
        extract_notes(path, finesse = finesse, debug=False, instruments_interdits = instruments_interdits, sequence = sequence)

    try:
        N, mcp = SetBoard()
        SetOutputs(NBR_CASES, mcp, finesse, declencher_touches, enclencher_touches)
    
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
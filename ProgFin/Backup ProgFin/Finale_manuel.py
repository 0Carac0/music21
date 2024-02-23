from extraction_notes_finale import *
from Pi_MCP23S17 import MCP23S17
from Notes_Pin import *
import time
from ScreenSelection import *


# liste des morceaux
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

# boucle de sélection du morceau
morceau = 0

while morceau == 0 :

#    morceau = str(input('\n\nMusique Numéro : ')) # Choix de la musique par l'utilisateur
    morceau = kv.JukeBoxMode.showSelection()
    
    if morceau == '1':
        finesse = 0.03125
        tempo = 125 # BPM
        instruments_interdits = ['','Church Bells', 'Trombone']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/4 non-blondes - Whats up.mid'
    elif morceau == '2':
        finesse = 0.03125 
        tempo = 75 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Adèle - Skyfall.mid'
    elif morceau == '3':
        finesse = 0.03125 
        tempo = 67 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Adèle - Someone like you.mid'
    elif morceau == '4':
        finesse = 0.03125 
        tempo = 93 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Alan Walker - Alone.mid'
    elif morceau == '5':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Alan Walker - Faded.mid'
    elif morceau == '6':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Alestorm - Nancy The Tavern wench.mid'        
    elif morceau == '7':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Amélie Poulain - Comptine Dun autre été.mid'
    elif morceau == '8':
        finesse = 0.03125 
        tempo = 136 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Aqua - Im a Barbie Girl.mid'
    elif morceau == '9':
        finesse = 0.03125
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/BabyShark.mid'
    elif morceau == '10':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Beethoven - Bagatella Op33 n5.mid'    
    elif morceau == '11':
        finesse = 0.03125 
        tempo = 170 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Beethoven - Moonlight sonata (3rd mouvement).mid'
    elif morceau == '12':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Diver.mid'
    elif morceau == '13':
        finesse = 0.03125
        tempo = 64 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Kakugo.mid'
    elif morceau == '14':
        finesse = 0.03125
        tempo = 162 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Opening 1 (Baton Road).mid'
    elif morceau == '15':
        finesse = 0.03125
        tempo = 180 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Boruto - Spin and Burst (OST).mid'
    elif morceau == '16':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Carl Douglas - Kung Fu Fighting.mid'
    elif morceau == '17':
        finesse = 0.03125
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Cascada - Every Time We Touch.mid'
    elif morceau == '18':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Case Closed - Detective Conan.mid'
    elif morceau == '19':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Chopin - Fantaisie impromptu (Op 66).mid'
    elif morceau == '20':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Chopin - Polonaise in A.mid'
    elif morceau == '21':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Crazy Frog - Axel Foley.mid'
    elif morceau == '22':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Daft Punk - Get Lucky.mid'
    elif morceau == '23':
        finesse = 0.03125
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta - Dangerous.mid'
    elif morceau == '24':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta feat Martin Garrix - Like I do.mid'
    elif morceau == '25':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta feat Sia  - She wolf falling to pieces.mid'
    elif morceau == '26':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/David Guetta feat Sia - Titanium.mid'
    elif morceau == '27':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Different Heaven - Nekozilla.mid'
    elif morceau == '28':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dimitri Vegas Like Mike vs David Guetta - Complicated.mid'
    elif morceau == '29':
        finesse = 0.03125
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Disfigure - Blank.mid'
    elif morceau == '30':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Don Omar - Danza Kuduro.mid'
    elif morceau == '31':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dr. Dre feat Snoop Dogg - Still D.R.E.mid'
    elif morceau == '32':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Dr. Dre - Whats the Difference.mid'    
    elif morceau == '33':
        finesse = 0.03125 
        tempo = 180 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/DragonForce - Through the fire and the flames.mid'
    elif morceau == '34':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Earth Wind and Fire - September.mid'
    elif morceau == '35':
        finesse = 0.03125 
        tempo = 254 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Eiffel 65 - Im Blue.mid'
    elif morceau == '36':
        finesse = 0.03125 
        tempo = 62 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Elton John - Your song.mid'
    elif morceau == '37':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 6
        path = '/home/pi/Desktop/Music21/midi/Eurythmics - Sweet Dreams.mid'
    elif morceau == '38':
        finesse = 0.03125 
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Fairy Tail - New Main Theme.mid'
    elif morceau == '39':
        finesse = 0.03125 
        tempo = 168 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Game of thrones - Main Theme.mid'
    elif morceau == '40':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['', 'Piano']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Ghost Busters - Main Theme.mid'
    elif morceau == '41':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Glen Caleb - Off the Shore.mid'
    elif morceau == '42':
        finesse = 0.03125 
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Gravity Falls - Opening Theme.mid'
    elif morceau == '43':
        finesse = 0.03125
        tempo = 138 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Harry Potter - Dolores Umbridge.mid'
    elif morceau == '44':
        finesse = 0.03125 
        tempo = 188 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Imagine Dragons - Believer.mid'
    elif morceau == '45':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Imagine Dragons - Radioactive.mid'
    elif morceau == '46':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Inception - Time.mid'
    elif morceau == '47':
        finesse = 0.03125
        tempo = 130 # BPM
        instruments_interdits = ['', 'Piano', 'StringInstrument', 'Timpani']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Indiana Jones - Main Theme.mid'
    elif morceau == '48':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Interstellar - Main Theme.mid'
    elif morceau == '49':
        finesse = 0.03125
        tempo = 170 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Israel Kamakawiwoole - Somewhere over the rainbow.mid'
    elif morceau == '50':
        finesse = 0.03125
        tempo = 70 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/James Bay - Let it Go.mid'
    elif morceau == '51':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jojos Bizarre adventure - Main Theme.mid'
    elif morceau == '52':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jonnhy Haliday - Allumer le feu.mid'
    elif morceau == '53':
        finesse = 0.03125 
        tempo = 60 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Jurassic Park - Main Theme.mid'
    elif morceau == '54':
        finesse = 0.03125
        tempo = 117 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Justice - Heavy Metal.mid'
    elif morceau == '55':
        finesse = 0.03125
        tempo = 125 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Katy Perry - Fireworks.mid'
    elif morceau == '56':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Katy Perry - I kissed a girl.mid'
    elif morceau == '57':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Kiss - I was made for loving you.mid'
    elif morceau == '58':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/La Casa De Papel - Bella Ciao.mid'
    elif morceau == '59':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['', 'Steel Drum', 'Piano', 'Piccolo']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/La petite Sirène - Sous locéan.mid'
    elif morceau == '60':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/La Reine des neiges - Libéré Délivré.mid'
    elif morceau == '61':
        finesse = 0.03125
        tempo = 175 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Laszlo - Fall to light.mid'
    elif morceau == '62':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Lazy Town - We are number one.mid'
    elif morceau == '63':
        finesse = 0.03125
        tempo = 128 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Lensko - Cetus.mid'
    elif morceau == '64':
        finesse = 0.03125 
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Linkin Park - Numb.mid'
    elif morceau == '65':
        finesse = 0.03125
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Liszt - La Campanella.mid'
    elif morceau == '66':
        finesse = 0.03125 
        tempo = 89 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Luis Fonsi - Despacito.mid'
    elif morceau == '67':
        finesse = 0.03125 
        tempo = 110 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Maroon 5 - Payphone.mid'
    elif morceau == '68':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/My Hero academia - Main Theme.mid'
    elif morceau == '69':
        finesse = 0.03125 
        tempo = 72 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto - Sadness and Sorrow.mid'
    elif morceau == '70':
        finesse = 0.03125
        tempo = 152 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto Shippuden - Opening 3 (Blue Bird).mid'
    elif morceau == '71':
        finesse = 0.03125
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto Shippuden - Opening 16 (Silhouette).mid'
    elif morceau == '72':
        finesse = 0.03125
        tempo = 90 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Naruto Shippuden - Vent.mid'
    elif morceau == '73':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Nyan Cat.mid'
    elif morceau == '74':
        finesse = 0.03125
        tempo = 168 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/One Piece - We Are.mid'
    elif morceau == '75':
        finesse = 0.03125 
        tempo = 130 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/OZone - Dragostea din tei.mid'
    elif morceau == '76':
        finesse = 0.03125
        tempo = 135 # BPM
        instruments_interdits = ['', 'Percussion', 'Piano']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Patrick Sebastien - Petit bonhomme en mousse.mid'
    elif morceau == '77':
        finesse = 0.03125 
        tempo = 200 # BPM
        instruments_interdits = ['']
        sequence = 5
        path = '/home/pi/Desktop/Music21/midi/Pirates des Caraïbes - Main Theme.mid'
    elif morceau == '78':
        finesse = 0.03125 
        tempo = 107 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Littleroot Town.mid'
    elif morceau == '79':
        finesse = 0.03125
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Pokemon - Medley.mid'
    elif morceau == '80':
        finesse = 0.03125 
        tempo = 158 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Portugal. The Man - Feel it still.mid'
    elif morceau == '81':
        finesse = 0.03125
        tempo = 95 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Red Hot Chili Peppers - Californication.mid'
    elif morceau == '82':
        finesse = 0.03125
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Red Hot Chili Peppers - Snow.mid'
    elif morceau == '83':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Richard Clayderman - Mariage Damour.mid'
    elif morceau == '84':
        finesse = 0.03125
        tempo = 87 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Rihanna feat Eminem - Love the way you lie.mid'
    elif morceau == '85':
        finesse = 0.03125
        tempo = 75 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Rihanna - Love on the Brain.mid'
    elif morceau == '86':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Flight_of_the_bumble_bee.mid'
    elif morceau == '87':
        finesse = 0.03125 
        tempo = 88 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Listen_To_Your_Heart__Roxette.mid'
    elif morceau == '88':
        finesse = 0.03125 
        tempo = 92 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Rudimental - These Days.mid'
    elif morceau == '89':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Scylla_Le_monde_est__mes_pieds.mid'
    elif morceau == '90':
        finesse = 0.03125
        tempo = 127 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Waka_Waka_This_Time_For_Africa.mid'
    elif morceau == '91':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The Imperial March - Star Wars.mid'
    elif morceau == '92':
        finesse = 0.03125
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Formidable_Stromae.mid'
    elif morceau == '93':
        finesse = 0.03125 
        tempo = 135 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Tetris_-_Theme_A.mid'
    elif morceau == '94':
        finesse = 0.03125
        tempo = 127 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Timelapse by Bagio.mid'
    elif morceau == '95':
        finesse = 0.03125
        tempo = 104 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Unity by Bagio.mid'
    elif morceau == '96':
        finesse = 0.03125
        tempo = 72 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The-Godfather-Theme.mid'
    elif morceau == '97':
        finesse = 0.03125 
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/The_Simpsons_Theme_by_Danny_Elfman.mid'
    elif morceau == '98':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale_-_Megalovania_Piano_ver._3.mid'
    elif morceau == '99':
        finesse = 0.03125 
        tempo = 100 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Undertale_Undertale_Piano.mid'
    elif morceau == '100':
        finesse = 0.03125 
        tempo = 126 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Chariots_of_Fire_Piano_Theme.mid'
    elif morceau == '101':
        finesse = 0.03125 
        tempo = 140 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Vivaldi_-_Summer__The_Four_Seasons__-_Rousseau.mid'
    elif morceau == '102':
        finesse = 0.03125 
        tempo = 120 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Wii_Theme.mid'
    elif morceau == '103':
        finesse = 0.03125 
        tempo = 80 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/See_You_Again_-_Wiz_Khalifa__Charlie_Puth_Piano_Tutorial_.mid'
    elif morceau == '104':
        finesse = 0.03125
        tempo = 150 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/La_Valse_dAmelie_original_version_Yann_Tiersen.mid'
    elif morceau == '105':
        finesse = 0.03125 
        tempo = 160 # BPM
        instruments_interdits = ['']
        sequence = 4
        path = '/home/pi/Desktop/Music21/midi/Yuri_on_Ice_-_Piano_Theme_Full.mid'
    else:
        print("\n\nCe numéro n'est pas valable\n")
        morceau = 0
    
    

    
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
   
def main():
    
    
    enclencher_touches, declencher_touches, NBR_CASES = \
        extract_notes(path, finesse = finesse, debug=False, instruments_interdits = instruments_interdits, sequence = sequence)

    try:
        N, mcp = SetBoard()
        SetOutputs(NBR_CASES, mcp, finesse, declencher_touches, enclencher_touches)
    
    except KeyboardInterrupt:
        print('\n Program stopped by keyboard.\n')

#    except:
#        print('\n Program stopped by an error. \n')
        
    finally:
        for x in range(0, 16):
            for I in range(N):
                mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
#                print(I,x,'OFF')
    
if __name__ == '__main__':
    main()
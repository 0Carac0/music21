from extraction_notes_finale_manuel import *
from Pi_MCP23S17 import MCP23S17
from Notes_Pin import *
import sys
import time


# liste des morceaux
print('''
10 = 4 non-blondes - What's up
20 = Adèle - Skyfall
30 = Adèle - Someone like you
35 = Aladin - Arabian night
40 = Alan Walker - Alone
50 = Alan Walker - Faded
60 = Alestorm - Nancy The Tavern wench
70 = Amélie poulain - Comptine d'un autre été
80 = Aqua - I'm a Barbie Girl
81 = Bach - PreludeAndFugueInCMajor
90 = BabyShark
100 = Beethoven - Bagatella Op33 n5
110 = Beethoven - Moonlight sonata (3rd mouvement)
111 = Beethoven - Ode to Joy
120 = Boruto - Diver
130 = Boruto - Kakugo 
140 = Boruto - Opening 1 (Baton Road)
150 = Boruto - Spin and Burst (OST)
160 = Carl Douglas - Kung Fu Fighting
170 = Cascada - Every Time We Touch
180 = Case Closed - Detective Conan
190 = Chopin - Fantaisie impromptu (Op 66)
200 = Chopin - Polonaise in A
205 = Coffin Dance Medley
210 = Crazy Frog - Axel Foley
220 = Daft Punk - Get Lucky
230 = David Guetta - Dangerous
240 = David Guetta feat Martin Garrix - Like I do
250 = David Guetta feat Sia - She wolf falling to pieces
260 = David Guetta feat Sia - Titanium
261 = Death Note - The World (opening 1)
262 = Demon Slayer - Gurenge (opening 1)
270 = Different Heaven - Nekozilla
280 = Dimitri Vegas Like Mike vs David Guetta - Complicated
290 = Disfigure - Blank
291 = DOOM - E1M1
300 = Don Omar - Danza Kuduro
310 = Dr. Dre feat Snoop Dogg - Still D.R.E
320 = Dr. Dre - What's the difference
321 = Dragon Ball Super - Limit Break X Survivor
330 = DragonForce - Through the fire and the flames
340 = Earth Wind and Fire - September
350 = Eiffel 65 - I'm Blue
360 = Elton John - Your song
370 = Eurythmics - Sweet Dreams
371 = Evangelion - A cruel Angel's thesis
380 = Fairy tail - New Main Theme
381 = Final Fantasy - Victory Theme
382 = Final Fantasy VII - Cloud Theme
383 = Final Fantasy VII - One Winged Angel
384 = Final Fantasy VII - Those who fight
390 = Game of thrones - Main Theme
400 = Ghost Busters - Main Theme
410 = Glen Caleb - Off the Shore
420 = Gravity falls - Opening Theme
421 = Hamster Dance
430 = Harry Potter - Dolores Umbridge
432 = Hatsune Miku (Loituma) - Levan Polkka
435 = Hercule (Disney) - De Zéro en Héro
440 = Imagine Dragons - Believer
450 = Imagine Dragons - Radioactive
460 = Inception - Time
470 = Indiana Jones - Main Theme
471 = Initial D - Déjà Vu
472 = Initial D - Running in the 90's
480 = Interstellar - Main Theme
490 = Israel Kamakawiwo'ole - sortedmewhere over the rainbow
500 = James Bay - Let it go
510 = Jojo' Bizarre adventure - Main Theme
511 = Jojo' Bizarre adventure - Il Vento d'oro
512 = Jojo' Bizarre adventure - Sono Chi No Sadame
519 = JOPLIN - The entertainer
520 = Jonnhy Haliday - Allumer le feu
521 = John Williams - Schindlers List
530 = Jurassic park - Main Theme
540 = Justice - heavy metal
550 = Katy Perry - Fireworks
560 = Katy Perry - I kissed a girl
561 = Kingdom Hearts - Dearly Beloved
562 = Kingdom Hearts - Namine's theme
563 = Kingdom Hearts - Simple And Clean
570 = Kiss - I was made for loving you
580 = La Casa De Papel - Bella Ciao
590 = La petit Sirène - Sous l'océan
591 = L'arc-en-ciel (GTO) - Driver's high
600 = La Reine des neiges - Libéré délivré
601 = Liszt La Campanella
610 = Laszlo - Fall to light
620 = Lazy Town - We are number one
621 = Legend of Zelda - Gerudo Valley
622 = Legend of Zelda - Kokiri Forest
623 = Legend of Zelda - Lon Lon Ranch
630 = Lensko - Cetus 
640 = Linkin Park - Numb
650 = Liszt - La Campanella
659 = Luigi's Mansion - Theme
660 = Luis Fonsi - Despacito
670 = Marron 5 - Payphone
671 = Michel Sardou - Les Lacs du Connemara
672 = Mozart - RondoAllaTurca
673 = Mulan - I'll make a man out of you
680 = My Hero academia - Main Theme
685 = My neighbor Totoro - Theme
690 = Naruto - Sadness and Sorrow
700 = Naruto Shippuden - Opening 3 (Blue Bird)
710 = Naruto Shippuden - Opening 16 (Silouhette)
720 = Naruto Shippuden - Vent
725 = Nier Automata - Weight of the World
730 = Nyan Cat
740 = One Piece - Sake de Binks
741 = One Piece - We are
750 = O'Zone - Dragostea din tei
751 = Pachelbel_Canon.mid
760 = Patrick Sebastien - Petit bonhomme en mousse
770 = Pirate des Caraïbes - Main Theme
775 = Pokemon - Gotta Catch'em all !
780 = Pokemon - Littleroot Town
790 = Pokemon - Main theme
800 = Portugal. The Man - Feel it Still
810 = Red Hot Chili Peppers - Californication
820 = Red Hot Chili Peppers - Snow
830 = Richard Clayderman - Mariage d'amour
840 = Rihanna feat Eminem - Love the way you lie
850 = Rihanna - Love on the Brain
860 = Rimsky-Korsakov - The flight of the Bumble Bee
870 = Roxette - Listen to your heart
880 = Rudimental - These Days
890 = Scylla - Le monde est à mes pieds
891 = Sergey Stepanov = Epic Sax Guy
900 = Shakira - Waka Waka
910 = Star Wars - Imperial March
920 = Stromae - Formidable
921 = Super Mario 64 - BobOmb Battlefield
929 = Super Smash Bros. Ultimate - Lifelight
930 = Tetris - Main Theme
940 = The FatRat - Time Lapse
950 = The FatRat - Unity
960 = The Godfather - Main Theme
961 = The Nightmare before Christmas - This is Halloween
970 = The Simpsons - Main Theme
971 = Toy Story (Disney) - You've got a friend in me
975 = Undertale - Doge song
980 = Undertale - Megalovania
985 = Undertale - Spear of Justice
990 = Undertale - Undertale
999 = Vanessa Carlton - A Thousand Miles
1000 = Vangelis - Chariots of fire
1010 = Vivaldi - Four Season (Summer)
1020 = Wii - Main Theme
1030 = Wiz Khalifa - See you again
1040 = Yann Tiersen - La valse d'Amélie Poulain 
1050 = Yuri on ice - Main Theme
1060 = 
1070 = ''')

# boucle de sélection du morceau
#morceau = 0

#while morceau == 0 :

    #morceau = str(input('\n\nMusique Numéro : ')) # Choix de la musique par l'utilisateur
    
morceau = str(sys.argv[1])
    
if morceau == '10':
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
    tempo = 120 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Beethoven - Bagatella Op33 n5.mid'    
elif morceau == '110':
    finesse = 0.03125 
    tempo = 170 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Beethoven - Moonlight sonata (3rd mouvement).mid'
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
elif morceau == '180':
    finesse = 0.03125 
    tempo = 130 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Case Closed - Detective Conan.mid'
elif morceau == '190':
    finesse = 0.03125 
    tempo = 150 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Chopin - Fantaisie impromptu (Op 66).mid'
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
    path = '/home/pi/Desktop/Music21/midi/Crazy Frog - Axel Foley.mid'
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
elif morceau == '260':
    finesse = 0.03125
    tempo = 135 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/David Guetta feat Sia - Titanium.mid'
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
elif morceau == '270':
    finesse = 0.03125
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
    tempo = 120 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/La Casa De Papel - Bella Ciao.mid'
elif morceau == '590':
    finesse = 0.03125 
    tempo = 150 # BPM
    instruments_interdits = ['', 'Steel Drum', 'Piano', 'Piccolo']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/La petite Sirène - Sous locéan.mid'
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
    path = '/home/pi/Desktop/Music21/midi/La Reine des neiges - Libéré Délivré.mid'
elif morceau == '601':
    finesse = 0.03125
    tempo = 120 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Liszt_LaCampanella.mid'
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
    tempo = 100 # BPM
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
    tempo = 120 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Mozart - RondoAllaTurca.mid'
elif morceau == '673':
    finesse = 0.03125 
    tempo = 100 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Mulan - Comme un homme.mid'
elif morceau == '680':
    finesse = 0.03125 
    tempo = 120 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/My Hero academia - Main Theme.mid'
elif morceau == '685':
    finesse = 0.03125 
    tempo = 130 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/My Neighbor Totoro - Theme.mid'
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
elif morceau == '751':
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
elif morceau == '775':
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
elif morceau == '800':
    finesse = 0.03125 
    tempo = 158 # BPM
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
    path = '/home/pi/Desktop/Music21/midi/Rimsky-Korsakov - The flight of the Bumble Bee.mid'
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
    path = '/home/pi/Desktop/Music21/midi/Tetris - Main Theme.mid'
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
elif morceau == '1050':
    finesse = 0.03125 
    tempo = 160 # BPM
    instruments_interdits = ['']
    sequence = 4
    path = '/home/pi/Desktop/Music21/midi/Yuri on ice - Main Theme.mid'
    
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

#     except:
#         print('\n Program stopped by an error. \n')
        
    finally:
        for x in range(0, 16):
            for I in range(N):
                mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
#                print(I,x,'OFF')
    
if __name__ == '__main__':
    main()
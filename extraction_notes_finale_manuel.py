# -*- coding: utf-8 -*-

from music21 import *
from rpi_ws281x import *
import time as tm

# Active ou désactive les temporisations et certaines données d'affichage dans le terminal de commande. Ralentit énormément le lancement des musiques. En fonctionnement normal, mettre à 0
# 1 == temporisations sur les évènements spéciaux lors de l'extraction (changement de note, conversions etc) 2 == temporisations courtes à chaque note 3 == temporisations longues
tpDebug = 0

def tri_notes(tracks, finesse, sequence=4):
    global tpDebug
    
    conv_ctr = 0
    conv_bd = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    sorties_notes = [
        'A0','A#0','B0',
        'C1','C#1','D1','D#1','E1','F1','F#1','G1','G#1','A1','A#1','B1',
        'C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2',
        'C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3',
        'C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4',
        'C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5',
        'C6','C#6','D6','D#6','E6','F6','F#6','G6','G#6','A6','A#6','B6',
        'C7','C#7','D7','D#7','E7','F7','F#7','G7','G#7','A7','A#7','B7',
        'C8','C#8','D8','D#8','E8','F8','F#8','G8','G#8','A8','A#8','B8'
        ]

    maximum = 0 # On pense que cette mémoire sert à la fin du programme, à tester (elle n'a aucune incidence sur le début et milieu du morceau)
    for entry in tracks :
        if entry[1] > maximum:
            if tpDebug > 0 :
                print(entry)
                tm.sleep(0.015 * (tpDebug -1))
            maximum = entry[1]
    pos_maximum = maximum + 1 + int(5.0/finesse) # ajout du 1 pour le temps t=0 et pour laisser la place a au maximum une ronde (OFF) 
    etapes_ON  = pos_maximum*[0]
    etapes_OFF = pos_maximum*[0] 
    for I in range(pos_maximum):
        etapes_ON[I]  = []
        etapes_OFF[I] = []
    
    '''
    
    ####################################
    
    L E   P R O B L è M E   E S T   L à
    
    Musique : Aria Math (morceau == '1057')
    > La dernière note du morceau, pour une raison encore indéterminée, rallonge les autres notes de la musique et fait se chevaucher des notes sans pour autant en changer la valeur.
    
    ####################################
    
    '''
    print("Nbr de pas de la sequence ON: %s\n" % (len(etapes_ON)))
    print("Nbr de pas de la sequence OFF: %s\n" % (len(etapes_OFF)))
    try :
        for note in tracks: # note[0] = la note à jouer, note[1] = au moment ou la note doit être jouée, note[2] = durée de la note
            #if note != tracks[-1] : # Condition de test (englobe tout jusqu'au 'print' en-dessus du return (non-compris). A supprimer lors d'un cycle normal. Permet de ne pas jouer la dernière note)
            #print(note)
            
            for noteFuture in tracks:
                if tpDebug > 0 :
                    tm.sleep(0.015 * (tpDebug -1))
                
                # Le bloc suivant permet d'éviter le chevauchement de deux mêmes notes qui devraient normalement se suivre mais qui sont jouées sur le même moment. Ce bloc sépare les deux instances de la note et permet de relâcher la touche entre les deux
                if note[0] == noteFuture[0] and noteFuture[1] > note[1] : # Vérification de la présence d'une note de même hauteur dans les prochains temps
                    #print(note, noteFuture)
                    if note[2] >= (noteFuture[1] - note[1]) - 4 : # True si la 'note' et la 'noteFuture' ont moins de 4 unités de temps entre le relâchement de la première et l'appui de la seconde
                        note[2] = (noteFuture[1] - note[1]) - 4 # Raccourcit la première note de faÇon à ce qu'elle soit jouée moins longtemps afin de laisser un temps de relâchement de 4 unités avant la deuxième note
                        if tpDebug > 0 :
                            print('CHANGEMENT DE DUREE', note, noteFuture)
                            tm.sleep(0.02 * (tpDebug))
                    break                
            
            '''
            if note[2] >= 232 : # Debug la musique Aria Math (solution temporaire)
                note[2] = 190
                if tpDebug > 0
                    print('Changement de longueur de note')
                    tm.sleep(0.1)
            '''
            
            #print(note)
            
            if '-' in note[0]:  # test de la presence de bemols et conversion en diese
                conv_ctr += 1
                note[0] = conv_bd[conv_bd.index(note[0][0])-1] + '#' + note[0][2] # Prend la valeur de la note en bémol (p.ex. Gb4 (ou "G-4")) puis la sépare : récupère 'note[0][0]' (la note, donc 'G') et la remplace par la note "inférieure" ('G' devient 'F'), y colle le symbole '#' (pour que la note soit un dièze) puis ajoute 'note[0][2]' (càd l'octave, en l'occurrence '4') /!\ il faut savoir qu'en musique, une note bémole est égale à la note dièze inférieure. Par exemple, Db2 = C#2    
            #etapes_OFF[note[1]+note[2]].append(sorties_notes.index(note[0]))
            etapes_ON[note[1]].append(sorties_notes.index(note[0]))
            while len(etapes_OFF) <= (note[1]+note[2]+sequence) :
                etapes_OFF.append([])
                
                
            while len(etapes_ON) < (len(etapes_OFF)) :
                etapes_ON.append([])
                
            if tpDebug > 0 :
                print("Longueur de la liste 'etapes_ON' :", len(etapes_ON), "\nLongueur de la liste 'etapes_OFF' :", len(etapes_OFF))
                tm.sleep(0.1 * (tpDebug -1))
                
            etapes_OFF[note[1]+note[2]-sequence].append(sorties_notes.index(note[0])) # decalage de 1 case pour pouvoir jouer repetitions
            etapes_ON[note[1]].append(sorties_notes.index(note[0]))
            
            if note[1]+note[2]-sequence <= note[1]:
                print("depart: "+str(note[1])+" - fin: "+str(note[1]+note[2]-sequence))
                if tpDebug > 0 :
                    tm.sleep(0.2 * tpDebug)
            
                
        print("%s bemol(s) converti(s) en diese.\n" % (conv_ctr))
        #print(etapes_ON, etapes_OFF, pos_maximum)
        return etapes_ON, etapes_OFF, pos_maximum
    except :
        print('Problème dans la conversion de dièzes')



def extract_notes(path = '/home/pi/Desktop/Music21/midi/Barbie_Girl.mid', finesse = 0.25, debug = False, instruments_interdits = [''], sequence = 4):
    # finesse de 0.5 => noire dure 2 temps au lieu d'1, elle est a adapter en fonction de la + petite duree de note (0.5 => croche)
    # instruments_interdits = ['']
    
    try:
        midi = converter.parse(path)
        # recuperation des pistes 'voix' qui ne présentent pas d'instrument
        for I in range(len(midi)):
            if not(midi[I].getInstrument(returnDefault=False)):
                midi[I].insert(instrument.Percussion())
                midi[I].insert(instrument.Piano()) 
        if debug:
            midi.show() # affichage de la partition sur MuseScore si installe
        parts = instrument.partitionByInstrument(midi)
        # recuperation des infos generales du fichier midi
        instrument_list = []    # tableau des instruments
        for piste in midi:
            for entry in piste:
                if isinstance(entry, meter.TimeSignature):
                    time_signature = str(entry)
                else:
                    time_signature = 'none'
                if isinstance(entry, instrument.Instrument):
                    if str(entry) not in instruments_interdits:
                        instrument_list.append(str(entry))
                if isinstance(entry, key.KeySignature):
                    music_key = str(entry)
                else:
                    music_key = 'none'
        print("\nInstrument(s):")
        for instr in instrument_list:
            print(instr)
        print("\nClef: %s\nMesure: %s \n" % (music_key, time_signature[-4:-1]))
        print("Pas temporel du tableau: %s temps" % (finesse))
        # recuperation des notes pour les instruments suivants > histoire de generer un tableau unique pour notre systeme
        note_list = []
        pause = False
        for music_instrument in range(len(parts)):
            if parts.parts[music_instrument].id in instrument_list:
                for element_by_offset in stream.iterator.OffsetIterator(parts[music_instrument]):
                    for entry in element_by_offset:
                        if isinstance(entry, note.Note):
                            info_note = []  # note et offset, duree pas utilise pour l'instant
                            info_note.append(str(entry.pitch))  # "note"
                            # "ARRONDI" de l offset via variable finesse (plus petit pas possible entre note)
                            info_note.append(int(entry.offset/finesse)) # offset = timestamp de la note en "temps" par rapport a t=0
                            if int(entry.duration.quarterLength/finesse) == 0: # Quand on a des triples croches, on leurs donne automatiquement 
                                info_note.append(8)                            # une durée de 8 séquence pour que la note ne reste pas au fond 
                            else:                                              # et qu'elle ait le temps de jouer la note
                                info_note.append(int(entry.duration.quarterLength/finesse)) # "duree"
                            note_list.append(info_note) # ajout de la note dans le tableau
                        elif isinstance(entry, chord.Chord):
                            for n in entry:
                                info_note = []
                                info_note.append(str(n.pitch))
                                info_note.append(int(entry.offset/finesse)) # l offset est au niveau de l accord et non de la note !
                                info_note.append(int(n.duration.quarterLength/finesse))
                                note_list.append(info_note)
                        elif isinstance(entry, note.Rest):
                            pause = True    # pause presente sur la piste
    
        
    
        return tri_notes(note_list, finesse, sequence)
    
    except Exception as e:
        print(e)
        pass
     

# si classe appelee toute seule, generation du tableau des notes du fichier par defaut
if __name__ == "__main__":
    print(extract_notes())
    print(get_bpm())

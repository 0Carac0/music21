from music21 import *

def tri_notes(tracks, finesse):
    conv_ctr = 0
    conv_bd = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    sorties_notes = [
        'C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2',
        'C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3',
        'C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4',
        'C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5',
        'C6','C#6','D6','D#6','E6','F6','F#6','G6','G#6','A6','A#6','B6'
        ]
    max = 0
    for entry in tracks:
        if entry[1] > max:
            max = entry[1]
    pos_max = max + 1 + int(5.0/finesse) # ajout du 1 pour le temps t=0 et pour laisser la place a au max une ronde (OFF)
    etapes_ON  = pos_max*[0]
    etapes_OFF = pos_max*[0] 
    for I in range(pos_max):
        etapes_ON[I]  = []
        etapes_OFF[I] = []
    print("Nbr de pas de la sequence: %s\n" % (len(etapes_ON)))
    for note in tracks:
        if '-' in note[0]:  # test de la presence de bemols et conversion en diese
            conv_ctr += 1
            note[0] = conv_bd[conv_bd.index(note[0][0])-1] + '#' + note[0][2]
        etapes_ON[note[1]].append(sorties_notes.index(note[0]))
        etapes_OFF[note[1]+note[2]].append(sorties_notes.index(note[0]))
    print("%s bemol(s) converti(s) en diese.\n" % (conv_ctr))
    return etapes_ON, etapes_OFF, pos_max

def extract_notes(path = 'H:/Music21/midi/morning-has-broken-flute-and-bassoon.mid', finesse = 0.5, debug = False):
    # finesse de 0.5 => noire dure 2 temps au lieu d'1, elle est a adapter en fonction de la + petite duree de note (0.5 => croche)
    try:
        midi = converter.parse(path)
        if debug:
            midi.show() # affichage de la partition sur MusicScore si installe
        parts = instrument.partitionByInstrument(midi)
        # recuperation des infos generales du fichier midi
        instrument_list = []    # tableau des instruments
        for piste in midi:
            for entry in piste:
                if isinstance(entry, meter.TimeSignature):
                    time_signature = str(entry)
                if isinstance(entry, instrument.Instrument):
                    instrument_list.append(str(entry))
                if isinstance(entry, key.KeySignature):
                    music_key = str(entry)
        print("Instrument(s): (fusiones pour notre piano)")
        for instr in instrument_list:
            print(instr)
        print("\nClef: %s\nMesure: %s \n" % (music_key, time_signature[-4:-1]))
        print("Pas temporel du tableau: %s temps\n(1 temps = une noire)" % (finesse))
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
        if pause:
            print("Presence de pauses dans notre fichier.\n")
        return tri_notes(note_list, finesse)
    
    except Exception as e:
        print(e)
        pass
   
# si classe appelee toute seule, generation du tableau des notes du fichier par defaut
if __name__ == "__main__":
    print(extract_notes())

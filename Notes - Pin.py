###############################################################################
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#                               Daniel Burnier                                # 
#            Algoritme de traduction nomDeNoteOctave - BankPortPin            #
#  Pour MBR                                                         18.11.19  #
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
###############################################################################


appNote,seltNote,note,octaves,piano = '',[],['A','A#','B','C',
                                         'C#','D','D#','E', 
                                         'F','F#', 'G', 'G#'],\
                                         [0,1,2,3,4,5,6,7,8],[]
# notes à écarter
exception = []

qPin, bank, port, pin, pins = [],['A','B','C','D','E','F','G','H'],\
                            [1,2],\
                            [1,2,3,4,5,6,7,8],[]

# ecriture de chaque note dans le format NOTEOCTAVE
# avec gestion des exceptions ('A#0,B0,C1' par ex)
for j in range(len(octaves)):
    for i in range(len(note)):
        if j == 0 and i >= 3:
            exception.append((note[i],octaves[j]))
        elif j == 1 and i <= 2:
            exception.append((note[i],octaves[j]))
        elif j == 8 and i >= 1:
            exception.append((note[i],octaves[j]))
        else:
            appNote = note[i] + str(octaves[j])
            piano.append(appNote)

print(piano,len(piano))

# ecriture de tous les pins possibles dans le format BANKPORTPIN
for x in range(len(bank)):
    for y in range(len(port)):
        for z in range(len(pin)):
            appPin = bank[x] + str(port[y]) + str(pin[z])
            pins.append(appPin)

nNotes = int(input('Combien de notes ? \n'))

for m in range(nNotes):
    selNote = input('Entrez les notes : ').upper()
    qNote = piano.index(selNote)
    qPin.append(pins[qNote])
    

print(qPin)
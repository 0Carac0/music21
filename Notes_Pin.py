###############################################################################
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#                               Daniel Burnier                                #
#            Algoritme de traduction nomDeNoteOctave - BankPortPin            #
#  Pour MBR                                                         18.11.19  #
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
###############################################################################
 
def Notes_Pin(nNotes, selNote):
 
    note,octaves,piano = ['C','C#','D','D#',
                          'E','F','F#', 'G',
                          'G#', 'A','A#','B'],\
                          [0,1,2,3,4,5,6],[]
 
    qPin, bank, port, pin, pins = [],['A','B','C','D','E','F','G','H'],\
                                [1,2],\
                                [1,2,3,4,5,6,7,8],[]
 
 
    # ecriture de chaque note dans le format NOTEOCTAVE
    for j in range(len(octaves)):
        for i in range(len(note)):
            piano.append(note[i] + str(octaves[j]))

    
                
    # ecriture de tous les pins possibles dans le format BANKPORTPIN
    for x in range(len(bank)):
        for y in range(len(port)):
            for z in range(len(pin)):
                pins.append(bank[x] + str(port[y]) + str(pin[z]))
 
    for m in range(len(pins)):
        if m == piano.index(piano[selNote]):
            qPin.append(m) 

 
    return qPin
 
def mainA():
   
    Notes_Pin(1, 21)
   
if __name__ == '__main__':
    mainA()
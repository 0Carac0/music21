from music21 import *
from extraction_notes_finale import *
from Pi_MCP23S17 import MCP23S17
from Notes_Pin import *
import time



def VelocityNote(velocity = 128):
    
    v = volume.Volume(velocity = velNote)
    print(v.cachedRealizedStr)
    
    return v.cachedRealizedStr, velocity

if __name__ == "__main__":

    velNote = int(input('>'))
    VelocityNote(velNote)
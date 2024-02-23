#!/usr/bin/python

from Pi_MCP23S17 import MCP23S17
import time

N = 4 # nombre de chip

try:
    # master control program/protocol (?)
    mcp = []
    # ajouter les chip aux chips-maitres
    mcp.append(MCP23S17()) # chip A
    mcp.append(MCP23S17(deviceID=0x01)) # chip B
    mcp.append(MCP23S17(deviceID=0x02)) # chip C
    mcp.append(MCP23S17(deviceID=0x03)) # chip D
    
    for I in range(N):
        mcp[I].open()

    for x in range(0, 16):
        for I in range(N):
            mcp[I].setDirection(x, mcp[I].DIR_OUTPUT)
    
    
    
    print("Starting blinky on all pins (CTRL+C to quit)")
    while (True):
#        mcp[1].digitalWrite(1, MCP23S17.LEVEL_HIGH) # activer (mettre au niveau haut) la sortie numero 5 du chip C

        for x in range(0, 16):
            for I in range(N):
                #mcp[0].digitalWrite(x, MCP23S17.LEVEL_HIGH)
                print(mcp[1], x, 'ON')
        time.sleep(2)

#        mcp[1].digitalWrite(1, MCP23S17.LEVEL_LOW) # activer (mettre au niveau haut) la sortie numero 5 du chip C


        for x in range(0, 16):
            for I in range(N):
                mcp[I].digitalWrite(x, MCP23S17.LEVEL_LOW)
                print(mcp[1], x, 'OFF')
        time.sleep(2)
        



finally:
    for I in range(N):
        mcp[I].close()

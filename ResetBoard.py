from Pi_MCP23S17 import MCP23S17


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
        
del mcp

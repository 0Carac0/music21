from ySourceProg import *

allumage()

rythme = 0.4
"""
accord sol majeur
x1 = 2
y1 = 2
x2 = 2
y2 = 6
x3 = 2
y3 = 9
x4 = 2
y4 = 14
"""

x1 = 2
y1 = 5
x2 = 2
y2 = 8
x3 = 2
y3 = 12
x4 = 3
y4 = 1

# G2
mcp[x1].digitalWrite(y1, MCP23S17.LEVEL_HIGH)
# laisse la note jouer (si rythme < ~0.05, n'a pas le temps de jouer correctement)
sleep(rythme)
# B2
mcp[x2].digitalWrite(y2, MCP23S17.LEVEL_HIGH)
#temps de pause 
sleep(rythme)
#D2
mcp[x3].digitalWrite(y3, MCP23S17.LEVEL_HIGH)
#temps de pause
sleep(rythme)
#G2 finale
mcp[x4].digitalWrite(y4, MCP23S17.LEVEL_HIGH)
sleep(0.4)
# désactive la note
mcp[x1].digitalWrite(y1, MCP23S17.LEVEL_LOW)
mcp[x2].digitalWrite(y2, MCP23S17.LEVEL_LOW)
mcp[x3].digitalWrite(y3, MCP23S17.LEVEL_LOW)
mcp[x4].digitalWrite(y4, MCP23S17.LEVEL_LOW)


arret()
from extraction_notes_mid import *

enclencher_touches, declencher_touches, NBR_CASES = extract_notes(path='c:/Users/danburnier/Desktop/Music21/midi/morning-has-broken-flute-and-bassoon.mid', debug=False)

# a specifier dans parametres si autres besoins, sinon par defaut:
# path = 'H:/Music21/midi/morning-has-broken-flute-and-bassoon.mid'
# finesse = 0.5 => cadence (pas de temps du tableau) au demi temps (croche)
# debug = False (avec debug = True, la partition midi sera ouverte) 

print("Tableau des touches a enclencher par cadence de 'finesse':")
print(enclencher_touches)

print("Tableau des touches a declencher par cadence de 'finesse':")
print(declencher_touches)

print("Indice max des tableaux:")
print(NBR_CASES)

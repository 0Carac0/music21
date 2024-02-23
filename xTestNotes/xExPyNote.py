from xTestPiano import *

'''
Appelle la fonction 'allumage()' et attend quelques instants
pour que l'alimentation soit bien enclenchée.
À la fin du programme, éteint l'alimentation.
'''

allumage()
enter = 0

try :
    vitesse = float(input("Durée de chaque note (en secondes) ?\n> "))
    uniqHaut = str(input("Jouer uniquement la zone à problèmes ?   y / n\n> "))
    repeat = str(input("Répétition ?   y / n\n> "))
except :
    print("Programme réinitialisé et terminé. Valeur non-valide.")
 
try :
    SetBoard(vitesse, uniqHaut, repeat)
except :
    sleep(0.5)
    SetBoard(0, "n", "n")

arret()

print("Fin de programme")


'''
POUR TESTER LES NOTES :
  1) Ouvrir un terminal
  2) Accéder à l'emplacement de ce fichier via 'cd'
  3) Lancer le programme via 'python3 xExPyNote.py'
  4) Choisir un rythme ("BPM" = notes par minutes) -> 0.007 Commutation visible ; 0.025 Quelques notes jouées ; 0.3 Presque toutes notes jouées ; 0.04 Toutes notes jouées
/!\ Éviter si possible d'interrompre le programme en cours.
Si cela est vraiment nécessaire, l'arrêter avec Ctrl+c puis relancer
immédiatement le programme et n'entrer aucune vitesse, seulement
appuyer sur Enter.
Il s'agit d'un programme non-sécurisé et expérimental, et les
électro-aimants chauffent bien trop s'ils sont maintenus longtemps.
'''


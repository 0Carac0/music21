iAmTesting = [7, 2.9, 29, 13, 45, 18, 20, 34]
attemptsNumber = 0
print ("I want twenty :)")
for x in iAmTesting :
   print ("I'm testing this one...")
   print (x)
   attemptsNumber = (attemptsNumber + 1)
   if x == 20 :
      print ("\nYay it's twenty :D\n\n")
      break
   else :
      print ("\nNah it's not twenty :C\n\n")
print ("It took ", attemptsNumber, " attempts")


a = int (input ("Input a number : "))

if a == 20 :
   print ("It's twenty !\nThanks !! :D")
else :
   if a < 30 and a > 20 :
      print ("Hum... It is not 20, but ", a, " is cool too. I take it :|")
   else :
      print ("NO !! I WANT TWENTY ! >:O")

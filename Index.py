print("The Number you have to guess is between 0 and 100")
import random
on = random.randint(0,100)
if on % 2 == 0:
    print("The Number to guess is Even")
else :
    print("The Number to guess is Odd")

c = 1

while c < 7 :
 gn = int(input("Guess :"))
 c += 1
 if on == gn :
  print("Correct Guess. Congratulations!🎉🎉👏🏻")
 elif on > gn :
    print("The Guess is Too Small")
 elif gn > on :
    print("The Guess is Too High ")
 if c == 7 and gn != on  :
    print("Sorry. There are only 6 chances and You finished them All. You Lost 😞😓.")


   








     


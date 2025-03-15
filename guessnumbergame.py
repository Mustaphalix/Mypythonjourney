import random

secretnumber = random.randint(1, 30)

for guessattempt in range(1,5):
   print('Enter a number to guess from  1 to 30')
   guess = int(input())
   
   if guess < secretnumber:
      print('Number is to low!')
   elif guess > secretnumber:
      print('Number is too big!')
   else:
      break
if guess == secretnumber:
   print('Youre correct , you made the guess in '+str(guessattempt)+' attempt')
else:
   print("The guess number i expect is " +str(secretnumber))
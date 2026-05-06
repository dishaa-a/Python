import random
target = (random.randrange(1, 100))

while True:

   userNum = int(input("Enter a number:"))
   if(target == userNum):
        print("You win!")
        break
   elif(target < userNum):
        print("Guess a lower number.")
   else:
        print("Guess a higher number.")

print("--Game Over--")
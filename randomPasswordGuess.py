import random


target = random.randint(1,100)
attempt = 0
print("welcome to the Random number game! Can you guess the game  under 10 tries!")

#I am using  infinite loop but  inside the loop i will break  bcause  i need to ask from user  again and again when user not give the correct answer that why  while i have from True boolean value 
while True:
  userChoice = input("Guess the target number Or Quit(Q):  ")
  attempt +=1
  if userChoice == "Q" or  userChoice == "q":
    print("You quite the game! The Correct answer is: ",target)
    break
  if not userChoice.isdigit():
    print("Invalid input: Please enter the valid Number or Q (quit)") 
    continue

  userChoice = int(userChoice)
  if userChoice == target:
   
    print("Sucess: Correct Guess!!" )
    print("Sucess: Your total attempts are: ",attempt,"You won the game" )
        
    break
  elif userChoice < target:
    print("Your num is less than target number...")
  else:
     print("Your num is greater than target number...")


  if (attempt >=10) :
    print("Your attempt is more than 10 Please Try again") 
    break


print("-----Game Over-----")  



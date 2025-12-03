# import random

# num = random.randrange(0, 10,2)
# print("computer selected a number from 0 to 10 (incusive),now pick a number -")
# turns=0
# while True:
#     guess=int(input("enter the number guessed ="))
#     if (guess==num):
#         print("\n\tyou got it right")
#         break
#     elif(guess<num):
#         print("\tBigger number please")
#         turnck
#     elif(guess>num):
#         print("Lesser number please")
#         turnck
# print("Number of turns = ",)

# import random

# probability =["rock", "paper", "scissors"]




# turns = 0

# while turns <  3 :
#     turns+=1

#     result = probability[random.randint(0,2)]  

#     choice = int(input(" enter 0 for rock for paper and 2 for scissors: "))
   
#     print(f"you chose {probability[choice]} and computer chose {result}")

#     print("you have 3 turns")
#     if result == probability[choice]:
#         print("it is a tie")
#         print(f"you chose {probability[choice]} and computer chose {result}")

#     elif result == "rock" and probability[choice] == "paper":
#         print("you win")
#         print(f"you chose {probability[choice]} and computer chose {result}")
        
#     elif result == "paper" and probability[choice] == "scissors":
#         print("you win")
#         print(f"you chose {probability[choice]} and computer chose {result}")
        
#     elif result == "scissors" and probability[choice] == "rock":
#         print("you win")
#         print(f"you chose {probability[choice]} and computer chose {result}")
#     else:
#         print("you lose")
#         print(f"you chose {probability[choice]} and computer chose {result}")

    
# print("Number of turns = ",)  

    



# file  = open("text.txt","w")
# file.write("happy birthday to you")
# content  = file.read()
# print(content)
# file.close()


# with open ("notiq.txt","w") as file:
#     notiq =input("enter message")
#     file.write(notiq)
#     print(notiq)

# with open ("notiq.txt","a") as file:
#     notiq =input("enter message")
#     file.write("\n by notiq\n"+notiq)
    

def view():
    with open ("Arteta.txt","r") as file:
       sush = file.read()  
       print(sush)

def add():
    name = input("Enter the name of the player: ")
    position = input("Enter the position of the player: ")
    number = input("Enter the number of the player: ")    

    with open  ("Arteta.txt","a") as file:
              file.write(f"Name: {name}\nPosition: {position}\nNumber: {number}\n\n")
              print("Player added successfully")  

while True :
       print("Welcome to the Arsenal FC squad also known as the Gunners or  should I say the Notiq fc")                                         
       print("________________________")     
       print("1. View squad")
       print("2. Add player")
       print("3. Exit")

       choice = input("Enter your choice: ")

       if choice == "1":
          view()
          print("you chose one")
       elif choice == "2":
            add()
            print("you chose 2")
       elif choice == "3":
            print("It was nice having you here")
            print("you chose 3")
            break
       else:
            print("invalid choice")
            

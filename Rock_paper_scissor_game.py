import random
print("\nRock-paper-scissor game")
choices=["Rock","Paper","Scissor"]
while True:
    print("\n Rock")
    print("Paper")
    print("Scissor")
    try:
        user_choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please Enter an valid choice")
        continue
    if user_choice<1 or user_choice >3:
        print("Please Enter an valid choice (1 to 3)")
        continue
    use_choice=choices[user_choice-1]
    comp=random.randint(1,3)
    comp_cho=choices[comp-1]
    print("\nYou chose:", use_choice)
    print("Computer chose:", comp_cho)
    if(user_choice==comp):
        print("Game is Tie!")
    elif (user_choice==1 and comp==3) or (user_choice==3 and comp==2) or (user_choice==2 and comp==1):
        print("User wins!")
    else:
        print("Computer wins!")
    while True:
        ans=input("\n Do you want to play again (y/n) : ").lower()
        if ans=='y' or ans =='n':
            break
        print("Please enter an valid option(y or n)")
    if ans=='n':
        print("Thank you for playing!")
        break
    elif ans!='y':
        print("Invalid option. starting an new round")
    

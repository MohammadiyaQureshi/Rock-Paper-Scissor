import random 
print("🎮 Welcome to Rock, Paper, Scissors!")
user_score=0
computer_score=0

options=["rock","paper","scissor"]
while True:
    user_input=input("👉Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input=="q":
     print("\n👋 Thanks for playing! See you next time.")
     break
    if user_input not in options:
        print("⚠️ Invalid input. Try again.")
        continue

    random_number=random.randint(0,2)
    #    rock=0  paper=1   scissor=2
    computer_pick=options[random_number]
    print("💻Computer picked",computer_pick)

    if user_input=="rock" and computer_pick=="scissor":
        print("✅  U Won!")
        user_score+=1

    
    elif user_input=="paper" and computer_pick=="rock":
        print("✅  U Won!")
        user_score+=1

    
    elif user_input=="scissor" and computer_pick=="paper":
        print("✅  U Won!")
        user_score+=1   

    else:
        print("❌  You Lost!....") 
        computer_score+=1   

print("\n📊 Final Score:")
print("🧑 You won",user_score,"times")
print("💻 Computer won",computer_score,"times")
print("🏁 Game Over!")
print("Goodbye!")
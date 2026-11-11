import random
import time
#-----------
print("WELCOME TO ROCK, PAPER, SCISSORS.")
player_score = 0
comp_score = 0
move = 0
text = ""
#--------------
while move != 3:
    player = input("rock, paper, scissors?")
    comp = random.randint(1,3)
    print("------------------")
    if comp == 1:
        comp = "rock"
    elif comp == 2:
        comp = "paper"
    else:
        comp = "scissors"
    print("🙂:"+player)
    print("🤖:"+comp)
    print("------------------")
    time.sleep(1)
    #check
    if player == "rock":
        if comp == "paper":
            text = "You lose!"
            comp_score += 1
        elif comp == "scissors":
            text = "You win 🎉🏆!!"
            player_score += 1
        move += 1
    #-------
    elif player == "paper":
        if comp == "scissors":
            text = "You lose!"
            comp_score += 1
        elif comp == "rock":
            text = "You win 🎉🏆!!"
            player_score += 1
        move += 1
            #--------
    elif player == "scissors":
        if comp == "rock":
            text = "You lose!"
            comp_score += 1
        elif comp == "paper":
            text = "You win 🎉🏆!!"
            player_score += 1
        move += 1
            #----------
    elif comp == player:
        text = "Both win"
    else:
        text = "I don't know this move."
    
    print(move)
    print("🙂:",player_score)
    print("🤖:",comp_score)
    print(text)
    time.sleep(2)
    print("-----------------------")
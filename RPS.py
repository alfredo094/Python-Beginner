
import random
import time
import sys

def play():
    user_choice = input_validation() #Apparently 
    time.sleep(1)
    computer_thoughts = random.choice(["The computer is trying to read your mind for the best answer...", "The computer is attempting to use your hardware to view your movements...",\
                                      "The computer is using new technology to logically deduce your choice..."]) #Brackets are necessary to make lists, commas separate arguments. 
    print(computer_thoughts) 
    time.sleep(5)
    computer_choice = random.choice(['r', 'p', 's']) ## I think the commas here make it so the computer chooses a string at random.

    print (f'You chose {user_choice}. The computer chose {computer_choice}.')

    if user_choice == computer_choice:
        return 'The result is a tie'
    if is_win(user_choice, computer_choice): #This can be called here because Python will read the entire document then do print(play()), by which is_win will exist.\
            #I'm still not sure what exactly the parameters are doing, though. 
            return 'You won!'
    else: # this line is not necessary, since we have already checked for ties and wincons. I'm just including it for clarity. 
        return 'You lost!'

def input_validation(): #I was doing it in the previous function, but decided to separate them for readability and debugging. 
    user_choice = input("What's your choice? Input 'r' for rock, 'p' for paper, 's' for scissors.")
    if user_choice == ({'r','p','s'}):
        return user_choice
    elif True: #Idk why I have to put "true" here
        Attempts = 1
        while user_choice not in {'r', 'p', 's'}: #ChatGPT helped me out here, apparently I need to do strings as well here, also not sure how the "not in" function works. 
            if Attempts in {1, 2}:
                print("Invalid input. Please choose 'r' for rock, 'p' for paper, 's' for scissors.")
                user_choice = input()
                Attempts += 1 
            if Attempts in {3, 4}:
                print("Do you think this is funny? Do a valid input already.")
                user_choice = input()
                Attempts += 1
            if Attempts == 5:
                print("You get one more chance before I go. Just... put the correct input.")
                user_choice = input()
                Attempts += 1
            if Attempts == 6:
                print("All right. Bye, come back when you can follow instructions.")
                raise SystemExit #I'm not sure if this is the most elegant way to close the program
        return user_choice
    
# I am also not sure why these are now separate functions. My guess is that I will call "play" first, it checks for a tie, then call "is_win" afterwards,
# But I am not sure why we wouldn't simply do everything in the same function. 

def is_win(player, opponent): #I'm also not sure what the parameteres are doing here exactly. 
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'): #OR can be used to 
        return True
    

print(play()) 
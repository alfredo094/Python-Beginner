# This program should run so that you get a random madlib and can replay it as many times as you want. 
# This is the greeting that the user should see first. 

print("Answer the prompts for a fun madlib!")

# Going to call the "random" toolbox right away just to have it globally, I'll define how to use it later. 

import random

# Defining all the madlibs before declaring the random functions. 

def madlib1 ():
    adj1 = input("Adjective: ").lower()
    adj2 = input("Another adjective: ").lower()
    verb1 = input ("Now, a verb: ").lower()

    return f"The {adj1} user is {adj2}! He wants to {verb1} to make a better living."

def madlib2 ():
    noun1 = input("Noun: ").lower()
    noun2 = input("Another noun: ").lower()
    famous_person = input("Someone you like:")
    verb1 = input("Action: ").lower()
    
    return f"That {noun1} is trapped inside a {noun2}! {famous_person} is trying to save it, please let them know by {verb1}!"

def madlib3 ():
    family_member = input("Family member (i.e. 'dad'): ").lower()
    activity = input("Activity:").lower()
    reward = input("Reward: ").lower()
    return f"Their {family_member} needs help with {activity}! They will give you {reward} if you lend them a hand."

# Doing the random-choice logic here. 

madlib_list = [madlib1, madlib2, madlib3]

# This is the loop that will allow the user to play as many times as they want

while True:

    chosen_madlib = random.choice(madlib_list)
    print(chosen_madlib())
    # The above loop should give the user their entire madlib. 
    # The below one will ask them to play again. If they choose not to, the program will end. 
    
    while True:

        play_again = input("\nDo you want to madlib again? (y/n)").strip().lower()
        if play_again == "y":
            print("Great! Let's do another one.")
            break
        elif play_again == "n":
            print("Goodbye! Thanks for playing")
            exit()
        else:
            print("Incorrect input, please type 'y' or 'n'.")
                         


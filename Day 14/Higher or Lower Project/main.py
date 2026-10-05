import game_data
import random
import art
"""
-To do, star the game by choosing two random entries in the list and assigining them to variables. 
-Create a comparison function that compares the number of followers which is a specific point of the entry inside of a dictionary
-Receive input from the player to guess whether one is larger or not. 
-If B is great then B becomes A, if A is greater then B becomes A. 
-Probably could do with setting up a while loop that is true so long as Correct is true. 
-Could possibly have it not randomly iterate through but instead catalog which ones have already been 
"""

### Todo-1 choose two random entries in the list and assigning them variables

total_grams = len(game_data.data)
### only assign the whole dictionary to double check
Option_A = game_data.data[random.randint(0,total_grams)]
Option_B = game_data.data[random.randint(0,total_grams)]

### double check random case that two of the same pages were drawn, redraw option_B
if Option_A['name'] == Option_B['name']:
    Option_B = game_data.data[random.randint(0, total_grams)]




#### Todo-2 create comparison function
Still_play = True
score= 0

def comparison(Option_A, Option_B, guess):
    follower_A = Option_A['follower_count']
    follower_B = Option_B['follower_count']
    if follower_A > follower_B and guess == 'A':
        return guess =='A'
    else:
        return guess == 'B'

#### Todo-4 generate a new card always to option_B when called

def new_account():
    Option_B = game_data.data[random.randint(0, total_grams)]
    if Option_A['name']== Option_B['name']:
        Option_B = game_data.data[random.randint(0, total_grams)]
    return Option_B

#### Todo-3 recieve input from player to guess which one is greater and to call the comparison function
def play(Option_A, Option_B, score, Still_play):
    winner = {}
    is_correct = True
    while Still_play == True:
        print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            """)
        print(art.logo)
        if score == 0:
            print("Welcome to Higher Lower")
        else:
            Option_A = winner
            print(f"You're right! Your score is:{score}")
        print(f"Compare A: {Option_A['name']}, a {Option_A['description']} from {Option_A['country']} with {Option_A['follower_count']} million followers")
        print(art.vs)
        print(f"Against B, {Option_B['name']}, a {Option_B['description']} from {Option_B['country']}")
        guess = input("Who has more followers?: Type 'A' or 'B'")

        follower_A = Option_A['follower_count']
        follower_B = Option_B['follower_count']
        print(follower_A)
        print(follower_B)
        is_correct = comparison(Option_A, Option_B, guess)
        if is_correct == True:
            score +=1
            winner = Option_B
        else:
            Still_play = False

        Option_B = new_account()
    else:
        print(f"That is wrong. You're score is {score}")

play(Option_A, Option_B, score, Still_play)

### Todo-5 keep playing while guess=true

#while guess == True:

 #   play(Option_A, score)

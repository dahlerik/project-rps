from random import choice
options = ['r', 'p', 's']
player = input("LEt me record your name!")
score = {player:0, "computer":0}


player_choice = input("Gimme your worst!")
random_choice = choice(options)

#checks who wins
def check_win(player_chocie,random_choice):
    if player_choice == random_choice:
        #results in tie
        print("You tied!")
        return "Tie!"
#MOVE: player chooses 'p'
    elif player_choice == 'p':
 #playr loses
        if random_choice == 's':
            return False
 #player wins
        elif random_choice == 'r':
            return True
#Move: player chooses 'r'
    elif player_choice == 'r':
 #player loses
        if random_choice == 'p':
            return False
 #player wins
        elif random_choice == 's':
            return True
#Move: player chooses 's'
    elif player_choice == 's':
 #player loses
        if random_choice == 'r':
            return False
 #player wins
        elif random_choice == 'p':
            return True
check_win(player_choice,random_choice)

while score[player] < 5 and score['computer'] < 5:
    player_choice = input("Gimme your worst!")
    random_choice = choice(options)
    if player_choice not in ['q', 'r', 's', 'p']:
        print("Not an option, try again.")
        continue
    elif player_choice == 'q':
        break
    elif check_win(player_choice, random_choice) =='Tie!':
        print('Tie!')
        pass
    elif check_win(player_choice, random_choice):
        score[player]+= 1
    else:
        score['computer']+= 1
    print('{}: {} vs. computer: {}'.format(player,score[player],score['computer']))   

from random import choice

class RPS():

    #Class Attribute
    options = ['r', 'p', 's']

    def __init__(self, score = (0,0)):
        self.player = input("LEt me record your name!")
        self.score = {self.player:score[0], 'computer':score[1]}
    
    def player_choice(self):
        return input('Gimme your worst!')
    def random_choice(self):
        return choice(self.options)

    #checks who wins
    def check_win(self,player_choice,random_choice):
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

    def play(self):
        while self.score[self.player] < 5 and self.score['computer'] < 5:
             player_choice = self.player_choice()
             random_choice = self.random_choice()
             if player_choice not in ['q', 'r', 's', 'p']:
                 print("Not an option, try again.")
                 continue
             elif player_choice == 'q':
                 break
             elif self.check_win(player_choice, random_choice) =='Tie!':
                 print('Tie!')
                 pass
             elif self.check_win(player_choice, random_choice):
                 self.score[self.player]+= 1
             else:
                 self.score['computer']+= 1
             print('{}: {} vs. computer: {}'.format(self.player,self.score[self.player],self.score['computer']))   

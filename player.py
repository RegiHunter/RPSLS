import random

class RPSLS:
    def __init__(self):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.player_score = 0
        self.computer_score = 0
        self.rules = {RPSLS.scissors: [RPSLS.lizard, RPSLS.paper],
            RPSLS.paper: [RPSLS.spock, RPSLS.rock],
            RPSLS.rock: [RPSLS.lizard, RPSLS.scissors],
            RPSLS.lizard: [RPSLS.spock, RPSLS.paper],
            RPSLS.spock: [RPSLS.scissors, RPSLS.rock],
        }    
        

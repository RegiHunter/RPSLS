class Player:
    def __init__(self):
        self.name = ''
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.selected_gesture = ''
        self.score = 0

    def enter_name(self):
        self.name = input('Enter player name.')



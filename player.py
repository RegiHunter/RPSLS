class Player:
    def __init__(self):
        self.name = ""

    def select_gesture(self):
        self.selected_gesture = input(f'Select your gesture!: "rock", "paper", "scissors", "lizard", or "spock"?').lower()

    def play_hand(self):
        #Player displays their selected gesture
        if  self.selected_gesture == "rock" :
            print(f'{self.name} has selected {self.selected_gesture}.')
        elif self.selected_gesture == "paper" :
                print(f'{self.name} has selected {self.selected_gesture}.')
        elif self.selected_gesture == "scissors" :
                print(f'{self.name} has selected {self.selected_gesture}.')
        elif self.selected_gesture == "lizard" :
                print(f'{self.name} has selected {self.selected_gesture}.')
        elif self.selected_gesture == "spock" :
                print(f'{self.name} has selected {self.selected_gesture}.')
        else:
            self.select_gesture()
    
  
class Player1(Player) :
    def __init__(self):
        self.name = input("What is your name?")
    def select_gesture(self):
        self.selected_gesture = input(f'Select your gesture!: "rock", "paper", "scissors", "lizard", or "spock"?').lower()

class Player2(Player) :
    def __init__(self):
        self.name = input("What is your name?")
    def select_gesture(self):
        self.selected_gesture = input(f'Select your gesture!: "rock", "paper", "scissors", "lizard", or "spock"?').lower()


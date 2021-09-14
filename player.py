class Player:
    def __init__(self):
        self.name = ""

    def play_hand(self):
        #Player displays their selected gesture
        if Player1.select_gesture() == "rock" :
            selected_gesture = "rock"
            print(f'{self.name} has selected {selected_gesture}.')
        elif Player1.select_gesture() == "paper" :
                selected_gesture = "paper"
                print(f'{self.name} has selected {selected_gesture}.')
        elif Player1.select_gesture() == "scissors" :
                selected_gesture = "scissors"
                print(f'{self.name} has selected {selected_gesture}.')
        elif Player1.select_gesture() == "lizard" :
                selected_gesture = "lizard"
                print(f'{self.name} has selected {selected_gesture}.')
        elif Player1.select_gesture() == "spock" :
                selected_gesture = "spock"
                print(f'{self.name} has selected {selected_gesture}.')
        else:
            Player1.select_gesture()

    def enter_name(self):
        self.name = input('Enter player name.')
    
  
class Player1(Player) :
    def __init__(self):
        self.name = input("What is your name!")
    def select_gesture(self):
        self.selected_gesture = input(f'Select your gesture!: "rock", "paper", "scissors", "lizard", or "spock"?').lower()
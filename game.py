class Game:
    def __init__(self):
        pass
    def choose_gametype(self):
        self.gametype_choice = input("Would you like to play against a 'human' or an 'AI'?")

        human = "human"
        ai = "AI"
        if (self.gametype_choice == human) :
            pass
            # Method to (Human vs. Human) gamemode
        elif (self.gametype_choice == ai) :
            pass
            # Method to (Human vs. AI) gamemode
        else :
            print(self.gametype_choice) 
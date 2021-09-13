class Player:
    def __init__(self):
        self.name = ""

    def play_hand(self):
        #Player displays their selected gesture
        pass

    def enter_name(self):
        self.name = input('Enter player name.')

    def select_gesture(self):
        selected_gesture = input(f'Select your fighter!: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, {self.gestures[4]}').lower()
        if selected_gesture == self.gestures:
            self.selected_gesture = selected_gesture
            print(f'{self.name} has selected {self.selected_gesture}.')
        else:
            self.select_gesture()    
class Warrior:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def info(self):
            print(f" I will not be defeated, My name is {self.name} my power level is {self.power} .")

    def intro_sound(self):
            print("Slash")

class Ninja:
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def info(self):
                print(f" You can't see me, I am the night. {self.name} my power level is {self.power} .")

        def intro_sound(self):
                print("..silence (beware)")

player1 = Warrior("James", 7.9)
player2 = Ninja("Night Stalker", 8.5)

for game in (player1, player2):
    game.intro_sound()
    game.info()

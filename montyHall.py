import random


class MontyHall:

    def __init__(self, nDoors, trials, switch=True):
        self.nDoors = nDoors
        self.trials = trials
        self.switch = switch
        self.wins = 0

    def __create_doors(self):
        doors = [0] * self.nDoors
        car_position = random.randint(0, self.nDoors - 1)
        doors[car_position] = 1  
        return doors

    def calculate_probability(self):
        for i in range(self.trials):
            doors = self.__create_doors()
            cDoor = random.randint(0, self.nDoors - 1)  

            while True:
                open_door = random.randint(0, self.nDoors - 1)
                if open_door != cDoor and doors[open_door] == 0:
                    break

            if self.switch:
                while True:
                    switch_door = random.randint(0, self.nDoors - 1)
                    if switch_door != cDoor and switch_door != open_door:
                        cDoor = switch_door
                        break

            if doors[cDoor] == 1:
                self.wins += 1

        return self.wins / self.trials


nDoors = 3
trials = 10000
switch = False  
game = MontyHall(nDoors, trials, switch)
probability = game.calculate_probability()
print(f"Winning probability: {probability}")

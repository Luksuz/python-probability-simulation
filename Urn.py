import random

class Urn:
    def __init__(self, composition: dict, required, trials):
        self.initial_composition = self.__comp_to_list(composition)
        self.composition = self.initial_composition.copy()
        self.item = required[0]
        self.draws = required[1]
        self.trials = trials
        self.successes = 0

    def __comp_to_list(self, composition):
        comp = []
        for key, value in composition.items():
            for _ in range(value):
                comp.append(key)
        random.shuffle(comp)
        return comp

    def __draw_randomly(self):
        # Draw a random ball from the urn and delete the item from it
        return self.composition.pop(random.randint(0, len(self.composition) - 1))

    def __reset_urn(self):
        self.composition = self.initial_composition.copy()

    def calculate_probability(self):
        for _ in range(self.trials):
            self.__reset_urn()
            count = 0
            for _ in range(self.draws):
                if self.__draw_randomly() == self.item:
                    count += 1
            if count == self.draws:
                self.successes += 1
        probability = self.successes / self.trials * 100
        return str(probability) + "%"

urn = Urn({"red": 4, "blue": 3, "green": 4}, ("red", 2), 100000)
print(urn.calculate_probability())

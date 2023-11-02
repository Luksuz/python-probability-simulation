import random

class DeckOfCards:

    def __init__(self, wantedCards, numberOfDraws, trials):
        self.deck = self.__createDeck()
        self.wantedCards = wantedCards
        self.numberOfDraws = numberOfDraws
        self.trials = trials

    def __createDeck(self):
        suits = ['h', 'd', 's', 'c']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        deck = [rank + suit for suit in suits for rank in ranks]
        return deck

    def calculateProbability(self):
        won = 0
        for _ in range(self.trials):
            current_deck = self.deck.copy()
            random.shuffle(current_deck)
            drawnCards = random.sample(current_deck, self.numberOfDraws)

            if all(card in drawnCards for card in self.wantedCards):
                won += 1

        return str(won / self.trials * 100) + "%"

deck = DeckOfCards(["4h", "4s", "4d", "4c"], 10, 1000)
print(deck.calculateProbability())

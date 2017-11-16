
import random


class Card(object):

    value_names = [None, "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, suit=0, value=2):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}' % (Card.suit_names[self.value],Card.value_names[self.suit])


    def __cmp__(self, other):

        pile1 = self.suit, self.value
        pile2 = other.suit, other.value
        return cmp(pile1, pile2)


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for value in range(1, 14):
                card = Card(suit, value)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, i=-1):

        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):

        for i in range(num):
            hand.add_card(self.pop_card())



if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()


    print Deck()

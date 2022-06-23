import random

class Card:

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):  # human-friendly, concise
        return f"{self.rank}-{self.suit}"

    def __repr__(self):  # code-friendly
        return f"Card({self.rank}, {self.suit})"

class CardDeck:  # inherit constructor from 'object'
    """
    One deck of cards

    deck = Card("dealer name")
    deck.shuffle()
    card = deck.draw()
    """
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = '\u2663', '\u2662', '\u2661', '\u2660'
    DECK_COUNT = 0

    def __init__(self, dealer):  # constructor
        self.dealer = dealer
        CardDeck.DECK_COUNT += 1  # increment CLASS data
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_deck_count(cls):
        return cls.DECK_COUNT

    def __len__(self):
        return len(self._cards)

    def __add__(self, other):
        new_deck = CardDeck(self.dealer)
        new_deck._cards = self._cards + other._cards
        return new_deck


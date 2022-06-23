from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call parent _make_deck()
        for _ in range(2):
            card = Card(None, '\U0001F0CF')
            self._cards.append(card)




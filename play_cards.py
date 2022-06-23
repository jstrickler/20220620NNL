from carddeck import CardDeck, Card
from jokerdeck import JokerDeck

d1 = CardDeck("Betty")
d2 = CardDeck("Lakshmi")
print("d1: {}".format(d1))
print("d2: {}".format(d2))

print("d1.dealer: {}".format(d1.dealer))
print("d2.dealer: {}".format(d2.dealer))

d1.dealer = "Roberto"
print("d1.dealer: {}".format(d1.dealer))

try:
    d1.dealer = 1.234
except TypeError as err:
    print(err)
else:
    print("d1.dealer: {}".format(d1.dealer))


d1.shuffle()
for i in range(5):
    print("d1.draw(): {}".format(d1.draw()))
    
print("d1.cards: {}".format(d1.cards))
x = CardDeck("Mollie")

print("d1.get_deck_count(): {}".format(d1.get_deck_count()))
print("CardDeck.get_deck_count(): {}".format(CardDeck.get_deck_count()))

j = JokerDeck("Jerry")
print("j: {}".format(j))
j.shuffle()
print("j.draw(): {}".format(j.draw()))
print("j.cards: {}".format(j.cards))

print(len(d1), len(d2), len(j))

big_deck = d1 + d2
print("big_deck: {}".format(big_deck))
print("len(big_deck): {}".format(len(big_deck)))

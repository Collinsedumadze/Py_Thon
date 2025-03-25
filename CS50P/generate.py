import random

#choice() function -> choice(sequence)
""" coin = random.choice(['Heads', 'Tails'])
print(coin) """


#randint() function -> randint(a, b)
""" number = random.randint(1, 10)
print(number) """


cards = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
random.shuffle(cards)
for card in cards:
    print(card)
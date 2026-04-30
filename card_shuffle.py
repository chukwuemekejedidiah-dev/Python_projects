import random

def make_deck():
    faces = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    deck = []
    
    for s in suits:
        for f in faces:
            deck.append((f, s))
    
    random.shuffle(deck)
    return deck

def show_deck(deck):
   
    i = 0
    while i < len(deck):
        f, s = deck[i]
        print(f"{f} of {s:<10}", end="\t")
        i += 1
        if i % 4 == 0:
            print()


cards = make_deck()
show_deck(cards)

from itertools import groupby
def is_pair(card_one, card_two):
    return card_one.rank == card_two.rank


class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def some_method(self):
        return self.foo


def is_flush(hand_array):
    for card in range(0,4):
        if hand_array[card].suit != hand_array[card + 1].suit:
            return False
    return True


def get_rank(card):
    return card.rank

def is_straight(hand):
    sorted_hand = sorted(hand, key=get_rank)
    for card in range(0,4):
        if sorted_hand[card].rank != (sorted_hand[card + 1].rank - 1):
            return False    
    return True

def is_handone_high_card(hand_array1, hand_array2):
    hand1 = sorted(hand_array1, key=get_rank)
    hand2 = sorted(hand_array2, key=get_rank)
    if hand1[-1].rank > hand2[-1].rank:
            return True

    return False

def is_three_of_a_kind(hand_array1):
    for key, group in groupby(hand_array1, key=get_rank):
        if len(list(group)) == 3:
            return True

    return False

#! /usr/bin/python
 
from nose.tools import *
from pokerhands.main import *
from array import *
hand
def setup():
     
def test_card_should_have_rank():
    card = Card('S', 5)
    assert_equals(card.rank, 5)


def test_two_cards_same_rank_should_be_pair():
    card_one = Card('S', 2)
    card_two = Card('D', 2)
    assert_true(is_pair(card_one, card_two))

def test_two_cards_dif_rank_shouldnt_be_pair():
    card_one = Card('S', 2)
    card_two = Card('D', 3)
    assert_false(is_pair(card_one, card_two))

def test_hand_is_same_suit():
    hand = [Card('S', 1),Card('S',2),Card('S',3),Card('S',4),Card('S',5)]
    assert_true(is_flush(hand))


def test_hand_last_card_different_suit():
    hand = [Card('S', 1),Card('S',2),Card('S',3),Card('S',4),Card('D',5)]
    assert_false(is_flush(hand))

def test_hand_is_straight_ranks_ordered():
    hand = [Card('S', x) for x in range(4)]
    assert_true(is_straight(hand))

def test_hand_is_straight_ranks_disordered():
    hand = [Card('S', 1),Card('S',2),Card('S',3),Card('S',6),Card('D',5)]
    assert_false(is_straight(hand))

def test_hand_is_straight_cards_unordered():
    hand = [Card('S', 1),Card('S',3),Card('S',2),Card('S',4),Card('D',5)]
    assert_true(is_straight(hand))

def test_which_high_card_is_higher():
    lowerHand = [Card('S', 1),Card('S',3),Card('S',2),Card('S',4),Card('D',5)]
    higherHand = [Card('S', 2),Card('S',3),Card('S',4),Card('S',5),Card('D',6)]
    assert_true(is_handone_high_card(higherHand, lowerHand))

def test_which_high_card_is_higher_false():
    lowerHand = [Card('S', 1),Card('S',3),Card('S',2),Card('S',4),Card('D',5)]
    higherHand2 = [Card('S', 2),Card('S',3),Card('S',4),Card('S',5),Card('D',6)]
    assert_false(is_handone_high_card(lowerHand, higherHand2))

def test_which_high_card_is_higher_false2():
    higher_hand = [Card('S', 10),Card('S',3),Card('S',2),Card('S',4),Card('D',5)]
    lowerHand2 = [Card('S', 2),Card('S',3),Card('S',4),Card('S',5),Card('D',6)]
    assert_true(is_handone_high_card(higher_hand, lowerHand2))

def test_three_of_a_kind():
    hand = [Card('S', 10),Card('D',10),Card('C',10),Card('S',4),Card('D',5)]
    assert_true(is_three_of_a_kind(hand))

def test_not_three_of_a_kind():
    hand = [Card('S', 9),Card('D',10),Card('C',10),Card('S',4),Card('D',5)]
    assert_false(is_three_of_a_kind(hand))
def test_four_of_a_kind():

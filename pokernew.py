#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:33:44 2018

@author: kpit
"""
import itertools
import random
import time
import pandas as pd
print("*********************POKER**************************")
print("\n")
print("\n")
print("\n")
SR = input("For registration enter 1. For login enter any number except 1:")
print(SR)
if SR == '1' :
    print(9)
    c=int(0)
    USER_LOGIN = input("new_user:")
    PASSWORD_LOGIN = input("set_password:")
    NEW_LIST=[USER_LOGIN, PASSWORD_LOGIN,c]                                                                                 
    FL_DF = pd.DataFrame(NEW_LIST)
    FL_DF.to_csv(
        '/home/kpit/Documents/poker_/pokeruser.csv',
        mode='a',
        encoding='utf-8',
        sep=',',
        index=False,
        header=False,
    )
DF = pd.read_csv('/home/kpit/Documents/poker_/pokeruser.csv',
        sep=',',
        header=0)
DF = DF.set_index('USERNAME')
USER = input("user_name:")
while 1:
    if USER not in DF.index:
        print("invalid user name")
        USER = input("user_name:")
    else:
        break
PASSWORD = DF.at[USER, 'PASSWORD']
if input('Password:') == str(PASSWORD):
    DF.at[USER, 'COUNT'] += 1
    DF.to_csv("pokeruser.csv")
    print("play")
DECK = list(itertools.product(range(1, 14), ['S', 'H', 'D', 'C']))
CARDS_PLAYER1 = []
CARDS_PLAYER2 = []
random.shuffle(DECK)
print(DECK)
time.sleep(2)
print("\n")
print("\n")
print("player1 got:")
for var2 in range(3):
    CARDS_PLAYER1.append(DECK[var2])
    print(DECK[var2][0], "of", DECK[var2][1])
print("\n")
print("\n")
time.sleep(2)
#print("player2 got:")
for var1 in range(3):
    CARDS_PLAYER2.append(DECK[len(DECK)-1-var1])
#    print(DECK[len(DECK)-1-var1][0], "of", DECK[len(DECK)-1-var1][1])

print("cards on board:")
for var3 in range(2):
    CARDS_PLAYER1.append(DECK[var3+10])
    CARDS_PLAYER2.append(DECK[var3+10])
    print(DECK[var3 + 10][0], "of", DECK[var3 + 10][1])
print("\n")
print("\n")
print(CARDS_PLAYER1)
print("\n")
COUNT = 0
AMT = 2500

while COUNT < 5:
    AMT1 = int(input("PLAYER1 BID:"))
    print("COMPUTER BID: {}".format(AMT1 + 500))
    AMT = AMT + AMT1
    COUNT = COUNT + 1
print("\n")

def royal_flush(player_cards):
    '''royal flush case'''
    card_value = []
    card_suit = []
    for var5, _ in enumerate(player_cards):
        card_value.append(player_cards[var5][0])
        card_suit.append(player_cards[var5][1])
    num = card_suit.count(card_suit[0])
    if num == 5:
        for sid in range(10, 15):
            if sid in card_value:
                continue
        return True
    return False

def flush(player_cards):
    '''flush case'''
    card_suit = []
    for var6, _ in enumerate(player_cards):
        card_suit.append(player_cards[var6][1])
    current_suit = card_suit[0]
    for card in card_suit:
        if card != current_suit:
            return False
        current_suit = card
    return True


def four_of_a_kind(player_cards):
    '''four of a kind case'''
    card_value = []
    for var7, _ in enumerate(player_cards):
        card_value.append(player_cards[var7][0])
    c_f_c = card_value.count(card_value[0])
    c_s_c = card_value.count(card_value[1])
    if c_f_c == 4 | c_s_c == 4:
        return True
    return False

def three_of_a_kind(player_cards):
    '''three of a kind case'''
    card_value = []
    for var8, _ in enumerate(player_cards):
        card_value.append(player_cards[var8][0])
    c_f_c1 = card_value.count(card_value[0])
    c_s_c1 = card_value.count(card_value[1])
    if c_f_c1 == 3 | c_s_c1 == 3:
        return True
    return False

def straight(player_cards):
    '''straight case'''
    cardv = []
    for var9, _ in enumerate(player_cards):
        cardv.append(player_cards[var9][0])
    sma = min(cardv)
    if sma == 10 and (sma + 1 in cardv) and (sma + 2 in cardv):
        return True
    return False
def fullhouse(player_cards):
    '''fullhouse case'''
    card_value = []
    for var10, _ in enumerate(player_cards):
        card_value.append(player_cards[var10][0])
    card_value.sort()
    c_o_c = card_value.count(card_value[0])
    c_t_c = card_value.count(card_value[len(card_value) - 1])
    if (c_o_c == 2 and c_t_c == 3) or (c_o_c == 3 and c_t_c == 2):
        return True
    return False

def two_pair(player_cards):
    '''two pair case'''
    card_value = []
    for var11, _ in enumerate(player_cards):
        card_value.append(player_cards[var11][0])
    cf2 = card_value.count(card_value[0])
    cs2 = card_value.count(card_value[4])
    ct2 = card_value.count(card_value[2])
    if(cf2 == 2 and cs2 == 2) or (cf2 == 2 and ct2 == 2) or (cs2 == 2 and ct2 == 2):
        return True
    return False


def get_score(player_cards):
    '''get total score'''
    score = 0
    if royal_flush(player_cards):
        score = 400
    elif flush(player_cards) and straight(player_cards):
        score = 350
    elif four_of_a_kind(player_cards):
        score = 300
    elif fullhouse(player_cards):
        score = 250
    elif flush(player_cards):
        score = 200
    elif straight(player_cards):
        score = 150
    elif three_of_a_kind(player_cards):
        score = 100
    elif two_pair(player_cards):
        score = 50
    else:
        score = 10
    return score
time.sleep(2)
print("\n")
print(CARDS_PLAYER2)
print("\n")
PLAYER_1 = get_score(CARDS_PLAYER1)
PLAYER_2 = get_score(CARDS_PLAYER2)
print(PLAYER_1)
print("\n")
time.sleep(2)
print(PLAYER_2)

if PLAYER_1 > PLAYER_2:
    print("PLAYER1 WINS: {}".format(AMT))
elif PLAYER_2 > PLAYER_1:
    print("COMPUTER WINS: {}".format(AMT))
else:
    print("DUTCH THE AMOUNT")

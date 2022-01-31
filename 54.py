def dict_invert(d: dict) -> dict:
    return dict((v, k) for k,v in d.items())


# card[0] = value, card[1] = suit

def rank_compare(r1: int, r2: int) -> int:
    if r1 > r2:
        return 1
    elif r2 > r1:
        return 2
    else:
        return 0

def get_val(card: str) -> int:
    if card[0] == 'A':
        return 14
    elif card[0] == 'K':
        return 13
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'J':
        return 11
    elif card[0] == 'T':
        return 10
    else:
        return int(card[0])

# returns hand with all cards of value val removed
def remove_val(hand: list, val: int) -> list:
    newhand = []
    for card in hand:
        if not get_val(card) == val:
            newhand.append(card)
    return newhand

# returns a dictionary mapping card rank values to the number of times they appear in hand
def occurences(hand: list) -> dict:
    occ = dict()
    for card in hand:
        occ.setdefault(card[0], 0)
        occ[card[0]] += 1
    return occ

def card_vals(hand: list) -> list:
    vals = []
    for card in hand:
        vals.append(get_val(card[0]))
    return vals

def resolve_tie(hand1: list, hand2: list) -> int:
    if len(hand1) != len(hand2):
        print("hands are different length:", hand1, hand2)
        exit(1)
    vals1 = card_vals(hand1)
    vals2 = card_vals(hand2)
    vals1.sort(reverse=True)
    vals2.sort(reverse=True)
    for i in range(len(hand1)):
        if vals1[i] > vals2[i]:
            return 1
        elif vals1[i] < vals2[i]:
            return 2
        else: 
            continue
    print(hand1, hand2, "hands were equal!")
    exit(1)

def high_card(hand: list) -> int:
    high = 0
    for card in hand:
        high = max(high, get_val(card))

# if there are 'num' of a kind in 'hand', return that card which occurs 'num' times
# else return false
def of_a_kind(hand: list, num: int) -> int:
    try:
        return dict_invert(occurences(hand))[num]
    except:
        return 0

def pair(hand: list) -> int:
    return of_a_kind(hand, 2)

# given that hand1, hand2 have a two pair, return the winning hand
def resolve_two_pair(hand1: list, hand2: list) -> int:
    print("tie???", hand1, hand2)
    exit(1)

def two_pair(hand: list) -> bool:
    return list(occurences(hand).values()).count(2) == 2 

def three_kind(hand: list) -> int:
    return of_a_kind(hand, 3)

def straight(hand: list) -> bool:
    vals = list(map(get_val, hand))
    vals.sort()
    for i in range(4):
        if vals[i+1] - vals[i] != 1:
            return False
    return True

def flush(hand: list) -> bool:
    suit = hand[0][1]
    for card in hand:
        if suit != card[1]:
            return False
    return True

def full_house(hand: list) -> bool:
    occ = occurences(hand)
    return 2 in occ.values() and 3 in occ.values()

def four_kind(hand: list) -> int:
    return of_a_kind(hand, 4)

def straight_flush(hand: list) -> bool:
    return straight(hand) and flush(hand)

def royal_flush(hand: list) -> bool:
    return straight_flush(hand) and high_card(hand) == 14
    
def check_tie(hand1: list, hand2: list, f):
    if f(hand1) and f(hand2):
        if f == straight_flush:
            return resolve_tie(hand1, hand2)
        elif f == four_kind:
            h1 = dict_invert(occurences(hand1))
            h2 = dict_invert(occurences(hand2))
            t = rank_compare(get_val(h1[4]), get_val(h2[4]))
            if t != 0:
                return t
            else:
                return rank_compare(get_val(h1[1]), get_val(h2[1]))
        elif f == full_house:
            h1 = dict_invert(occurences(hand1))
            h2 = dict_invert(occurences(hand2))
            t = rank_compare(get_val(h1[3]), get_val(h2[3]))
            if t != 0:
                return t
            else:
                return rank_compare(get_val(h1[2]), get_val(h2[2]))
        elif f == flush:
            return resolve_tie(hand1, hand2)
        elif f == straight:
            return resolve_tie(hand1, hand2)
        elif f == three_kind:
            t = rank_compare(get_val(three_kind(hand1)), get_val(three_kind(hand2)))
            if t != 0:
                return t
            else:
                hand1 = remove_val(hand1, three_kind(hand1))
                hand2 = remove_val(hand2, three_kind(hand2))
                return resolve_tie(hand1, hand2)
        elif f == two_pair:
            return resolve_two_pair(hand1, hand2)
        elif f == pair:
            t = rank_compare(get_val(pair(hand1)), get_val(pair(hand2)))
            if t != 0:
                return t
            else:
                hand1 = remove_val(hand1, pair(hand1))
                hand2 = remove_val(hand2, pair(hand2))
                return resolve_tie(hand1, hand2)
        else:
            print("how did you get here?", hand1, hand2, f)
            exit(1)
    elif f(hand1):
        return 1
    elif f(hand2):
        return 2
    else:
        return 0

def winner(hand1: list, hand2: list):
    t = check_tie(hand1, hand2, royal_flush)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, straight_flush)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, four_kind)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, full_house)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, flush)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, straight)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, three_kind)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, two_pair)
    if t > 0:
        return t
    t = check_tie(hand1, hand2, pair)
    if t > 0:
        return t
    return resolve_tie(hand1, hand2)



p1wins = 0
for line in open("54_poker.txt").readlines():
    cards = line.split()
    hand1 = cards[:5]
    hand2 = cards[5:10]
    if winner(hand1, hand2) == 1:
        p1wins += 1
print(p1wins)
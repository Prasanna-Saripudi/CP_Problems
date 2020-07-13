# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().
# author: Prasanna Saripudi

def handtodice(hand):
    # converting dat as string to access numbers
    # hand = str(hand)
    # return (int(hand[0]), int(hand[1]), int(hand[2]))
    temp = 0
    result = []
    while temp < 3:
        result.append(hand//10**temp % 10)
        temp += 1
    return tuple(result)

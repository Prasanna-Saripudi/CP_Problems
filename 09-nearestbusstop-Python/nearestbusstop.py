# Write the function nearestBusStop(street) that takes a
# non-negative int street number, and returns the nearest
# bus stop to the given street, where buses stop every 8th street,
# including street 0, and ties go to the lower street,
# so the nearest bus stop to 12th street is 8th street,
# and the nearest bus stop to 13 street is 16th street.
# author: Prasanna Saripudi


def fun_nearestbusstop(street):
    value = street % 8
    # checking if tie
    if value == 4:
        return street - 4
    # if closest to lower street
    elif value < 4:
        return street - value
    # if closest to upper street
    return street + 8 - value

def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out

    # Alternate phrasing: a bit clever, same runtime, and harder to
    # read:

    # to_swap = to_swap.lower()
    #
    # fixed = [
    #     (char.swapcase() if char.lower() == to_swap else char)
    #     for char in phrase
    # ]
    #
    # return "".join(fixed)

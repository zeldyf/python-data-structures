def freq_counter(coll):

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts


def same_frequency(num1, num2):

    return freq_counter(str(num1)) == freq_counter(str(num2))

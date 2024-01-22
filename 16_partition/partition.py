def partition(lst, fn):

    # Best solution:

    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)

    return [true_list, false_list]

    # Clever, but less optimal solution --- this runs fn() twice on each element,
    # not once:
    #
    # return [
    #     [val for val in lst if fn(val)],
    #     [val for val in lst if not fn(val)]
    # ]

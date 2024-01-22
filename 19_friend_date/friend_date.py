def friend_date(a, b):

    if set(a[2]) & set(b[2]):
        return True
    else:
        return False

    # can even do by converting to boolean!
    #
    # return bool(set(a[2] & set(b[2])
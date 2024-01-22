def truncate(phrase, n):

    if n < 3:
        return "Truncation must be at least 3 characters."

    if n > len(phrase) + 2:
        return phrase

    return phrase[:n - 3] + "..."

def includes(collection, sought, start=None):

    if isinstance(collection, dict):
        return sought in collection.values()

    if start is None or isinstance(collection, set):
        return sought in collection

    return sought in collection[start:]

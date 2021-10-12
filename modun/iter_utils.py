import itertools


def _cycle(iterable):
    """
    Method to create a generator from an iterable. It keeps the
    current position of the iterable in memory.  Each time the
    next() method for the iterable is called, it will return the
    next item.  If there are no more items, it will cycle to the
    first item.
    """

    yield from itertools.cycle(iterable)


def chunks(lst, n):
    """
    Yield successive n-sized chunks from lst.
    Taken from https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

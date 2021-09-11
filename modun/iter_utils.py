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

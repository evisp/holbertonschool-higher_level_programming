class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        try:
            next_item = next(self._iterator)
            self._count += 1
            return next_item
        except StopIteration:
            raise

    def get_count(self):
        return self._count
    
from store import Store


class Shop(Store):

    def __init__(self, items, capacity=20, name=''):
        super().__init__(items, capacity, name)

    def add(self, title: str, amount: int):
        if self._capacity >= amount and len(self._items.keys()) < 5:
            self._capacity = self._capacity - amount
            self._items[title] = amount
            return None
        else:
            return 'Free space is over'

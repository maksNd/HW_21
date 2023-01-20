from store import Store


class Shop(Store):
    name = 'магазин'

    def __init__(self, items={}, capacity=20):
        super().__init__(items, capacity)

    def __repr__(self):
        return 'магазин'

    def __eq__(self, other):
        return Shop.name == other

    def add(self, title: str, amount: int):
        if self._capacity >= amount and len(self._items.keys()) < 5:
            self._capacity = self._capacity - amount
            self._items[title] = amount
            return None
        else:
            return 'Free space is over'

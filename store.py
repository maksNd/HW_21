from abstract_Storage import Storage


class Store(Storage):

    def __init__(self, items=None, capacity=100, name=''):
        if items is None:
            self._items = {}
        else:
            self._items = items
        self._capacity = capacity
        self._name = name

    def __repr__(self):
        return self._name

    def __eq__(self, other):
        return self._name == other

    def check_availability(self, title, amount):
        for item in self._items:
            if item.lower() == title:
                if self._items[item] >= amount:
                    return True
        return False

    def capacity(self):
        pass

    def items(self):
        pass

    def get_items(self):
        result = ''
        for title, amount in self._items.items():
            result += f'\n{title} - {amount}'
        return result

    def get_free_space(self):
        return self._capacity

    def add(self, title: str, amount: int):
        if self._capacity >= amount:
            self._capacity = self._capacity - amount
            self._items[title] = amount
            return None
        else:
            return 'Free space is over'

    def remove(self, title, amount):
        for item, stored_amount in self._items.items():
            if item.lower() == title.lower() and self._items[item] >= amount:
                self._items[item] = self._items[item] - amount
                return {title: amount}
        print('Not enough goods')

    def get_unique_items_count(self):
        result = []
        for item in self._items.keys():
            if item not in result:
                result.append(item)
        return result

from abc import ABC


class Storage(ABC):

    def __int__(self, items, capacity):
        self._items = items
        self._capacity = capacity


    def add(self, name, count):
        if count < self._capacity:
            if self._capacity - count > 0:
                if name in self._items:
                    self._items[name] += count
                    self._capacity -= count
                else:
                    self._items[name] = count
                    self._capacity -= count

    def add_initial_values(self, name, count):
        self._items[name] = count
        self._capacity -= count


    def remove(self, name, count):
        if name in self._items:
            if self._items[name] >= count:
                if self._items[name] - count > 0:
                    self._items[name] -= count
                    return True
                elif self._items[name] - count == 0:
                    del self._items[name]
                    return True
            else:
                return False
        else:
            return False

    def get_free_space(self):
        """
        :return:вернуть количество свободных мест
        """
        return self._capacity



    def get_items(self):
        """
        :return: возвращает содержание склада в словаре {товар: количество}
        """
        for i in self._items:
            print(f'{i}  {self._items[i]}')

    def get_unique_items_count(self):
        """
        :return: возвращает количество уникальных товаров.
        """
        return len(self._items)



class Store(Storage):

    def __init__(self,  items, capacity=100):
        self._items = items
        self._capacity = capacity
        for k, v in self._items.items():
            self.add_initial_values(k, v)

    def add(self, name, count):
        if self.get_free_space() > count:
            super().add(name, count)
            return True
        else:
            return False

class Shop(Storage):
    def __init__(self, items, capacity=20):
        self._items = items
        self._capacity = capacity
        for k, v in self._items.items():
            self.add_initial_values(k, v)

    def add(self, name, count):
        if self.get_unique_items_count() < 5 and self.get_free_space() > count:
            super().add(name, count)
            return True
        else:
            return False


class Request:
    def __init__(self, from_where, to, amount, product):
        self.from_where = from_where
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_where} в {self.to}'



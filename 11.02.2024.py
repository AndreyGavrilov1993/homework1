### реализовать методы
### d.get() - найти элемент по ключу
### d.pop() - удалить элемент по ключу
### d.clear() - очистить словарь
from collections import deque
class Node(dict):
    def __int__(self, k, v):
        self.k = k
        self.v = v

    def __str__(self):
        return f"value: {self.v}"

class MyDict:

    def __init__(self):
        self.lst = [None for _ in range(10)]
        self.size = 0

    def add(self, k, v):
        index: int = hash(k) % len(self.lst)


        if self.lst[index] is None:
            self.lst[index] = Node(k=k, v=v)
            return
        if isinstance(self.lst[index], deque):
            for item in self.lst[index]:
                if item.k == k:
                    item.v = v
                    return
                self.lst[index].append(Node(k=k, v=v))
                return

        if self.lst[index].k == k:
            self.lst[index].v = v
            return

        temp_lst = deque()
        temp_lst.append(self.lst[index])
        temp_lst.append(Node(k=k, v=v))
        self.lst[index] = temp_lst

    def __str__(self):
        print_list = []
        for i in self.list:
            if i is None:
                continue
            print_list.append(i)
        return str(print_list)

    def get(self, k):
        index: int = hash(k) % len(self.lst)
        if self.lst[index] is None:
            raise KeyError("")

        if isinstance(self.lst[index], Node) and self.lst[index].k == k:
            return self.lst[index].v

        for node in self.lst[index].k:
            if node.k == k:
                return node.v
        return None

    def pop(self, k):
        index: int = hash(k) % len(self.lst)

        if self.lst[index] is None:
            raise  Exception
        if len(self.lst) == 0:
            return None
        removed = self.lst.pop()
        return removed


        #  if self.lst[index].k == k:
        #      self.lst.pop(__index=k)
        #     return  self.lst
        # if isinstance(self.lst[index], Node):
        #     is self.lst[index].k == k:
        #     self.lst[index] = None
        #     self.size -= 1
        #     return  True
        # else:
        #     raise  KeyError("")
        #
        # for node is self.lst[index]:
        #     if node[k] == k:
        #     raise KeyError

    def clear(self):
        self.lst = [None]
        return self.lst

d = MyDict()
# d.add(5, 100)
# d.add("name", "Ivan")
# a = d.get(5)
# print(a, type(a))
# print(d)
# d.pop(5)
# print(d)
# d.clear()
# print(d)
# d.add(1, 100000)
# print(d)

d.add(5, 100)
d.add(55, 999)

print(d.get(55))
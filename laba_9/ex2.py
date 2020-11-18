class Node:
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.l = l
        self.r = r

    def insert(self, data):
        if self.value > data:
            if self.l is None:
                self.l = Node(data)
            else:
                self.l.insert(data)
        else:
            if self.r is None:
                self.r = Node(data)
            else:
                self.r.insert(data)

    def show(self):
        if self.l is not None:
            self.l.show()
        print(self.value)
        if self.r is not None:
            self.r.show()

    def get_value(self):
        return self.value

    def get_l(self):
        return self.l

    def get_r(self):
        return self.r


class BinTree:
    def __init__(self):
        self.root = None
        self.length = 0
        self.queue = []

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def show(self):
        if self.root is not None:
            self.root.show()

    def __iter__(self):
        if self.root is None:
            return self
        self.queue = [self.root]
        while self.queue[0].l is not None:
            self.queue.insert(0, self.queue[0].l)
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration()
        val = self.queue[0].get_value()
        if self.queue[0].r is not None:
            self.queue[0] = self.queue[0].r
            while self.queue[0].l is not None:
                self.queue.insert(0, self.queue[0].l)
        else:
            self.queue.pop(0)
        return val


bt = BinTree()
bt.add(5)
bt.add(1)
bt.add(4)
bt.add(9)
bt.add(10)
bt.add(1)
bt.add(2)
bt.add(6)
bt.add(3)
bt.add(8)
for i in bt:
    print(i)
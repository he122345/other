class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def LENGTH(self):
        q = self.head
        count = 1
        if q is None:
            return 0
        elif q.next is None:
            return 1
        else:

            while q.next is not None:
                q = q.next
                count += 1
            return count

    def PUSH_FRONT(self, x):  # 1
        node = Node(x)
        node.next = self.head
        if self.head is not None:
            self.head.pre = node
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def POP_FRONT(self):  # 1
        if self.LENGTH() <= 1:
            self.head = None
            self.tail = None
        else:
            p = self.head
            self.head = self.head.next
            self.head.pre = None
            del p

    def PUSH_BACK(self, x):  # 1
        node = Node(x)
        if self.tail is not None:
            self.tail.next = node
            node.pre = self.tail
        self.tail = node
        if self.head is None:
            self.head = self.tail

    def POP_BACK(self):  # 1
        if self.LENGTH() <= 1:
            self.head = None
            self.tail = None
        else:
            p = self.tail
            self.tail = p.pre
            self.tail.next = None
            del p

    def INSERT(self, index, x):  # 1
        if index == 0:
            self.PUSH_FRONT(x)

        elif index == self.LENGTH():
            self.PUSH_BACK(x)
        else:
            q = self.head
            for i in range(index - 1):
                q = q.next
            node = Node(x)
            node.next = q.next
            q.next.pre = node
            q.next = node
            node.pre = q

    def CONTAIONS(self, x):  # 1
        q = self.head
        while q is not None:
            if q.item == x:
                return True
            q = q.next
        return False

    def REMOVE(self, x):
        q = self.head
        if q is None:
            return
        elif self.LENGTH() == 1:
            if q.item == x:
                self.POP_FRONT()
            else:
                return
        elif q.item == x:
            self.POP_FRONT()
        while q.next is not None:
            if q.next.item == x:
                node = q.next
                q.next = q.next.next
                del node
            else:
                if q.next is not None:
                    q = q.next
                else:
                    return

    def REVERSE(self):  # 1
        p = self.head
        q = p
        if p is None:
            return
        while 1:
            s = p.pre
            p.pre = p.next
            p.next = s
            if p.pre is None:
                break
            p = p.pre
        self.head = self.tail
        self.tail = q

    def FOR_EACH(self):
        q = self.head
        if q is None:
            print()
        elif q.next is None:
            print(q.item,"123")
        else:
            while q.next is not None:
                print(q.item, end=" ")
                q = q.next
            print(q.item,"for_each")

    def VISIT(self, x, k):
        q = self.head
        n = 0
        if q is None or not self.CONTAIONS(x):
            print()
            return
        elif q.item == x:
            n = 0
        else:
            while q.next is not None:
                if q.next.item == x:
                    q = q.next
                    n += 1
                    break
                q = q.next
                n += 1
        a, b = q, q
        for i in range(min(int(k), n)):
            a = a.pre
        for i in range(min(self.LENGTH() - 1, int(k))):
            b = b.next
        while 1:
            if a == b:
                print(a.item,"visit")
                break
            print(a.item, end=" ")


def min(a, b):
    if a < b:
        return a
    else:
        return b


def switch(sw, link):
    if sw[0] == "PUSH_FRONT":
        link.PUSH_FRONT(int(sw[1]))
    elif sw[0] == "POP_FRONT":
        link.POP_FRONT()
    elif sw[0] == "POP_BACK":
        link.POP_BACK()
    elif sw[0] == "PUSH_BACK":
        link.PUSH_BACK(int(sw[1]))
    elif sw[0] == "INSERT":
        link.INSERT(int(sw[1]), int(sw[2]))
    elif sw[0] == "CONTAINS":
        if link.CONTAIONS(int(sw[1])) is True:
            print("true")
        else:
            print("false")
    elif sw[0] == "REMOVE":
        link.REMOVE(int(sw[1]))
    elif sw[0] == "REVERSE":
        link.REVERSE()
    elif sw[0] == "FOR_EACH":
        link.FOR_EACH()
    elif sw[0] == "VISIT":
        link.VISIT(int(sw[1]), int(sw[2]))
    else:
        return False


if __name__ == "__main__":
    link = LinkList()
    num = input()
    for i in range(int(num)):
        take = list(input().split())
        switch(take, link)

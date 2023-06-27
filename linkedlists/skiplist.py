from math import inf
from random import random

class SkiplistNode:
    def __init__(self, val=-inf, nxt=None, dwn=None):
        self.val = val
        self.nxt = nxt
        self.dwn = dwn

class Skiplist:

    def __init__(self):
        self.levels = [SkiplistNode()]
        self.head = self.levels[0]

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.nxt and curr.nxt.val < target:
                curr = curr.nxt
            if curr.nxt and curr.nxt.val == target:
                return True
            curr = curr.dwn
        return False

    def add(self, num: int) -> None:
        curr = self.head
        path = []
        while curr:
            while curr.nxt and curr.nxt.val < num:
                curr = curr.nxt
            path.append(curr)
            curr = curr.dwn
        insert = True
        down = None
        while insert and path:
            curr = path.pop()
            curr.nxt = SkiplistNode(num, curr.nxt, down)
            down = curr.nxt
            insert = (random() < 0.5)
        if insert:
            self.head = SkiplistNode(-inf, None, self.head)
            self.head.nxt = SkiplistNode(num, None, down)

    def erase(self, num: int) -> bool:
        curr = self.head
        path = []
        while curr:
            while curr.nxt and curr.nxt.val < num:
                curr = curr.nxt
            path.append(curr)
            curr = curr.dwn
        found = False
        while path:
            curr = path.pop()
            if curr.nxt and curr.nxt.val == num:
                curr.nxt = curr.nxt.nxt
                found = True
        return found
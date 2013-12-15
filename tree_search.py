from collections import deque


def search(node, goal_fn, container):
    """ Search abstraction """
    container.add(node)
    while container.has_items():
        val = container.get()
        if goal_fn(val):
            return True
        else:
            for k in val.successors:
                container.add(k)
    return False


def dfs(root, goal_fn):
    """ Depth First Search """
    return search(root, goal_fn, DS_Stack())


def bfs(root, goal_fn):
    """ Breadth First Search """
    return search(root, goal_fn, DS_Queue())


class DS_Stack:
    """ Stack data structue """
    def __init__(self):
        self.vals = []
    def get(self):
        return self.vals.pop()
    def add(self, value):
        self.vals.append(value)
    def has_items(self):
        return bool(self.vals)


class DS_Queue:
    """ Queue data structure """
    def __init__(self):
        self.vals = deque()
    def get(self):
        return self.vals.popleft()
    def add(self, value):
        self.vals.append(value)
    def has_items(self):
        return bool(self.vals)


class Tree:
    """ Tree data structure """
    def __init__(self, value):
        self.value = value
        self.successors = []
    def add_successor(self, tree):
        self.successors.append(tree)
        return self


# Tests

def test_tree():
    t = (Tree(5).add_successor(Tree(3).add_successor(Tree(8)).add_successor(Tree(7)))
                .add_successor(Tree(2).add_successor(Tree(6)).add_successor(Tree(9)))
         )
    assert(t.value == 5)
    assert(len(t.successors) == 2)
    assert(t.successors[0].value == 3)
    assert(t.successors[1].value == 2)


def test_dfs():
    t = (Tree(5).add_successor(Tree(3).add_successor(Tree(8)).add_successor(Tree(7)))
                .add_successor(Tree(2).add_successor(Tree(6)).add_successor(Tree(9)))
         )
    assert(dfs(t, lambda x: x.value == 9) == True)
    assert(dfs(t, lambda x: x.value == 10) == False)


def test_bfs():
    t = (Tree(5).add_successor(Tree(3).add_successor(Tree(8)).add_successor(Tree(7)))
                .add_successor(Tree(2).add_successor(Tree(6)).add_successor(Tree(9)))
         )
    assert(bfs(t, lambda x: x.value == 9) == True)
    assert(bfs(t, lambda x: x.value == 10) == False)


if __name__ == '__main__':
    test_tree()
    test_dfs()
    test_bfs()

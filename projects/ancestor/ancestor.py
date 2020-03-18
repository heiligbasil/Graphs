import operator


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    """Find and return the earliest ancestor (DFT to the deepest node)"""
    s = Stack()
    depth = 0
    s.push({starting_node: depth})
    visited = dict()
    while s.size() > 0:
        depth += 1
        vk, vv = s.pop().popitem()
        if vk not in visited.keys():
            visited[vk] = vv
            for p, c in ancestors:
                if c == vk:
                    s.push({p: depth})
    if len(visited) == 1:
        return -1
    else:
        earliest_ancestors = []
        max_depth = 0
        for d in sorted(visited.items(), key=operator.itemgetter(1), reverse=True):
            max_depth = max(max_depth, d[1])
            if d[1] == max_depth:
                earliest_ancestors.append(d[0])
        return min(earliest_ancestors)


class Ancestor:
    def __init__(self):
        self.persons = {}

    def add_person(self, person):
        self.persons[person] = set()

    def add_line(self, parent, child):
        if parent in self.persons and child in self.persons:
            self.persons[child].add(parent)
        else:
            raise ValueError(f"Person '{parent}' and/or '{child}' do not exist")

    def get_relatives(self, person):
        if person in self.persons:
            return self.persons[person]
        else:
            raise ValueError(f"Person '{person}' doesn't exist")

    def earliest_ancestor_recursive(self, child_depth, visited=None, depth=0):
        if visited is None:
            visited = dict()
        vk, vv = child_depth.popitem()
        if vv == 0 and len(self.get_relatives(vk)) == 0:
            return -1
        elif vk not in visited.keys():
            visited[vk] = vv
            depth += 1
            for p in self.get_relatives(vk):
                self.earliest_ancestor_recursive({p: depth}, visited, depth)
            earliest_ancestors = []
            max_depth = 0
            for d in sorted(visited.items(), key=operator.itemgetter(1), reverse=True):
                max_depth = max(max_depth, d[1])
                if d[1] == max_depth:
                    earliest_ancestors.append(d[0])
            return min(earliest_ancestors)


if __name__ == '__main__':
    ancestor_list = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(ancestor_list, 6)

    a = Ancestor()
    a.add_person(1)
    a.add_person(2)
    a.add_person(3)
    a.add_person(4)
    a.add_person(5)
    a.add_person(6)
    a.add_person(7)
    a.add_person(8)
    a.add_person(9)
    a.add_person(10)
    a.add_person(11)
    a.add_line(1, 3)
    a.add_line(2, 3)
    a.add_line(3, 6)
    a.add_line(5, 6)
    a.add_line(5, 7)
    a.add_line(4, 5)
    a.add_line(4, 8)
    a.add_line(8, 9)
    a.add_line(11, 8)
    a.add_line(10, 1)
    print(a.earliest_ancestor_recursive({11: 0}))

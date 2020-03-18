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


if __name__ == '__main__':
    ancestor_list = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(ancestor_list, 9)

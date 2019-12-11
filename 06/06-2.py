class Tree(object):

    def __init__(self, data, parent = None):
        self.parent = parent
        self.children = None
        self.data = data

    def findNode(self, node):
        if self.data == node:
            return self
        elif self.children is not None:
            for child in self.children:
                find = child.findNode(node)
                if find is not None:
                    return find
        else:
            return

    def appendNode(self, node):
        if self.children is None:
            self.children = []
        self.children.append(node)
        return

    def print(self):
        if self.children is None:
            return self.data
        children = []
        for child in self.children:
            children.append(child.print())
        return [self.data, children]

    def getNumberOfOrbits(self):
        if self.parent is None:
            return 0
        return 1 + self.parent.getNumberOfOrbits()

    def getNumberOfOrbitsRec(self):
        if self.children is None:
            return self.getNumberOfOrbits()
        number = self.getNumberOfOrbits()
        for child in self.children:
            number += child.getNumberOfOrbitsRec()
        return number

    def isDescendantOf(self, node):
        while self.parent is not None:
            if self.parent.data == node.data:
                return True
            return self.parent.isDescendantOf(node)
        return False

    def findClosestCommonParent(self, node):
        if self.isDescendantOf(node):
            return node
        if node.isDescendantOf(self):
            return self
        return self.parent.findClosestCommonParent(node)

    def findNumberOfJumpsTo(self, node):
        jumps = 0
        root = self.findClosestCommonParent(node)
        cur = self.parent
        while cur.data != root.data:
            cur = cur.parent
            jumps += 1
        cur = node.parent
        while cur.data != root.data:
            cur = cur.parent
            jumps += 1
        return jumps


def findObjectsByCenter(objects, center):
    return [x for x in objects if x[0] == center]


def appendChildren(tree, objects):
    children = findObjectsByCenter(objects, tree.data)
    if children:
        for child in children:
            tmp = appendChildren(Tree(child[1], tree), objects)
            tree.appendNode(tmp)
    return tree


input = [line for line in open('input.txt').read().splitlines()]
objects = [line.split(')') for line in input]
start = findObjectsByCenter(objects, 'COM')[0]
orbits = appendChildren(Tree('COM'), objects)

you = orbits.findNode('YOU')
santa = orbits.findNode('SAN')

jumps = you.findNumberOfJumpsTo(santa)
print(jumps)
class Tree(object):

    def __init__(self, data, parent = None):
        self.parent = parent
        self.children = None
        self.data = data

    def findNode(self, node):
        if self.data == node:
            return self
        elif self.children is None:
            return
        else:
            for child in self.children:
                return child.findNode(node)

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
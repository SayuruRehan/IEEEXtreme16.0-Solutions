class Node:
    def __init__(self, id, character, yes, no):
        self.id = id
        self.character = character
        self.yes = yes
        self.no = no


class Tree:
    def __init__(self):
        self.root = None

    def add(self, type, id, character, pYes=None, pNo=None):
        if self.root is None:
            self.root = Node(id, character, pYes, pNo)
        else:
            if type == "I":
                self._addNode(id, character, pYes, pNo, self.root)
            elif type == "L":
                self._addLeaf(id, character, self.root)

    def _addNode(self, id, character, pYes, pNo, node):
        if node.yes is not None:
            if node.yes == id:
                node.yes = Node(id, character, pYes, pNo)
            else:
                if isinstance(node.yes, Node):
                    self._addNode(id, character, pYes, pNo, node.yes)
        if node.no is not None:
            if node.no == id:
                node.no = Node(id, character, pYes, pNo)
            else:
                if isinstance(node.no, Node):
                    self._addNode(id, character, pYes, pNo, node.no)

    def _addLeaf(self, id, character, node):
        if node.yes is not None:
            if node.yes == id:
                node.yes = Node(id, character, None, None)
            else:
                if isinstance(node.yes, Node):
                    self._addLeaf(id, character, node.yes)
        if node.no is not None:
            if node.no == id:
                node.no = Node(id, character, None, None)
            else:
                if isinstance(node.no, Node):
                    self._addLeaf(id, character, node.no)

    def isLeaf(self, node):
        if node.yes is None and node.no is None:
            return True
        else:
            return False

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.yes)
            print(str(node.id) + str(node.character) + ' ')
            self._printTree(node.no)

    def travelTree(self, node, sentence):
        if node is not None and not self.isLeaf(node):
            for letter in sentence:
                if letter == node.character:
                    return self.travelTree(node.yes, sentence)
            return self.travelTree(node.no, sentence) + " " + self.travelTree(node.yes, sentence)
        elif node is not None and self.isLeaf(node):
            return node.character
        return ""


def findFather(nodes: list):
    for i in range(len(nodes)):
        isFather = True
        for j in range(len(nodes)):
            if i != j:
                if nodes[j][0] == "I" and (nodes[j][3] == nodes[i][1] or nodes[j][4] == nodes[i][1]):
                    isFather = False
        if isFather:
            return i


def createTree(nodes: list):
    tree = Tree()
    for node in nodes:
        if node[0] == "I":
            tree.add("I", node[1], node[2], node[3], node[4])
        else:
            tree.add("L", node[1], node[2])
    return tree


def orderList(nodes: list):
    father = findFather(nodes)
    orderedList = []
    orderedList.append(nodes.pop(father))
    actInd = [orderedList[-1][3], orderedList[-1][4]]
    i = 0
    while len(nodes) > 0:
        if nodes[i][1] == actInd[0]:
            orderedList.append(nodes.pop(i))
            if (orderedList[-1][0] == "I"):
                actInd += [orderedList[-1][3], orderedList[-1][4]]
            actInd.pop(0)
            i = 0
        else:
            i += 1
    return createTree(orderedList)


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def callLanguage():
    languageNodes: list = []
    cantLanguages = get_number()
    cantSentences = get_number()
    for i in range(cantLanguages):
        actualNode = [get_word()]
        if actualNode[0] == "I":
            actualNode += [get_number(), get_word(),
                           get_number(), get_number()]
        elif actualNode[0] == "L":
            actualNode += [get_number(), get_word()]
        languageNodes.append(actualNode)
    for i in range(cantSentences):
        tree = orderList(languageNodes.copy())
        print(tree.travelTree(tree.root, input()))
    return


callLanguage()

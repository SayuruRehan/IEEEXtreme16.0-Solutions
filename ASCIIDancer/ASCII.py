

from importlib.metadata import SelectableGroups


class Dancer():
    def __init__(self):
        self.top: list = [' ', 'o', ' ']
        self.middle: list = ['/', '|', '\\']
        self.bottom: list = ['/', ' ', '\\']
        self.body: list = [self.top,  self.middle,  self.bottom]
        self.in_zone: list = ['<', '>']
        self.out_zone: list = ['/', '\\']
        self.up_zone: list = ['(', ')']

    def setCommand(self, command: str) -> list:
        if (self.isSayCommand(command)):
            print(command[4:])
            return [command[4:]]
        elif (self.isTurnCommand(command)):
            self.turnBody()
        else:
            orientation: int = self.getOrientation(command)
            zone: int = self.getZone(command)
            char: str = self.getChar(command, orientation)

            if (self.haveDestination(command)):
                destination: int = self.getToDestination(command, orientation)
                self.setCharInto(orientation, destination, char)
            else:
                self.setCharInto(orientation, zone, char)
        self.printBody()
        return self.body

    def isTurnCommand(self, command: str) -> bool:
        if (command.find('turn') != -1):
            return True
        else:
            return False

    def turnBody(self) -> None:

        for i in range(len(self.body)):
            self.body[i].reverse()
            self.body[i][0] = self.turnSide(self.body[i][0])
            self.body[i][2] = self.turnSide(self.body[i][2])

    def turnSide(self, side: int) -> str:
        if (side in self.in_zone):
            if (side == self.in_zone[0]):
                return self.in_zone[-1]
            else:
                return self.in_zone[0]
        elif (side in self.up_zone):
            if (side == self.up_zone[0]):
                return self.up_zone[-1]
            return self.up_zone[0]
        elif (side in self.out_zone):
            if (side == self.out_zone[0]):
                return self.out_zone[-1]
            return self.out_zone[0]
        else:
            return ' '

    def printBody(self) -> None:
        for i in self.body:
            print(i[0]+i[1]+i[2])

    def haveDestination(self, command: str) -> bool:
        if (command.find('to') != -1):
            return True
        else:
            return False

    def isSayCommand(self, command: str) -> bool:
        if (command.find('say') != -1):
            return True
        else:
            return False

    def getToDestination(self, command: str, orientation: int) -> None:
        if (command.find('head') != -1):
            self.body[1][orientation] = ' '
            return 0  # firts position is left, second is right
        elif (command.find('hip') != -1 or command.find('start') != -1):
            self.body[0][orientation] = ' '
            return 1
        elif (command.find('in') != -1 or command.find('out') != -1):
            return 2

    def setCharInto(self, orientation: int, destination: int, char: str) -> None:
        self.body[destination][orientation] = char

    def getOrientation(self, command: str) -> int:
        if (command.find('left') != -1):
            return -1
        elif (command.find('right') != -1):
            return 0  # return the posicion of rights

    def getZone(self, command: str) -> int:
        if (command.find('hand') != -1):
            return 1
        elif (command.find('leg') != -1):
            return 2
        else:
            return 0

    def getChar(self, command: str, orientation: int) -> str:

        if (command.find('in') != -1 or command.find('hip') != -1):
            return self.in_zone[orientation]
        elif (command.find('out') != -1 or command.find('start') != -1):
            return self.out_zone[orientation]
        elif (command.find('head') != -1):
            return self.up_zone[orientation]


def getCommand() -> str:
    return input()


def get_number() -> int:
    return int(input())


dancer: Dancer = Dancer()
T = get_number()
for t in range(T):
    testCases = get_number()
    dancer: Dancer = Dancer()
    for j in range(testCases):
        command: str = getCommand()
        dancer.setCommand(command)

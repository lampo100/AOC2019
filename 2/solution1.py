from typing import Union, TextIO

class Parser:
    def __init__(self, filename: str):
        self.__tokens = []
        with open(filename) as file:
            for line in file:
                self.__tokens.extend([int(x) for x in line.split(',')])

    def __getitem__(self, item):
        return self.__tokens[item]

    def __setitem__(self, key, value):
        self.__tokens[key] = value

    def __str__(self):
        return str(self.__tokens)

class OpcodeHandler:
    def __init__(self, parser: Parser):
        self.__parser = parser
        self.__opcode_index = 0

    def next(self):
        index = self.__opcode_index * 4
        operation = parser[index]
        if operation == 99:
            return False
        first_argument = parser[parser[index + 1]]
        second_argument = parser[parser[index + 2]]
        if operation == 1:
            parser[parser[index + 3]] = first_argument + second_argument
        elif operation == 2:
            parser[parser[index + 3]] = first_argument * second_argument
        else:
            raise Exception("Unknown opcode [" + operation + "]")
        self.__opcode_index += 1
        return True


if __name__ == '__main__':
    parser = Parser('./input')
    handler = OpcodeHandler(parser)
    while handler.next():
        continue
    print(parser)



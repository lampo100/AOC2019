from second.solution1 import Parser, OpcodeHandler
from threading import *

def run_program(noun: int, verb: int):
    parser = Parser('./input')
    parser[1] = noun
    parser[2] = verb
    handler = OpcodeHandler(parser)
    while handler.next():
        continue
    return parser[0]

if __name__ == '__main__':
    for noun in range(155):
        for verb in range(155):
            output = run_program(noun, verb)
            print(output)
            if output ==  19690720:
                print("Noun: " + str(noun) + " ; Verb: " + str(verb))
                exit(0)
            print("noun=" + str(noun) + ";verb=" + str(verb))
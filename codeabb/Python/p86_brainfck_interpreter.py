"""
CodeAbbey, Problem 86
Coded by Raul Gonzalez
"""


class Brainfuck(object):
    def __init__(self, commands: str, input_list: str):
        self.current_index = 0
        self.cells = [0]
        self.input_list = list(map(int, input_list.split()))
        self.commands = commands
        self.results = []

    def run(self):
        index = 0
        loop_start = 0
        while index < len(self.commands):
            cmd = self.commands[index]
            if cmd == '[':
                if self.cells[self.current_index]:
                    loop_start = index
                else:
                    index = self.commands.find(']', index)
            elif cmd == ']':
                index = loop_start
                continue
            else:
                self.command(cmd)
            index += 1
        print(" ".join(map(str, self.results)))

    def command(self, cmd):
        if cmd == ';':
            self.get_input()
        elif cmd == '>':
            self.move_right()
        elif cmd == '<':
            self.move_left()
        elif cmd == '+':
            self.increment()
        elif cmd == '-':
            self.decrement()
        elif cmd == ':':
            self.print_cell()

    def get_input(self):
        try:
            self.cells[self.current_index] = self.input_list.pop(0)
        except KeyError:
            print('no inputs left')

    def print_cell(self):
        self.results.append(self.cells[self.current_index])

    def increment(self):
        self.cells[self.current_index] += 1

    def decrement(self):
        self.cells[self.current_index] -= 1

    def move_right(self):
        self.current_index += 1
        if self.current_index == len(self.cells):
            self.cells.append(0)

    def move_left(self):
        self.current_index -= 1
        if self.current_index < 0:
            raise IndexError('out of index range')


def main():
    commands = input()
    input_list = input()
    bf = Brainfuck(commands, input_list)
    bf.run()

if __name__ == "__main__":
    main()

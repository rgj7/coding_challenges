"""
CodeAbbey, Problem 96
Coded by whoisrgj
"""


class Problem96:
    def __init__(self):
        self.GAME_FIELD_ROWS = 13
        # self.GAME_FIELD_COLUMNS = 21
        self.game_field = list()
        self.step_sequences = list()
        self.snake_body_coordinates = [(0, 0), (0, 1), (0, 2)]
        self.total_steps = 0
        self.current_direction = 'R'
        self.steps_remaining = 0
        self.next_x = 0
        self.next_y = 2

    def get_game_field_from_input(self):
        for i in range(self.GAME_FIELD_ROWS):
            self.game_field.append(list(input().split(" ")))

    def get_initial_steps_from_input(self):
        self.step_sequences = list(input().split(" "))
        self.step_sequences.reverse()  # pop(0)/O(n) vs pop()/O(1)
        self.steps_remaining = int(self.step_sequences.pop())

    def next_step(self):
        if self.steps_remaining > 0:
            if self.current_direction == 'R':
                self.next_y += 1
            elif self.current_direction == 'L':
                self.next_y -= 1
            elif self.current_direction == 'U':
                self.next_x -= 1
            elif self.current_direction == 'D':
                self.next_x += 1
            self.steps_remaining -= 1
            return True
        else:
            if len(self.step_sequences) > 0:
                self.current_direction = self.step_sequences.pop()
                self.steps_remaining = int(self.step_sequences.pop())
                return self.next_step()
            else:
                return False

    # snake body methods
    def remove_tail(self):
        tail = self.snake_body_coordinates.pop(0)
        self.game_field[tail[0]][tail[1]] = '-'

    def add_head(self, x, y):
        self.snake_body_coordinates.append((x, y))
        self.game_field[x][y] = 'X'

    # def print_game_field(self):
    #     for i in range(self.GAME_FIELD_ROWS):
    #         print(" ".join(self.game_field[i]))
    #     print("")

    def solve(self):
        self.get_game_field_from_input()
        self.get_initial_steps_from_input()

        while self.next_step():
            # self.print_game_field()
            self.total_steps += 1
            if self.game_field[self.next_x][self.next_y] == '$':
                self.add_head(self.next_x, self.next_y)
            elif self.game_field[self.next_x][self.next_y] == 'X':
                # problem asks for coordinates in relation to an x-y axis
                print("{} {} {}".format(self.next_y, self.next_x, self.total_steps))
                break
            else:
                self.add_head(self.next_x, self.next_y)
                self.remove_tail()

if __name__ == "__main__":
    Problem96().solve()

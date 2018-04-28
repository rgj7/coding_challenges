# reddit.com/r/dailyprogrammer
# challenge 154, hard: wumpus cave game

from enum import Enum
import os
import random


class RoomType(Enum):
    EMPTY = "You see nothing which is something."
    ENTRANCE = "You see the entrance here. You wish to run away?"
    PIT_TRAP = "You fell to your death. SPLAT!"
    GOLD = "Before you, lies the gold of adventure seekers who fed a " \
           "Wumpus recently."
    WEAPON = "Cast before you in a rock, a sword awaits to be looted and " \
             "name yourself king."
    WUMPUS = "Overwhelmed in stench, a Wumpus stands before you, " \
             "ready to eat you."


class Room(object):
    def __init__(self, room_type=RoomType.EMPTY, visited=False):
        self.room_type = room_type
        self.visited = visited


class WumpusCaveGame(object):
    _ROOMS = (
        (RoomType.WUMPUS, 0.15),
        (RoomType.PIT_TRAP, 0.05),
        (RoomType.GOLD, 0.15),
        (RoomType.WEAPON, 0.15))
    
    def __init__(self, cave_size=10):
        self.cave_size = cave_size
        self.cave = self.generate_cave()
        self.current_room = self.find_entrance()
        self.points = 0
        self.has_weapon = False
        self.is_running = False

    def start(self):
        self.is_running = True
        while self.is_running:
            os.system('clear')
            self.print_cave()
            print(self.room_description())
            # self.print_environment_clues()
            print(self.points_weapon_status())
            move = input("Enter Move (? for help) > ")
            self.process_move(move)

    def generate_cave(self):
        cave = [Room(RoomType.ENTRANCE, True)]  # init with an entrance
        # add rooms
        for room_type, percent in self._ROOMS:
            for _ in range(int((self.cave_size ** 2) * percent)):
                cave.append(Room(room_type))
        # fill with empty rooms
        empty_rooms = (self.cave_size ** 2) - len(cave)
        cave.extend([Room(RoomType.EMPTY) for _ in range(empty_rooms)])
        random.shuffle(cave)
        return cave

    def find_entrance(self):
        for index, room in enumerate(self.cave):
            if room.room_type == RoomType.ENTRANCE:
                return index

    def process_move(self, move):
        if move in "NSEW":
            self.move_player(move)
            self.check_room()
        elif move == 'L':
            self.loot_room()
        elif move == 'R':
            self.run_out_of_cave()
        elif move == 'X':
            self.points = 0
            self.game_over()
        else:
            self.show_help()

    def move_player(self, direction):
        row = self.current_room // self.cave_size
        col = self.current_room % self.cave_size
        if direction == 'N' and row > 0:
            row -= 1
        elif direction == 'S' and row < self.cave_size - 1:
            row += 1
        elif direction == 'W' and col > 0:
            col -= 1
        elif direction == 'E' and col < self.cave_size - 1:
            col += 1
        self.current_room = (row * self.cave_size) + col

    def check_room(self):
        current_room = self.cave[self.current_room]
        if current_room.visited is False:
            self.points += 1
            current_room.visited = True
            if current_room.room_type == RoomType.WUMPUS:
                if self.has_weapon:
                    self.points += 10
                    current_room.room_type = RoomType.EMPTY
                else:
                    self.game_over(wumpus=True)
            elif current_room.room_type == RoomType.PIT_TRAP:
                self.game_over(pit=True)

    def loot_room(self):
        current_room = self.cave[self.current_room]
        if current_room.room_type in (RoomType.WEAPON, RoomType.GOLD):
            self.points += 5
            if current_room.room_type == RoomType.WEAPON:
                self.has_weapon = True
                # self.change_weapon_rooms_to_gold()
            current_room.room_type = RoomType.EMPTY
        else:
            print("You can't loot this room!")

    def run_out_of_cave(self):
        current_room = self.cave[self.current_room]
        if current_room.room_type == RoomType.ENTRANCE:
            self.game_over(run=True)
        else:
            print("You must be at the cave entrance to run!")

    def show_help(self):
        pass

    def game_over(self, wumpus=False, pit=False, run=False):
        self.is_running = False
        if wumpus:
            print("A Wumpus attacks you and makes you his lunch.")
        elif pit:
            print("You fall to your death. Your screams are heard by no one.")
        elif run:
            print(
                "You exit the Wumpus cave and run to town. People buy you "
                "ales as you tell the story of your adventures.")
        print("*** GAME OVER ***")
        print("You scored {points} points!".format(points=self.points))

    def print_cave(self):
        print("#" * (self.cave_size + 2), "\n#", end='')
        for index, room in enumerate(self.cave, start=1):
            symbol = '?'
            if room.visited:
                if room.room_type == RoomType.EMPTY:
                    symbol = '.'
                elif room.room_type == RoomType.WEAPON:
                    symbol = 'W'
                elif room.room_type == RoomType.GOLD:
                    symbol = '$'
                elif room.room_type == RoomType.ENTRANCE:
                    symbol = '^'
                if index - 1 == self.current_room:
                    symbol = '@'
            print(symbol, end='')
            if index % self.cave_size == 0:
                print("#\n#", end='')
        print("#" * (self.cave_size + 1))

    def room_description(self):
        return self.cave[self.current_room].room_type.value

    def points_weapon_status(self):
        point_status = "{0} points earned".format(self.points)
        if self.has_weapon:
            weapon_status = "You are armed and dangerous."
        else:
            weapon_status = "You are weaponless."
        return "[{0}] {1}".format(point_status, weapon_status)


def main():
    wcg = WumpusCaveGame()
    wcg.start()


if __name__ == "__main__":
    main()

"""
CodeAbbey, Problem 177
Coded by whoisrgj
"""

import requests
import time


class NimGame(object):
    _url = ""

    def __init__(self, token):
        self.token = token
        self.heap = []
        self.is_running = False

    def start(self):
        print("Game has commenced")
        self.is_running = True
        self.update()  # get the initial heap
        while self.is_running:
            time.sleep(1)
            self.update_with_next_move()
        print("Game has ended")

    def update_with_next_move(self):
        heap, stones = self.calculate_next_move()
        self.print_next_move(heap=heap, stones=stones)
        next_move = "{0} {1}".format(heap, stones)
        self.update(move=next_move)

    def calculate_next_move(self):
        xor_sum = self.heap[0] ^ self.heap[1] ^ self.heap[2]
        for heap, stones in enumerate(self.heap):
            if stones ^ xor_sum < stones:
                return heap, stones - (stones ^ xor_sum)

    def update(self, move=None):
        payload = {'token': self.token}
        if move:
            payload['move'] = move
        try:
            response = requests.post(self._url, data=payload)
            self.parse_response(response)
        except requests.RequestException:
            print("Error sending request...")
            self.is_running = False

    def parse_response(self, response):
        for line in response.text.splitlines():
            key, value = line.split(':')
            if key == "move":
                self.print_opponent_move(value)
            elif key == "heaps":
                self.update_heap(value)
                self.print_heap(self.heap)
            elif key == "end":
                self.is_running = False
                self.print_victory_token(value)

    def update_heap(self, heap_values):
        heap = heap_values.strip().split()
        self.heap = list(map(int, heap))

    @staticmethod
    def print_next_move(stones, heap):
        print("You took {0} stones from heap {1}".format(stones, heap))

    @staticmethod
    def print_opponent_move(move_values):
        heap_stack, stones = move_values.strip().split()
        print("--> Opponent took {0} stones from heap {1}".format(
            stones, heap_stack))

    @staticmethod
    def print_heap(heap):
        print("--> Heaps: ", ", ".join(heap))

    @staticmethod
    def print_victory_token(victory_token):
        print("--> End: ", victory_token.strip())


def main():
    game = NimGame("")
    game.start()

if __name__ == "__main__":
    main()

"""
CodeAbbey, Problem 177
Coded by whoisrgj
"""

import requests
import time


class NimGame(object):
    _URL = ""

    def __init__(self, token):
        self.payload = {'token': token}
        self.heap = []
        self.is_running = False

    def start(self):
        self.is_running = True
        self.send()  # get the initial heap
        self.run()

    def run(self):
        print("Game has commenced")
        while self.is_running:
            self.move(*self.calculate())
            time.sleep(1)
            self.send()
        print("Game has ended")

    def move(self, heap, stones):
        print("You took {0} stones from heap {1}".format(stones, heap))
        self.payload['move'] = "{0} {1}".format(heap, stones)

    def calculate(self):
        heap_list = list(map(int, self.heap))
        xor_sum = heap_list[0] ^ heap_list[1] ^ heap_list[2]
        for heap, stones in enumerate(heap_list):
            if stones ^ xor_sum < stones:
                return heap, stones - (stones ^ xor_sum)

    def send(self):
        try:
            r = requests.post(self._URL, data=self.payload)
            for line in r.text.splitlines():
                key, value = line.split(':')
                if key == "move":
                    heap_stack, stones = value.strip().split()
                    print("--> Opponent took {0} stones from heap {1}".format(
                        stones, heap_stack))
                elif key == "heaps":
                    self.heap = list(value.strip().split())
                    print("--> Heaps: ", ", ".join(self.heap))
                elif key == "end":
                    print("--> End: ", value.strip())
                    self.is_running = False
        except requests.RequestException:
            print("Error sending request...")
            self.is_running = False


def main():
    game = NimGame("")
    game.start()

if __name__ == "__main__":
    main()

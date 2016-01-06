"""
CodeAbbey, Problem 177
Coded by whoisrgj
"""

import requests
import time


class NimGame:
    _url = ""

    def __init__(self, t):
        self.payload = dict()
        self.payload['token'] = t
        self.heap = []
        self.running = False

    def start(self):
        if not self.running:
            print("Game has commenced.")
            self.running = True
            self.send(self.payload)
        else:
            print("Game has already started.")

    def send(self, payload):
        try:
            r = requests.post(self._url, data=payload)
            for line in r.text.splitlines():
                key, value = line.split(':')
                if key == "move":
                    h, s = value.strip().split()
                    print("--> Opponent took {0} stones from heap {1}.".format(s, h))
                elif key == "heaps":
                    self.heap = list(value.strip().split())
                    print("--> Heaps: ", ", ".join(self.heap))
                elif key == "end":
                    print("--> End: ", value.strip())
                    self.end()
        except requests.RequestException:
            print("Error sending request...")

    def end(self):
        if self.running:
            self.running = False
            print("Game has ended.")
        else:
            print("Game has already ended.")

    def move(self, heap, stones):
        print("You took {0} stones from heap {1}.".format(stones, heap))
        self.payload['move'] = "{0} {1}".format(heap, stones)
        self.send(self.payload)

    def calculate(self):
        heap = list(map(int, self.heap))
        xor_sum = heap[0] ^ heap[1] ^ heap[2]
        for i in range(len(heap)):
            if heap[i] ^ xor_sum < heap[i]:
                return i, heap[i]-(heap[i] ^ xor_sum)

    def is_running(self):
        return self.running

    def get_heap(self):
        return self.heap


def main():
    game = NimGame("")
    game.start()

    while game.is_running():
        h, s = game.calculate()
        #h, s = map(int, input("Enter move: ").split())
        time.sleep(1)
        game.move(h, s)

if __name__ == "__main__":
    main()

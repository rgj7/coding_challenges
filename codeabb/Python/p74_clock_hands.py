"""
CodeAbbey, Problem 74
Coded by whoisrgj
"""

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class ClockHands(object):
    MINUTE_HAND_LENGTH = 9.0
    HOUR_HAND_LENGTH = 6.0
    DEGREES_PER_MINUTE = 6.0
    DEGREES_PER_HOUR = 30.0
    ORIGIN_X = 10.0
    ORIGIN_Y = 10.0

    def get_minute_hand_endpoint(self, m):
        radians = math.radians(self.DEGREES_PER_MINUTE*m)
        return self._init_endpoint(self.MINUTE_HAND_LENGTH, radians)

    def get_hour_hand_endpoint(self, h, m):
        h %= 12  # converts 24-hr to 12-hr
        # 0.5 = 30 deg in hr / 60 min
        radians = math.radians(self.DEGREES_PER_HOUR*h + 0.5*m)
        return self._init_endpoint(self.HOUR_HAND_LENGTH, radians)

    def _init_endpoint(self, length, radians):
        return Point(
            x=length*math.sin(radians)+self.ORIGIN_X,
            y=length*math.cos(radians)+self.ORIGIN_Y)

    def get_endpoints(self, hour, minute):
        hour_endpoint = self.get_hour_hand_endpoint(hour, minute)
        minute_endpoint = self.get_minute_hand_endpoint(minute)
        return "{:.8f} {:.8f} {:.8f} {:.8f}".format(
            hour_endpoint.x, hour_endpoint.y,
            minute_endpoint.x, minute_endpoint.y)


def main():
    n = int(input())  # not used
    times = list(input().split())
    ch = ClockHands()
    print(*(ch.get_endpoints(*map(int, time.split(":"))) for time in times))

if __name__ == "__main__":
    main()

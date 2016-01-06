"""
CodeAbbey, Problem 74
Coded by Raul Gonzalez
"""

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Problem74:
    def __init__(self):
        self.MINUTE_HAND_LENGTH = 9.0
        self.HOUR_HAND_LENGTH = 6.0
        self.DEGREES_PER_MINUTE = 6.0
        self.DEGREES_PER_HOUR = 30.0
        self.ORIGIN_X = 10.0
        self.ORIGIN_Y = 10.0

    def get_minute_hand_end_point(self, m):
        minute_hand_end_point = Point()
        radians = math.radians(self.DEGREES_PER_MINUTE*m)
        minute_hand_end_point.x = self.MINUTE_HAND_LENGTH*math.sin(radians)+self.ORIGIN_X
        minute_hand_end_point.y = self.MINUTE_HAND_LENGTH*math.cos(radians)+self.ORIGIN_Y
        return minute_hand_end_point

    def get_hour_hand_end_point(self, h, m):
        hour_hand_end_point = Point()
        h %= 12  # converts 24-hr to 12-hr
        radians = math.radians(self.DEGREES_PER_HOUR*h + 0.5*m)  # 0.5 = 30 deg in hr / 60 min
        hour_hand_end_point.x = self.HOUR_HAND_LENGTH*math.sin(radians)+self.ORIGIN_X
        hour_hand_end_point.y = self.HOUR_HAND_LENGTH*math.cos(radians)+self.ORIGIN_Y
        return hour_hand_end_point

    def solve(self):
        clock_hand_points = list()
        test_cases = int(input())
        times = list(input().split())
        for tc in range(test_cases):
            hour, minute = map(int, times[tc].split(":"))
            hour_end_pnt = self.get_hour_hand_end_point(hour, minute)
            min_end_pnt = self.get_minute_hand_end_point(minute)
            clock_hand_points.append(
                "{:.8f} {:.8f} {:.8f} {:.8f}".format(hour_end_pnt.x, hour_end_pnt.y, min_end_pnt.x, min_end_pnt.y)
            )
        print(" ".join(clock_hand_points))


if __name__ == "__main__":
    Problem74().solve()
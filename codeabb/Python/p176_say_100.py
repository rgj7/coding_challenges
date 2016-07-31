"""
CodeAbbey, Problem 176
Coded by whoisrgj
"""

import requests


class Say100(object):
    _url = "http://codeabbey.sourceforge.net/say-100.php"

    def __init__(self, token):
        self.token = token

    def start(self):
        initial_number = int(self.send())
        answer = self.calculate(initial_number)
        victory_token = self.send(answer=answer)
        print(victory_token)

    def send(self, answer=None):
        payload = {'token': self.token}
        if answer:
            payload['answer'] = answer
        response = requests.post(self._url, data=payload)
        response.raise_for_status()
        return self.parse_response(response)

    @staticmethod
    def parse_response(response):
        _, value = response.text.split(":")
        return value.strip()

    @staticmethod
    def calculate(number):
        return 100 - number


def main():
    game = Say100("56y/wa38p8oeeeg0SRXD+TU3")
    game.start()

if __name__ == '__main__':
    main()

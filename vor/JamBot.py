
from time import sleep
from termcolor import colored

class Bot:

    wait = 1

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _format(self,s):
        return colored(s, 'yellow')

    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name？"

    def _think(self,s):
        return f"Hello, {s}"

class GreetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"

    def _think(self,s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"

import random

class FavoriteColorBot(Bot):
    def __init__(self):
        self.q = "What's your favorite colors?"

    def _think(self,s):
        colors = ['yellow','black','white']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}.\n  Actually, I'm teasing you, you know I'm just a bot, hahaha..."

from simpleeval import simple_eval

class CalcBot(Bot):
    def __init__(self):
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try:"

    def _think(self,s):
        return f"Done. Result = {simple_eval(s)}"
    
    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()

        while True:
            sleep(Bot.wait)
            print(self._format(self._think(self.a)))
            print('Input some arithmetic expression again or input "q" to quit')
            self.s = input()
            if self.s == 'q':
                break
            else:
                self.a = self.s

class Eai:

    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []

    def add(self,bot):
        self.bots.append(bot)

    def _prompt(self,s):
        print(s)
        print() 

    def run(self):
        self._prompt("This is Eai dialog Bot. Let's talk...")
        for bot in self.bots:
            bot.run()

jam = Eai(1)

jam.add(HelloBot())
jam.add(FavoriteColorBot())
jam.add(CalcBot())
jam.add(GreetingBot())

jam.run()
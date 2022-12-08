import sys


class Computer:
    def __getattr__(self, name):
        print("Computer says no")


sys.modules[__name__] = Computer()

"""
Run me with molotov:
    molotov --single-run molotov-script.py
"""
from molotov import scenario
from common import returnSomething


@scenario(1)
def scenario():
    print(returnSomething())

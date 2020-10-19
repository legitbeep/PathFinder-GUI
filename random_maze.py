import random

SIZE = 5

maze = [[1 for _ in range(SIZE)] for _ in range(SIZE)]
stack = []

while len(stack) > 0 : 
	
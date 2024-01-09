import random
import time
import pygame
import math
import numpy as np
from copy import deepcopy

class connect4Player(object):
	def __init__(self, position, seed=0):
		self.position = position
		self.opponent = None
		self.seed = seed
		random.seed(seed)

	def play(self, env, move):
		move = [-1]

class human(connect4Player):

	def play(self, env, move):
		move[:] = [int(input('Select next move: '))]
		while True:
			if int(move[0]) >= 0 and int(move[0]) <= 6 and env.topPosition[int(move[0])] >= 0:
				break
			move[:] = [int(input('Index invalid. Select next move: '))]

class human2(connect4Player):

	def play(self, env, move):
		done = False
		while(not done):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEMOTION:
					pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
					posx = event.pos[0]
					if self.position == 1:
						pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
					else: 
						pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
				pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))
					move[:] = [col]
					done = True

class randomAI(connect4Player):

	def play(self, env, move):
		possible = env.topPosition >= 0
		indices = []
		for i, p in enumerate(possible):
			if p: indices.append(i)
		move[:] = [random.choice(indices)]

class stupidAI(connect4Player):

	def play(self, env, move):
		possible = env.topPosition >= 0
		indices = []
		for i, p in enumerate(possible):
			if p: indices.append(i)
		if 3 in indices:
			move[:] = [3]
		elif 2 in indices:
			move[:] = [2]
		elif 1 in indices:
			move[:] = [1]
		elif 5 in indices:
			move[:] = [5]
		elif 6 in indices:
			move[:] = [6]
		else:
			move[:] = [0]

class minimaxAI(connect4Player):

	def play(self, env, move):
		env = deepcopy(env)
		env.visualize = False

		if np.array_equal(env.topPosition, [5, 5, 5, 5, 5, 5, 5]) or np.array_equal(env.topPosition, [5, 5, 5, 4, 5, 5, 5]):
			move[:] = [3]
			return

		depth = 2
		v, col = self.maxValue(env, move, depth)
		move[:] = [col]


	def maxValue(self, env, move, depth):
		possible = env.topPosition >= 0
		if len(env.history[0]) != 0:
			if env.gameOver(env.history[0][-1], self.opponent.position):
				return -math.inf, None
			elif np.array_equal(possible, [False, False, False, False, False, False, False]):
				return 0, None
			elif depth == 0:
				return self.evalFunction(env, move), None
		v = -math.inf
		col = -1
		for i, p in enumerate(possible):
			if p:
				next_node = deepcopy(env)
				self.simulateMove(next_node, i, self.position)
				child = self.minValue(next_node, i, depth-1)[0]
				if child > v:
					v = child
					col = i
		return v, col



	def minValue(self, env, move, depth):
		possible = env.topPosition >= 0
		if len(env.history[0]) != 0:
			if env.gameOver(env.history[0][-1], self.position):
				return math.inf, None
			elif np.array_equal(possible, [False, False, False, False, False, False, False]):
				return 0, None
			elif depth == 0:
				return self.evalFunction(env, move), None
		v = math.inf
		col = -1
		for i, p in enumerate(possible):
			if p:
				next_node = deepcopy(env)
				self.simulateMove(next_node, i, self.opponent.position)
				child = self.maxValue(next_node, i, depth-1)[0]
				if child < v:
					v = child
					col = i
		return v, col


	def evalFunction(self, env, move):
		scoreDict = {-3: 0, -2: 0, -1: 0, 1: 0, 2: 0, 3: 0}

		# horizontal
		for row in env.board:
			aiStreak = 0
			count = 0
			for m in row:
				if m == 0:
					if aiStreak == 1 or aiStreak == 2:
						scoreDict[count] += 1
					count = 0
					aiStreak = 0
					continue
				elif m == self.position:
					if aiStreak == 2:
						scoreDict[count] += 1
						count = 0
					count += 1
					aiStreak = 1
				elif m == self.opponent.position:
					if aiStreak == 1:
						scoreDict[count] += 1
						count = 0
					count -= 1
					aiStreak = 2
			if count != 0:
				scoreDict[count] += 1
		aiScore = scoreDict[1]*2 + scoreDict[2]*20 + scoreDict[3]*200
		opScore = scoreDict[-1] + scoreDict[-2]*10 + scoreDict[-3]*100

		# vertical
		env_transpose = env.board.transpose()
		for row in env_transpose:
			aiStreak = 0
			count = 0
			for m in row:
				if m == 0:
					if aiStreak == 1 or aiStreak == 2:
						scoreDict[count] += 1
					count = 0
					aiStreak = 0
					continue
				elif m == self.position:
					if aiStreak == 2:
						scoreDict[count] += 1
						count = 0
					count += 1
					aiStreak = 1
				elif m == self.opponent.position:
					if aiStreak == 1:
						scoreDict[count] += 1
						count = 0
					count -= 1
					aiStreak = 2
			if count != 0:
				scoreDict[count] += 1
		aiScore = scoreDict[1]*2 + scoreDict[2]*20 + scoreDict[3]*200
		opScore = scoreDict[-1] + scoreDict[-2]*10 + scoreDict[-3]*100

		return aiScore - opScore



	def simulateMove(self, env, move, player):
		env.board[env.topPosition[move]][move] = player
		env.topPosition[move] -= 1
		env.history[0].append(move)


class alphaBetaAI(connect4Player):

	def play(self, env, move):
		self.childOrdering = [5, 3, 1, 0, 6, 2, 4]
		env = deepcopy(env)
		env.visualize = False

		if np.array_equal(env.topPosition, [5, 5, 5, 5, 5, 5, 5]) or np.array_equal(env.topPosition,																			[5, 5, 5, 4, 5, 5, 5]):
			move[:] = [3]
			return

		depth = 3
		v, col = self.maxValue(env, move, depth, -math.inf, math.inf)
		move[:] = [col]
		print("TIMEOUT")


	def maxValue(self, env, move, depth, alpha, beta):
		possible = env.topPosition >= 0
		if len(env.history[0]) != 0:
			if env.gameOver(env.history[0][-1], self.opponent.position):
				return -math.inf, None
			elif np.array_equal(possible, [False, False, False, False, False, False, False]):
				return 0, None
			elif depth == 0:
				return self.evalFunction(env, move), None
		v = -math.inf
		col = -1
		for i, p in enumerate(possible):
			if possible[self.childOrdering[i]]:
				next_node = deepcopy(env)
				self.simulateMove(next_node, self.childOrdering[i], self.position)
				child = self.minValue(next_node, self.childOrdering[i], depth - 1, alpha, beta)[0]
				if child > v:
					v = child
					col = self.childOrdering[i]
				alpha = max(alpha, v)
				if alpha >= beta:
					break
		return v, col

	def minValue(self, env, move, depth, alpha, beta):
		possible = env.topPosition >= 0
		if len(env.history[0]) != 0:
			if env.gameOver(env.history[0][-1], self.position):
				return math.inf, None
			elif np.array_equal(possible, [False, False, False, False, False, False, False]):
				return 0, None
			elif depth == 0:
				return self.evalFunction(env, move), None
		v = math.inf
		col = -1
		for i, p in enumerate(possible):
			if possible[self.childOrdering[i]]:
				next_node = deepcopy(env)
				self.simulateMove(next_node, self.childOrdering[i], self.opponent.position)
				child = self.maxValue(next_node, self.childOrdering[i], depth - 1, alpha, beta)[0]
				if child < v:
					v = child
					col = self.childOrdering[i]
				beta = min(beta, v)
				if beta <= alpha:
					break
		return v, col


	def evalFunction(self, env, move):
		scoreDict = {-3: 0, -2: 0, -1: 0, 1: 0, 2: 0, 3: 0}

		# horizontal
		for row in env.board:
			aiStreak = 0
			count = 0
			for m in row:
				if m == 0:
					if aiStreak == 1 or aiStreak == 2:
						scoreDict[count] += 1
					count = 0
					aiStreak = 0
					continue
				elif m == self.position:
					if aiStreak == 2:
						scoreDict[count] += 1
						count = 0
					count += 1
					aiStreak = 1
				elif m == self.opponent.position:
					if aiStreak == 1:
						scoreDict[count] += 1
						count = 0
					count -= 1
					aiStreak = 2
			if count != 0:
				scoreDict[count] += 1
		aiScore = scoreDict[1]*2 + scoreDict[2]*20 + scoreDict[3]*200
		opScore = scoreDict[-1] + scoreDict[-2]*10 + scoreDict[-3]*100

		#vertical
		env_transpose = env.board.transpose()
		for row in env_transpose:
			aiStreak = 0
			count = 0
			for m in row:
				if m == 0:
					if aiStreak == 1 or aiStreak == 2:
						scoreDict[count] += 1
					count = 0
					aiStreak = 0
					continue
				elif m == self.position:
					if aiStreak == 2:
						scoreDict[count] += 1
						count = 0
					count += 1
					aiStreak = 1
				elif m == self.opponent.position:
					if aiStreak == 1:
						scoreDict[count] += 1
						count = 0
					count -= 1
					aiStreak = 2
			if count != 0:
				scoreDict[count] += 1
		aiScore = scoreDict[1]*2 + scoreDict[2]*20 + scoreDict[3]*200
		opScore = scoreDict[-1] + scoreDict[-2]*10 + scoreDict[-3]*100
				
		return aiScore - opScore

	def simulateMove(self, env, move, player):
		env.board[env.topPosition[move]][move] = player
		env.topPosition[move] -= 1
		env.history[0].append(move)


SQUARESIZE = 100
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)





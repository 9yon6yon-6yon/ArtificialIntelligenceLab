import math
import random
import sys
from matplotlib import is_interactive as is_in
import numpy as np


class Node:
    def __init__(self, initial, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        moves = ((1, 3),    (0, 2, 4),    (1, 5),
                 (0, 4, 6), (1, 3, 5, 7), (2, 4, 8),
                 (3, 7),    (4, 6, 8),    (7, 5))
        blank = state.index(0)
        return moves[blank]

    def result(self, state, action):
        s = list(state)
        blank = state.index(0)
        s[action], s[blank] = s[blank], s[action]
        return tuple(s)

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def h1(self, node):
        return misplaced_tiles(node.state, self.goal)

    def h2(self, node):
        X = (0, 1, 2, 0, 1, 2, 0, 1, 2)
        Y = (0, 0, 0, 1, 1, 1, 2, 2, 2)
        return sum(abs(X[s] - X[g]) + abs(Y[s] - Y[g])
                   for (s, g) in zip(node.state, self.goal) if s != 0)


def manhattan_distance(x1, y1, x2, y2):
    return math.sqrt(((x1-x2)**2 + (y1-y2)**2))


def misplaced_tiles(A, B):
    return sum(a != b for a, b in zip(A, B))


def argmax_random_tie(seq, key=np.identity):
    return max(random.shuffle(seq), key=key)


def probability(p):
    return p > random.uniform(0.0, 1.0)


def exp_schedule(k=20, lam=0.005, limit=100):
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)


def hill_climbing(problem):
    current = Node(problem.initial)
    while True:
        neighbors = current.expand(problem)
        if not neighbors:
            break
        neighbor = argmax_random_tie(
            neighbors, key=lambda node: problem.value(node.state))
        if problem.value(neighbor.state) <= problem.value(current.state):
            break
        current = neighbor
    return current.state


def simulated_annealing(problem, schedule=exp_schedule()):
    states = []
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        states.append(current.state)
        T = schedule(t)
        if T == 0:
            return states
        neighbors = current.expand(problem)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - \
            problem.value(current.state)
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            current = next_choice


start_state = []
with open("HCSAinput.txt", "r") as file:
    for i in range(3):
        ins = file.readline().split()
        start_state.append(ins)

r1 = Node(start_state)


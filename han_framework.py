"""
Library functions to solve the Towers of Hanoi problem in terms of sheer Python
datastructures.
"""

import sys

from smartparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="number of towers")
    return parser.parse_args()

def print_towers(problem):
    # To allow a Python2 script to import solve w/out compromise
    from itertools import chain, zip_longest

    largest = max(chain.from_iterable(problem)) + 1
    for row in reversed(list(zip_longest(*problem, fillvalue=0))):
        print("".join(("@" * (2 * disc - 1)).center(largest * 2) for disc in row))

def assert_towers(problem):
    for stack in problem:
        for i in range(len(stack) - 1):
            if stack[i] < stack[i + 1]:
                sys.exit("bad towers: {}".format(problem))
    print("safe")

def solve(towers, start, goal, aux, n):
    """
    Solve a hanoi problem given the tower setup (an array), the start tower,
    goal tower and auxiliary tower and the number of towers to solve for
    """

    if n == 1:
        towers[goal].append(towers[start].pop())
        yield start, goal
    else:
        # "yield from" surrogates
        for s in solve(towers, start, aux, goal, n - 1):
            yield s
        towers[goal].append(towers[start].pop())
        yield start, goal
        for s in solve(towers, aux, goal, start, n - 1):
            yield s


if __name__ == "__main__":
    args = get_args()

    n = args.n
    problem = [list(reversed(range(1, n + 1))), [], []]

    for ind, mov in enumerate(solve(problem, 0, 2, 1, n)):
        #print()
        #print_towers(problem)
        #assert_towers(problem)
        pass

    print("solved {} towers with {} moves".format(n, ind))

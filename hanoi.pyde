from han_framework import solve

TOWERS = 18
PER_FRAME = 10

def draw_towers(prob):
    largest = max(i for stack in prob for i in stack)
    t_height = height / float(TOWERS)
    for xind, stack in enumerate(prob):
        cx = xind * width / 3.0 + width / 6.0
        for yind, tower in enumerate(stack):
            t_ratio = tower / float(largest)
            t_width = t_ratio * width / 3.0
            cy = yind * t_height
            fill(t_ratio * 255, 255, 255)
            rect(cx - t_width / 2.0, cy, t_width, t_height)

def setup():
    global prob, solver
    size(1600, 800)
    colorMode(HSB, *[255] * 3)
    noStroke()
    prob = [range(TOWERS, 0, -1), [], []]
    solver = solve(prob, 0, 2, 1, TOWERS)

def draw():
    translate(0, height)
    scale(1, -1)
    for _ in xrange(PER_FRAME):
        try:
            next(solver)
        except StopIteration:
            break
    background(0)
    draw_towers(prob)
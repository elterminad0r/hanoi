from han_framework import solve

TOWERS = 14
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
    global prob, solver, step, f
    size(450, 150)
    noStroke()
    colorMode(HSB, *[255] * 3)
    step = 0
    f = createFont("courier", 20)
    prob = [range(TOWERS, 0, -1), [], []]
    solver = enumerate(solve(prob, 0, 2, 1, TOWERS), 1)

def draw():
    global step
    background(0)
    fill(255)
    textFont(f)
    rect(0, 0, width * step / float((1 << TOWERS) - 1), 5)
    text("{:7.2%}".format(step / float((1 << TOWERS) - 1)), 0, 25)
    text("{:6.2f}s".format(((1 << TOWERS) - 1 - step) / float(PER_FRAME * 60)), 0, 45)
    translate(0, height)
    scale(1, -1)
    textFont(f, 20)
    for _ in xrange(PER_FRAME):
        try:
            step, _ = next(solver)
        except StopIteration:
            break
    draw_towers(prob)
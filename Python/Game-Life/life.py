from __future__ import print_function
from itertools import product
from copy import deepcopy
from random import randint
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches  # gelp library draw results from matplotlib import pyplot as plt


# method for vizualization
def do_square(xy):
    verts = []
    codes = []
    for i in range(len(xy)):
        verts.extend([(xy[i][0], xy[i][1]),  # left, bottom
                      (xy[i][0], xy[i][1] + 1),  # left, top
                      (xy[i][0] + 1, xy[i][1] + 1),  # right, top
                      (xy[i][0] + 1, xy[i][1]),  # right, bottom
                      (xy[i][0], xy[i][1])])
        codes.extend([Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY, ])
    return [verts, codes]


# help function for drawing result
def plot_field(field, env):
    xy = []
    fig = plt.figure()
    for i in field.keys():
        if field[i].state:
            xy.append([field[i].x, field[i].y])
    plot = fig.add_subplot(111)
    plot.set_facecolor('black')
    plot.set_xlim([0, 15])
    plot.set_ylim([0, 15])
    [verts, codes] = do_square(xy)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor=(0.3, 0.9, 0.1), edgecolor='black', lw=1)
    plot.add_patch(patch)
    fig.suptitle('t = {0}'.format(env.now))
    fig.savefig('t{0}.png'.format(env.now))
    plt.close(fig)


# simpy environment
import simpy

env = simpy.Environment()


class Cell(object):
    '''Cell of the space with 2 condition: state = True (cell is alive)
    and state = False (cell is death)'''

    def __init__(self, x, y, state=False):
        self.x = x
        self.y = y
        self.state = state

    def count_neighbors(self, field):
        ''' quantitty cells-neighboors '''
        length = len([1 for i in set(self.ij_Neighnoors()).intersection(set(field.keys())) if field[i].state])
        return length

    def run(self, field):
        countN = self.count_neighbors(field)
        if countN == 2:
            pass
        elif countN == 3:
            self.state = True
        else:
            self.state = False

    def ij_Neighnoors(self):
        i, j = self.x, self.y
        return [(i % 16, (j + 1) % 16), ((i - 1) % 16, (j + 1) % 16), ((i - 1) % 16, j % 16),
                ((i - 1) % 16, (j - 1) % 16),
                (i % 16, (j - 1) % 16), ((i + 1) % 16, (j - 1) % 16), ((i + 1) % 16, j % 16),
                ((i + 1) % 16, (j + 1) % 16)]

    # my Field


field = {}

# initilalization all cells in field
for x, y in product(range(0, 15), range(0, 15)):
    field.update({(x, y): Cell(x, y)})
    # certain alive cells
    # init1 = Cell(0, 0, True)
    # init2 = Cell(1, 0, True)
    # init3 = Cell(2, 0, True)
    # init4 = Cell(1, 2, True)
    # init5 = Cell(2, 1, True)
    # field.update({(0, 0): init1, (1, 0): init2, (2, 0): init3, (1, 2): init4, (2, 1): init5})

# random alive cells
for i in range(50):
    init = Cell(randint(0, 15), randint(0, 15), True)
    field.update({(init.x, init.y): init})


# method for moving to next epoch
def next_epoch():
    while True:
        _field = deepcopy(field)
        for key in field.keys():
            __field = deepcopy(_field)
            field[key].run(__field)
            yield env.timeout(1)
            plot_field(field, env)

# simPy functions env.process(next_epoch()) env.run(until = 10)
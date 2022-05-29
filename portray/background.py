import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from scipy.spatial import Delaunay


def color(base):
    scale = np.array([0.1, 0.1, 0.1])
    return (base[0, 0] / 255. + scale * np.random.random(3)).clip(0, 1)


def rmesh(xmax, ymax, npoints):
    # Generate the points randomly
    points = np.concatenate([
        # Generate x, y coordinates separately, allow non-rectangular shapes
        np.concatenate([
            np.random.randint(0, xmax, (npoints, 1)),
            np.random.randint(0, ymax, (npoints, 1)),
        ], axis=1),
        # Add the corners to the triangulations
        np.array([
            [0, 0],
            [0, ymax],
            [xmax, 0],
            [xmax, ymax],
        ])
    ])
    return points


def background(canvas, npoints=100):
    xmax, ymax, _ = canvas.shape

    tri = Delaunay(rmesh(xmax, ymax, npoints))
    for i in tri.simplices:
        plt.gca().add_patch(Polygon(tri.points[i], facecolor=color(canvas)))

    plt.xlim(0, xmax)
    plt.ylim(0, ymax)

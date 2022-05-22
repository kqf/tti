import numpy as np
import matplotlib.pyplot as plt


def plot(text, canvas):
    plt.text(2.5, 2, text, fontname="Monospace", fontsize=14)
    plt.imshow(canvas)
    plt.show()


def main():
    canvas = np.zeros((1024, 1024, 3), dtype=np.uint8)
    canvas[:, :, :] = 238, 235, 217
    plot("plain t", canvas)


if __name__ == "__main__":
    main()

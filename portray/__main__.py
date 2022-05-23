import numpy as np
import matplotlib.pyplot as plt


def plot(text, canvas):
    plt.text(
        .5,
        .5,
        text,
        fontname="monospace",
        fontsize=14,
        ha="center",
        va="center",
        # alpha=0.5,
        # Plot in axis coordinates (0, 0) -> (1, 1)
        transform=plt.gca().transAxes,
    )
    plt.gca().axis('off')
    plt.gcf().tight_layout()
    plt.imshow(canvas)
    plt.savefig(
        f"{text.replace(' ', '-')}.png",
        bbox_inches="tight",
        pad_inches=0
    )
    plt.show()


def main():
    canvas = np.zeros((1024, 1024, 3), dtype=np.uint8)
    canvas[:, :, :] = 238, 235, 217
    plot("Sample text", canvas)


if __name__ == "__main__":
    main()

import click
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot(text, canvas, ofile):
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
    plt.savefig(ofile, bbox_inches="tight", pad_inches=0)
    plt.show()


def build_canvas():
    canvas = np.zeros((1024, 1024, 3), dtype=np.uint8)
    canvas[:, :, :] = 238, 235, 217
    return canvas


@click.command()
@click.option("--data", type=click.Path(exists=True), default="data.csv")
@click.option("--output", type=click.Path(exists=False), default="images")
def main(data, output):
    df = pd.read_csv(data, names=["entity"])
    canvas = build_canvas()
    for i, entry in enumerate(df.to_dict(orient="records")):
        text = entry["entity"]
        plot(text, canvas, f"{output}/{i}.png")

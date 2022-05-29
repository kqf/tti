import matplotlib.pyplot as plt
import numpy as np
import pytest
from portray.background import background


@pytest.fixture
def canvas():
    return np.full((1024, 1024, 3), 220., dtype=np.uint8)


def test_background(canvas):
    plt.imshow(canvas)
    background(canvas)
    plt.show()

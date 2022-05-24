import numpy as np
import pytest
from portray.__main__ import plot


@pytest.fixture
def canvas():
    return np.full((1024, 1024, 3), 255., dtype=np.uint8)


def test_plots(canvas, tmp_path):
    plot("lol", canvas, tmp_path / "lol.png")

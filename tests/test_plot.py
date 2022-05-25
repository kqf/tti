import numpy as np
import pytest
from click.testing import CliRunner
from portray.__main__ import main, plot


@pytest.fixture
def canvas():
    return np.full((1024, 1024, 3), 255., dtype=np.uint8)


def test_plots(canvas, tmp_path):
    plot("lol", canvas, tmp_path / "lol.png")


def test_main_works():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert result.output == ''

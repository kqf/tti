import numpy as np
import pytest
from click.testing import CliRunner
from portray.__main__ import main, plot


@pytest.fixture
def canvas():
    return np.full((1024, 1024, 3), 255., dtype=np.uint8)


def test_plots(canvas, tmp_path):
    plot("lol", canvas, tmp_path / "lol.png")


@pytest.mark.parametrize("args", [
    [],
    ["--output", "dummy.png"]
])
def test_main_works(args, tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path) as fs:
        with open(f'{fs}/data.csv', 'w') as f:
            f.write('Jack the dull boy\nLorem Ipsum\n')
        result = runner.invoke(main, args)
    assert result.exit_code == 0

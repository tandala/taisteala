import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402
from src.utils import data  # noqa: E402
from src.app import journey as j  # noqa: E402


@pytest.fixture
def airports_three_path(tmp_path: Path) -> Path:
    path = tmp_path / "airports.dat"
    sample = Path("tests/fixtures/airports_three.dat").read_bytes()
    path.write_bytes(sample)
    return path


def test_calculate_journey(airports_three_path: Path) -> None:
    airports = data.load_airports(airports_three_path)
    index = j.build_iata_index(airports)
    codes = ["GKA", "MAG", "HGU"]
    legs, total = j.calculate_journey(codes, index)
    assert len(legs) == 2
    assert legs[0] == pytest.approx(106.7139, rel=1e-4)
    assert legs[1] == pytest.approx(179.0360, rel=1e-4)
    assert total == pytest.approx(sum(legs))

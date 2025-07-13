import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from unittest import mock  # noqa: E402
import pytest  # noqa: E402
from src.utils import data  # noqa: E402


@pytest.fixture
def sample_data_path(tmp_path: Path) -> Path:
    path = tmp_path / "airports.dat"
    sample = Path("tests/fixtures/airports_sample.dat").read_bytes()
    path.write_bytes(sample)
    return path


def test_load_airports(sample_data_path: Path) -> None:
    airports = data.load_airports(sample_data_path)
    assert len(airports) == 2
    assert airports[0]["iata"] == "GKA"


def test_download_airports_data(tmp_path: Path) -> None:
    target = tmp_path / "airports.dat"
    fake_response = mock.Mock(status_code=200, content=b"abc")
    with mock.patch("requests.get", return_value=fake_response) as m_get:
        path = data.download_airports_data(target)
    m_get.assert_called_once()
    assert path.exists()
    assert path.read_bytes() == b"abc"

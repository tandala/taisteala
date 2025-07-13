"""Utilities for handling airport data."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Dict

import requests

AIRPORTS_DATA_URL = (
    "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
)

FIELDS = [
    "airport_id",
    "name",
    "city",
    "country",
    "iata",
    "icao",
    "latitude",
    "longitude",
    "altitude",
    "timezone",
    "dst",
    "tz_database_time_zone",
    "type",
    "source",
]


def download_airports_data(dest: Path) -> Path:
    """Download the airports dataset to ``dest``.

    Args:
        dest: Destination file path.

    Returns:
        Path to the downloaded file.
    """
    response = requests.get(AIRPORTS_DATA_URL, timeout=30)
    response.raise_for_status()
    dest.write_bytes(response.content)
    return dest


def load_airports(path: Path) -> List[Dict[str, str]]:
    """Load airports from ``path``.

    Args:
        path: Path to the airports ``.dat`` file.

    Returns:
        List of airport dictionaries.
    """
    with path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [dict(zip(FIELDS, row)) for row in reader]

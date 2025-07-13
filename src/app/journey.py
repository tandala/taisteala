"""Journey distance calculations."""

from __future__ import annotations

from typing import Dict, List, Tuple

from src.utils.geo import great_circle_distance


AirportsIndex = Dict[str, Dict[str, str]]


def build_iata_index(airports: List[Dict[str, str]]) -> AirportsIndex:
    """Build a mapping from IATA code to airport record."""
    return {a["iata"]: a for a in airports if a.get("iata")}


def calculate_journey(
    codes: List[str], index: AirportsIndex
) -> Tuple[List[float], float]:
    """Calculate leg distances and total journey distance.

    Args:
        codes: Sequence of IATA codes. Must contain at least two codes.
        index: Mapping of IATA code to airport info.

    Returns:
        Tuple of list of leg distances and total distance in kilometers.
    """
    if len(codes) < 2:
        raise ValueError("Journey must include at least two airports")

    legs: List[float] = []
    for a, b in zip(codes, codes[1:]):
        try:
            a_data = index[a]
            b_data = index[b]
        except KeyError as exc:
            raise KeyError(f"Unknown IATA code: {exc.args[0]}") from exc

        lat1, lon1 = float(a_data["latitude"]), float(a_data["longitude"])
        lat2, lon2 = float(b_data["latitude"]), float(b_data["longitude"])
        legs.append(great_circle_distance(lat1, lon1, lat2, lon2))

    total = sum(legs)
    return legs, total

"""Command-line interface for Taisteala."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.data import download_airports_data, load_airports
from src.app.journey import build_iata_index, calculate_journey


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Taisteala CLI")
    parser.add_argument(
        "command", choices=["load-airports", "journey"], help="Command to execute"
    )
    parser.add_argument(
        "journey",
        nargs="?",
        help="Dash-separated IATA codes for the journey (e.g. JFK-LHR-SIN)",
    )
    parser.add_argument(
        "--dest",
        default="data/airports.dat",
        help="Path to airports data file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    dest = Path(args.dest)
    if args.command == "load-airports":
        download_airports_data(dest)
        airports = load_airports(dest)
        print(f"Loaded {len(airports)} airports")
    elif args.command == "journey":
        if not args.journey:
            raise SystemExit("Journey string is required")
        airports = load_airports(dest)
        index = build_iata_index(airports)
        codes = args.journey.split("-")
        legs, total = calculate_journey(codes, index)
        for i, dist in enumerate(legs, start=1):
            print(f"Leg {i}: {dist:.2f} km")
        print(f"Total: {total:.2f} km")


if __name__ == "__main__":
    main()

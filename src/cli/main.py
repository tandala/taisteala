"""Command-line interface for Taisteala."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.data import download_airports_data, load_airports


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Taisteala CLI")
    parser.add_argument("command", choices=["load-airports"], help="Command to execute")
    parser.add_argument(
        "--dest", default="data/airports.dat", help="Path to store airports data"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    dest = Path(args.dest)
    if args.command == "load-airports":
        download_airports_data(dest)
        airports = load_airports(dest)
        print(f"Loaded {len(airports)} airports")


if __name__ == "__main__":
    main()

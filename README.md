# Taisteala

A CLI-based travel planner. This version can download airport data and
calculate the distance for a multi-leg journey.

## Usage

- **Load airports data**

  ```bash
  python -m src.cli.main load-airports --dest data/airports.dat
  ```

- **Calculate journey distance**

  ```bash
  python -m src.cli.main journey JFK-LHR-SIN --dest data/airports.dat
  ```

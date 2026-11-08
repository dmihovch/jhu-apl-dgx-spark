#!/usr/bin/env python3
"""Render the precision comparison through concurrency 64."""

from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


ROOT: Path = Path(__file__).resolve().parents[2]
PLOTTING_DIRECTORY: Path = ROOT / "plotting"
INDEX_PATH: Path = ROOT / "baselines/rdma-pilot-2026-10/index.csv"
OUTPUT_DIRECTORY: Path = Path(__file__).resolve().parent / "figures"
OUTPUT_PATH: Path = OUTPUT_DIRECTORY / "precision_ladder_qwen3-next-80b-c64.png"
MODEL_LABELS: set[str] = {
    "qwen3-next-80b-bf16",
    "qwen3-next-80b-nvfp4",
}
MAX_CONCURRENCY: int = 64

sys.path.insert(0, str(PLOTTING_DIRECTORY))
import plot_trends


def main() -> None:
    """Filter retained measurements and use the repository precision plotter."""
    measurements: pd.DataFrame = plot_trends.load_index(str(INDEX_PATH))
    if "model_label" not in measurements.columns:
        raise ValueError("campaign index has no model labels")
    measurements = measurements[
        measurements["model_label"].isin(MODEL_LABELS)
    ].copy()
    # The single-Spark NVFP4 series has no retained 128-request point.
    measurements = plot_trends.collapse_repeats(
        measurements, allow_incomplete=True
    )
    measurements = measurements[
        measurements["concurrency"] <= MAX_CONCURRENCY
    ].copy()
    plot_trends.set_rc(300, False)
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=OUTPUT_DIRECTORY) as temporary_directory:
        plot_trends.fig_precision_ladder(
            measurements, temporary_directory, ["png"]
        )
        generated_image: Path = (
            Path(temporary_directory) / "precision_ladder_qwen3-next-80b.png"
        )
        generated_image.replace(OUTPUT_PATH)


if __name__ == "__main__":
    main()

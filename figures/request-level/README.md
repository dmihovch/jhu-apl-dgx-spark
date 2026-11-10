# Request-level Qwen3-Next NVFP4 pilot figures

Source: `dgx-spark-llm-serving-benchmark/baselines/rdma-pilot-2026-10/index.csv` and its indexed summaries. The figures contain 21 measured points: three configurations at concurrencies 1, 2, 4, 8, 16, 32 and 64. Each point has one run.

| Figure | Statistic |
|---|---|
| TTFT | Median request TTFT, unchanged |
| ITL | Median across per-request mean token gaps |
| Goodput | Requests satisfying both targets divided by measurement seconds, unchanged |
| Target attainment | 100 × qualifying requests / requests started during the measurement window |

Both targets apply to each request: TTFT ≤ 3 s and mean ITL ≤ 100 ms. Requests started during the measurement window are tracked to completion. Failed requests do not qualify. All 21 retained points report zero failures.

Qualifying counts are reconstructed from saved goodput × measurement seconds. The generator validates that each reconstructed count is an integer within the completed-request count. The percentage denominator includes all requests started in the window. This percentage is distinct from the goodput rate.

The new ITL graph uses the index field `mean_itl_p50`, verified against each summary's `mean_itl_s.p50`. Its vertical range extends to include the approximately 287 ms upper endpoint. The axis label remains `ITL (ms)`; the slide caption specifies its aggregation.

The SVG renderer uses Python ReportLab and Pillow, the local DejaVu Sans font, and axis geometry extracted from the original poster PNGs. Colors, markers, dimensions, typography and labels follow those figures. The original TTFT and goodput PNGs are copied unchanged. Font bytes are embedded in each SVG. The SVGs require no runtime Python or JavaScript.

Generate the four SVGs, the source-linked point table and the manifest from the benchmark repository:

```bash
/home/dan/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 plotting/plot_request_level_poster.py --out /home/dan/school/jhu-apl-dgx-spark/figures/request-level
```

The two revised PNG previews are rendered from the SVGs with librsvg. Original poster figures, campaign indexes, summaries and raw measurements are preserved. The manifest records source hashes and metric definitions. The point table contains derived summaries of retained measurements.

The local baseline lacks raw request streams. These figures use stored request-level summaries and aggregate qualification counts. They do not reconstruct separate TTFT-only and ITL-only violation percentages or identify the cause of increased latency.

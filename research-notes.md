# DGX Spark communication systems: presentation evidence

Prepared for a 20–25 minute JHU Applied Physics Laboratory technical interview presentation. The main sequence contains 22 screens and 23 minutes of assigned speaking time. The presentation uses the supplied PowerPoint for its topic sequence and the supplied PDF for its prior research checklist. The repository and retained artifacts control factual claims.

## Source state and terminology

- Main repository: `/home/dan/school/dgx-spark-llm-serving-benchmark`, branch `arbitrary-nodes`, commit `40e9e065d57ceebfbb3265d2d607b4f2650b2951`. Its working tree was clean before this presentation directory was added.
- Pairwise test repository: `/home/dan/school/perftest-suite-dgx-spark-cluster`, branch `transmission-time`, commit `fc590f71d1e7d11894556b86323d723e58eacc66`. Its working tree was clean when inspected.
- “Verified implementation” means behavior visible in current source. It does not establish individual authorship or historical behavior.
- “Retained measurement” means a value in a saved result artifact. It does not establish an isolated cause unless other conditions match.
- “Derived result” means arithmetic applied to a retained value or specification. The operation and units appear below.
- “User-reported history” identifies personal experience described in the task. No independent incident record establishes every reported step.

## Main sequence

| Screen | Point | Time |
| --- | --- | ---: |
| 1 | Engineering question and lab photograph placeholder | 0:30 |
| 2 | Desktop-node motivation and communication cost | 1:00 |
| 3 | Desktop system investment and hardware photo placeholder | 1:00 |
| 4 | New GB10 architecture and cluster-scale unknowns | 1:00 |
| 5 | Physical ports and logical RoCE rails | 1:00 |
| 6 | Hardware bandwidth question and measurement plan | 1:00 |
| 7 | Presenter-built pairwise PerfTest suite | 1:30 |
| 8 | Original PerfTest bandwidth figure | 1:00 |
| 9 | Original PerfTest latency figure | 1:00 |
| 10 | Original PerfTest transfer-time figure | 1:00 |
| 11 | Tensor and pipeline parallelism | 1:30 |
| 12 | vLLM, Ray, Docker, and NCCL roles | 0:45 |
| 13 | Historical NCCL TCP/RoCE plot and comparison boundary | 1:15 |
| 14 | MTU layers and congestion controls | 1:00 |
| 15 | Original precision comparison figure | 1:00 |
| 16 | TTFT, ITL, and goodput definitions | 1:00 |
| 17 | Original RoCE pilot TTFT figure | 1:00 |
| 18 | Original RoCE pilot ITL figure | 1:00 |
| 19 | Original RoCE pilot goodput figure | 1:15 |
| 20 | Serving and cache lifecycle | 1:15 |
| 21 | PCIe/NIC failure evidence and diagnostic checks | 1:15 |
| 22 | Evidence chain and next controlled test | 0:45 |

The assigned speech totals 23:00. Questions are outside that allocation.

## Embedded visual sources

The HTML embeds seven byte-identical copies of repository PNGs and one filtered precision plot rendered with the repository's `plot_trends.fig_precision_ladder` function. The precision plot retains the original panel layout, axes, labels, and series styling. HTML series keys identify the three curves in the poster plots, which have no embedded legend. All other slide drawings are conceptual HTML or SVG diagrams; they contain no simulated measurements. Fira Sans Regular and Bold are embedded from the locally installed `/usr/share/fonts/opentype/fira/` files. The presentation requires no network connection or asset directory.

| Screen | Visual source |
| --- | --- |
| 8 | [`figs/perftest_bandwidth.png`](/home/dan/school/perftest-suite-dgx-spark-cluster/figs/perftest_bandwidth.png) |
| 9 | [`figs/perftest_latency.png`](/home/dan/school/perftest-suite-dgx-spark-cluster/figs/perftest_latency.png) |
| 10 | [`nov5-figs/perftest-nov5/transmission_time_write.png`](/home/dan/school/perftest-suite-dgx-spark-cluster/nov5-figs/perftest-nov5/transmission_time_write.png) |
| 13 | [`results/tcp-rdma-interconnect-comparison/figs/stats/interconnect.png`](../../results/tcp-rdma-interconnect-comparison/figs/stats/interconnect.png) |
| 15 | [`precision_ladder_qwen3-next-80b-c64.png`](figures/precision_ladder_qwen3-next-80b-c64.png) |
| 17 | [`ttft_by_concurrency.png`](../../baselines/rdma-pilot-2026-10/figs/poster/qwen3-next-80b-nvfp4/ttft_by_concurrency.png) |
| 18 | [`itl_by_concurrency.png`](../../baselines/rdma-pilot-2026-10/figs/poster/qwen3-next-80b-nvfp4/itl_by_concurrency.png) |
| 19 | [`baselines/rdma-pilot-2026-10/figs/poster/qwen3-next-80b-nvfp4/goodput_by_concurrency.png`](../../baselines/rdma-pilot-2026-10/figs/poster/qwen3-next-80b-nvfp4/goodput_by_concurrency.png) |

Screens 1, 3, and 5 contain labeled photograph placeholders. Screen 20 contains a labeled incident-log placeholder. These placeholders identify material the presenter must supply before replacing them.

Screen 15's PNG is rendered by [`generate_precision_c64.py`](generate_precision_c64.py) from [`baselines/rdma-pilot-2026-10/index.csv`](../../baselines/rdma-pilot-2026-10/index.csv), using the original [`plotting/plot_trends.py`](../../plotting/plot_trends.py) precision-ladder function. The script collapses repeats, filters concurrency to 1, 2, 4, 8, 16, 32, and 64, and plots `tok_thru_tps` and `energy_per_token_j`. The single-Spark NVFP4 series has no retained concurrency-128 row, so repeat collapsing allows that incomplete upper endpoint before the filter. Matplotlib 3.10.9 rendered the filtered PNG. The campaign index and original precision PNG remain unchanged.

## Motivation and platform

The proposed university use is a no-cost LLM service for students and faculty, with room for university-specific knowledge and policy-compliant access. This remains broader project motivation and is omitted from the slide sequence because the current experiments do not evaluate service deployment or cost. The main repository measures serving behavior and records GPU power samples; it does not contain a full acquisition, networking, power, utilization, or total-cost analysis. Potential later reuse of desktop systems is also a proposed benefit.

NVIDIA specifies 128 GB of coherent unified memory, 273 GB/s memory bandwidth, up to 1 PFLOP at sparse FP4, a small desktop chassis, and ConnectX-7 networking for a 128 GB DGX Spark. The FP4 figure is a theoretical sparse-precision rating and must not be compared with a different precision or sparsity convention. NVIDIA currently documents up to four Spark systems connected through ConnectX-7, with a switch for four. This does not establish support for a 10–30-node research cluster. Sources: [DGX Spark product specifications](https://www.nvidia.com/en-us/products/workstations/dgx-spark/), [Spark hardware guide](https://docs.nvidia.com/dgx/dgx-spark/hardware.html), [Spark networking guide](https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html).

The task's proposed DGX Station GB300 comparison was excluded from the talk. NVIDIA documents up to 748 GB of coherent memory for DGX Station, including 252 GB of GPU HBM3e and 496 GB of CPU LPDDR5X. This is not the “52 GB more memory” relationship in the task. The proposed purchase prices were not verified and are absent from the presentation. Source: [DGX Station development guide](https://docs.nvidia.com/dgx/dgx-station-development-guide/Intro.html).

## Physical and logical topology

[`configs/cluster.yaml`](../../configs/cluster.yaml) declares `diya` as head, `betelgeuse` as worker, and four rails per node. It records interface names and IP subnets, not a photographic or switch-port record of a specific experiment. [`scripts/cluster_topology.py`](../../scripts/cluster_topology.py) validates this YAML for the serving harness. The separate pairwise suite uses JSON peer profiles such as `/home/dan/school/perftest-suite-dgx-spark-cluster/configs/diya.json`.

NVIDIA identifies two physical QSFP ports on each Spark. Each port maps to two Linux Ethernet interfaces and corresponding RoCE devices through two independent PCIe Gen 5 ×4 links. The supported cable list includes a QSFP-to-QSFP112 cable and a QSFP112 400G DAC. The Spark port is rated up to 200 Gb/s. A 400 Gb/s ConnectX-7 family capability does not set Spark's per-port rating. Source: [Spark networking guide](https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html).

The selected November 5 pairwise run records four device-to-peer links in `run.json`. Physical cable identity and any switch were not independently verified from that file. The presentation diagram therefore represents the four logical rails and two physical port groups without claiming a specific cable or switch model.

## Parallelism and serving stack

Tensor parallelism shards the computation and resident weights within layers; cross-node synchronization transfers intermediate values at implementation-dependent points. Pipeline parallelism places groups of layers on different nodes and transfers activations across stage boundaries. Autoregressive generation repeats the forward/decode path. The diagrams are conceptual. The exact collective sequence, payload shapes, and communication volume for each selected model were not traced.

The main repository's [`README.md`](../../README.md) describes a vLLM OpenAI-compatible completion server, Ray-backed distributed execution, and the streaming client. [`scripts/launch_server.sh`](../../scripts/launch_server.sh) launches vLLM inside Docker and uses Ray for two-node tensor and pipeline modes. [`scripts/connectx_env.sh`](../../scripts/connectx_env.sh) defaults `NCCL_IB_DISABLE=0` and records the selected container image; [`scripts/run_job.sh`](../../scripts/run_job.sh) performs transport checks. `NCCL_IB_DISABLE=0` permits the verbs-capable path but does not alone establish which NCCL network module carried a particular run. NCCL identifies its internal network modules as `IB` and `Socket`; transport evidence requires the selected run's logs. Source: [NCCL environment variable reference](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html).

The presentation contrasts the conventional socket path with the RoCEv2 verbs path. It does not assign an observed performance difference to kernel crossings, copies, or offload independently. The selected artifact set has no matched overhead decomposition. RoCEv2 carries the InfiniBand transport protocol over UDP/IP. Its IP encapsulation supports routed paths, although the selected two-node path does not require routing. Sources: [NVIDIA Cumulus RoCE guide](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/), [NCCL network reference](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html).

### Host bandwidth arithmetic

The retained kernel log at [`results/pcie-fail-and-high-load/more-logs-pcie.txt`](../../results/pcie-fail-and-high-load/more-logs-pcie.txt) reports `126.028 Gb/s available PCIe bandwidth (32.0 GT/s PCIe x4 link)` for one `mlx5_core` PCIe function. Two such reported x4 links imply about `2 × 126.028 = 252.056 Gb/s` of combined host-link bandwidth in one direction before transaction and application overhead. This is derived arithmetic, not an observed aggregate data rate. NVIDIA's up-to-200-Gb/s figure applies per Spark QSFP port. The retained test does not isolate a PCIe bottleneck from other shared resources. Slide 6 uses the component ratings to pose sustained single-rail and concurrent-rail bandwidth as measurement questions. Screens 7–10 introduce the pairwise suite and its bandwidth, latency, and transfer-time figures before the serving-stack discussion.

## MTU and congestion

The pairwise run's `environment/rocep1s0f0/link.json` records Linux Ethernet MTU `9000`. The matching `ibv_devinfo.txt` records `max_mtu: 4096` and `active_mtu: 4096` on that RoCE device. These values coexist in one saved run because they describe different protocol layers. A report that an RDMA MTU changed from 2048 to 4096 remains user-reported until the interface, command, date, and before/after captures are available. No measured performance change is attributed to that alleged adjustment. Source files:

- `/home/dan/school/perftest-suite-dgx-spark-cluster/perftest-results/trans-test-update/client/run-001/environment/rocep1s0f0/link.json`
- `/home/dan/school/perftest-suite-dgx-spark-cluster/perftest-results/trans-test-update/client/run-001/environment/rocep1s0f0/ibv_devinfo.txt`

RoCEv1 is link-layer and cannot traverse routed IP networks. RoCEv2 uses UDP/IP and can use IP ECN marking and congestion notification packets (CNPs). PFC operates at Ethernet priority level and is a separate mechanism. RoCEv2 encapsulation does not establish that ECN, CNP handling, or PFC was configured on this path. The presentation presents the mechanism and states the configuration gap. Sources: [NVIDIA Cumulus RoCE guide](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/), [NVIDIA NCCL RoCE troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html).

## Pairwise test suite and measurements

The separate suite's [`README.md`](/home/dan/school/perftest-suite-dgx-spark-cluster/README.md), [`perftest-suite.sh`](/home/dan/school/perftest-suite-dgx-spark-cluster/perftest-suite.sh), and [`runner.sh`](/home/dan/school/perftest-suite-dgx-spark-cluster/runner.sh) document one host/client pair per run. Device-to-peer mappings come from JSON or explicit options. The suite wraps `ib_send_lat`, `ib_write_lat`, `ib_read_lat`, and their bandwidth variants. It records exact commands, raw output, CSV measurements, and environment information. It supports isolation and concurrent-device modes, retries, and timeouts. The full suite's default connection type is RC, with 15,000 iterations per payload size in the latency and bandwidth sweeps. Those defaults do not automatically describe the separate fixed-volume transfer campaign.

The suite's plot script defines each estimated transmission time as smallest-payload typical latency plus transfer volume divided by largest-payload average throughput. The estimate is a model of the data phase, not a measured process wall time. The plotted volumes are 0.1, 1, 10, and 100 decimal GB. The plot's isolation and concurrent bands use the 10th and 90th percentiles across runs.

One full-suite client file at `/home/dan/school/perftest-suite-dgx-spark-cluster/perftest-results/trans-test-update/client/run-001/results.csv` records, for device `rocep1s0f0` in isolation, `ib_send_lat` typical latency of `2.20 µs` for 2-byte messages and `82.91 µs` for 1-MiB messages. `ib_write_bw` average bandwidth is `13.651 GB/s` for a 1-MiB message in the same run. These are one-run, perftest-reported values, not LLM serving latency or Ethernet wire rate.

The presentation embeds the suite's retained latency, bandwidth, and transfer-time figures. A separate fixed-volume client campaign has five retained runs at `/home/dan/school/perftest-suite-dgx-spark-cluster/transmission-results/rdma-transfer-nov5/client/run-001` through `run-005`. The `commands.txt` records `ib_write_bw -c RC -n 1000 -s 1000000 --report_gbits` on each device. Each test sends 1,000 messages of 1,000,000 bytes, totaling 1,000,000,000 bytes per device. Each run tested four devices separately, then together. The perftest output reports average Gbit/s for each command. These numeric rows are supporting context; the deck does not plot them.

| Run | `rocep1s0f0` isolated, Gb/s | Sum of four concurrent device rates, Gb/s |
| --- | ---: | ---: |
| 001 | 109.23 | 214.07 |
| 002 | 109.30 | 210.97 |
| 003 | 109.23 | 218.10 |
| 004 | 109.30 | 215.39 |
| 005 | 109.23 | 216.05 |
| Median | **109.23** | **215.39** |

The aggregate is the sum of four perftest-reported concurrent device rates within each run, followed by the median of five sums. The rates are not four independent physical port rates. Concurrent per-device medians were approximately 53–54 Gb/s. The selected isolated device's median estimated data-phase time is `1,000,000,000 bytes × 8 / (109.23 × 10^9 bit/s) = 0.07324 s`. Its median client process wall time is approximately `1.38 s`. Wall time includes process startup, RDMA connection setup, transfer, and teardown. The data-phase time is derived from perftest's rounded bandwidth report. It is not a directly timed phase. In the concurrent mode, each device's roughly 53–54 Gb/s rate implies about 0.15 s of estimated data-phase time for its own 1 GB transfer.

These retained results show contention or shared limits when all four logical rails run concurrently. They do not determine whether PCIe, NIC, port, memory, host scheduling, or another component is the dominant limit. The selected data do not support a universal 200 Gb/s aggregate ceiling.

### Historical TCP/RDMA comparison boundary

[`baselines/README.md`](../../baselines/README.md) records one cable for the July TCP campaign and two cables/four interfaces for the October RoCE pilot. Retained 1-GiB NCCL all-reduce rows report TCP `busbw_GBps` values `1.990`, `2.157`, and `2.218`, and one RoCE pilot value `23.564`. Multiplication by eight gives `15.920`, `17.256`, `17.744`, and `188.512 Gb/s`. NCCL bus bandwidth is not Ethernet wire rate. The campaigns differ in topology and other conditions. The presentation therefore gives no isolated TCP-to-RoCE speedup claim. A matched transport ablation is the proposed next comparison.

## Model selection and serving metrics

[`configs/models.yaml`](../../configs/models.yaml) declares dense and mixture-of-experts checkpoints with BF16, FP8, NVFP4, and MXFP4 metadata. “nBF16” in the task was treated as BF16 because the matrix uses `bf16`. Weight format, compute dtype, and KV-cache dtype are separate. The Qwen3-Next 80B-A3B BF16 entry declares `tp2` and `pp2`; its NVFP4 entry also declares `single`. Those entries are planned or permitted configurations, not proof of completed measurements. The current [`README.md`](../../README.md) describes a declared 19-checkpoint, 53-curve campaign; no claim that all 954 planned measurement windows have completed appears in the talk.

[`configs/experiment.yaml`](../../configs/experiment.yaml) defines a mixed request workload with input/output token buckets of `128/128`, `1024/256`, `4096/256`, and `8192/512`, weighted `1`, `1`, `1`, and `0.5`. It sets seed `1234` and closed-loop mode by default. The client requests exact output token counts and records token arrival times. [`bench/client.py`](../../bench/client.py) defines TTFT as request start to first returned token ID and request mean ITL as the mean of subsequent token gaps. [`bench/metrics.py`](../../bench/metrics.py) counts successful requests started in the measured window that meet `TTFT ≤ 3.0 s` and per-request `mean ITL ≤ 0.10 s`, divided by measurement seconds. A secondary `0.20 s` ITL tier exists. The plotted pooled token-gap median and the per-request mean used for goodput are distinct statistics. The thresholds are project objectives.

### Retained RoCE pilot figures

The serving figures embedded on screens 15, 17, 18, and 19 come from the October 2026 RoCE pilot. [`baselines/README.md`](../../baselines/README.md) records two cables, four interfaces, one repeat per point, 14 completed curves, and one excluded Qwen3-Next 80B NVFP4 single-node concurrency-128 row. The pilot summary index is [`baselines/rdma-pilot-2026-10/index.csv`](../../baselines/rdma-pilot-2026-10/index.csv). The original plots use Qwen3-Next 80B-A3B BF16 or NVFP4 configurations. They are not a general ranking of parallelism modes or a comparison isolated to the effect of precision.

The TTFT plot uses `ttft_p50`. The ITL plot uses median pooled token gaps `itl_p50`. The goodput plot uses `goodput_rps`, which qualifies each request against TTFT and per-request mean ITL targets. The GPU energy-per-token panel sums sampled GPU energy across participating nodes and divides by output tokens received; it excludes whole-system power. The pilot's request-level raw telemetry is absent from the local baseline checkout. The summary figures can be regenerated from the retained index, but request-level goodput and power samples cannot be recomputed from that checkout.

For the plotted Qwen3-Next 80B NVFP4 pilot, goodput is zero at concurrency 32 while the median TTFT and pooled median token-gap ITL curves remain below their plotted targets. This is consistent with the request-level qualification using different statistics. The retained summary plots do not identify each failed request's condition or mechanism.

## Reliability work and incident evidence

### Serving shutdown and cache cleanup

The user reports a historical overlap between stopping vLLM and deleting model-cache contents, followed by a crash and a locking change. The current scripts support the design principle: [`scripts/connectx_env.sh`](../../scripts/connectx_env.sh) implements a host resource lock with `flock` and idle checks; [`scripts/purge_model_cache.sh`](../../scripts/purge_model_cache.sh) obtains the lock and checks resource idleness before removal; [`scripts/run_job.sh`](../../scripts/run_job.sh) waits for serving resources to become idle during shutdown. The lock defaults to a host-local file in `/tmp`; the repository runbook explicitly states that it does not coordinate separate hosts without a shared lock filesystem.

The exact failing interleaving, process IDs, cache operation, crash message, and patch-level causal proof were not found in the retained material inspected. Unlinking an open Linux file does not by itself establish why a process would crash. The presentation labels the incident chronology as user-reported and the current ordering as verified implementation.

### Unexpected node failure

The user reports adapter swapping, head/worker role reversal, device-manager CPU saturation, a hardware diagnosis, and node replacement. The retained `cisc-hoedus` kernel artifacts contain fatal PCIe/NIC errors that the supplied PDF plan did not cite:

- [`scripts/results/node-postmortem-cisc-hoedus-20261026T193713Z/prev_boot_kernel.txt`](../../scripts/results/node-postmortem-cisc-hoedus-20261026T193713Z/prev_boot_kernel.txt) records `mlx5_pcie_event` warnings about insufficient PCIe slot power at boot.
- [`results/pcie-fail-and-high-load/pcie-fail-results.txt`](../../results/pcie-fail-and-high-load/pcie-fail-results.txt) records `mlx5_core 0002:01:00.1` at `2026-10-27T13:01:20.977463-04:00` reporting `Fatal error 1 detected`, then `PCI slot is unavailable`. Other `mlx5_core` functions report the PCI channel offline. A later excerpt in [`more-logs-pcie.txt`](../../results/pcie-fail-and-high-load/more-logs-pcie.txt) records recovery aborting because PCI reads were still not working.

The logs establish a PCIe/NIC path failure episode. They do not identify the defective physical component or demonstrate that replacement resolved every shutdown. The slide does not call the warnings alone the root cause. The user-reported diagnostic steps remain separate from the observed log lines.

[`scripts/system_snapshot.py`](../../scripts/system_snapshot.py) collects host, software, GPU, network, firmware, package, and container information without `sudo`. [`scripts/run_job.sh`](../../scripts/run_job.sh) invokes it at campaign startup and logs a failure without aborting. It is not a continuous monitor or a capture between every run. The retained snapshot at [`results/benchmark-2026-10-29-001/preflight/20261029-222325-278870/logs/system_snapshot.json`](../../results/benchmark-2026-10-29-001/preflight/20261029-222325-278870/logs/system_snapshot.json) has head-side host/container fields and an unavailable worker response; the worker inventory is incomplete in that example. [`scripts/node_postmortem.sh`](../../scripts/node_postmortem.sh) separately collects previous-boot journals, kernel matches, crash/pstore inventory, GPU temperature/power, memory, and container state. Root privileges are required for complete journal and pstore access.

The current campaign records failures and can continue independent legs after an isolated failure if shared resources return to an idle state. Preparation failures and untrusted shared state stop the campaign. Measurement calls use `--skip-done` to resume gaps in the result rectangle. Relevant code: [`scripts/run_job.sh`](../../scripts/run_job.sh), [`scripts/run_models.sh`](../../scripts/run_models.sh), and [`docs/campaign-runbook.md`](../../docs/campaign-runbook.md).

## Open checks before external presentation

1. Confirm the presenter line, individual contribution boundaries, collaborator credit, and permission to disclose lab photographs, logs, hostnames, and project data.
2. Add an approved photograph of the two-system setup. The HTML currently contains a labeled placeholder.
3. Recover the exact cable and switch topology for each plotted run. Four logical rails do not document every physical connection detail.
4. Recover both-rank NCCL transport logs, selected RoCE GID index, device mapping, and per-device counters for a matched TCP/RDMA serving comparison.
5. Recover actual ECN, CNP, and PFC configuration and counters before attributing performance or stability to congestion control.
6. Recover the reported 2048-to-4096 MTU adjustment's before/after evidence before claiming an effect.
7. Recover the shutdown/cache crash logs and exact file operation before stating a causal software mechanism.
8. Recover component diagnosis, replacement record, and post-replacement behavior before calling the node failure fully resolved.
9. Build an economic comparison with purchase price, switch/cables, power, utilization, and baseline service cost before stating that the cluster is economical.

No GPU workload, benchmark campaign, model download, network change, or hardware test was performed for these deliverables. Raw measurements and prior repository files were not modified.

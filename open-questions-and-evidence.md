# Presentation: open questions and supporting evidence

Review date: November 9, 2026. Slide numbers refer to the revised 24-slide HTML presentation. The methodology section is slide 14; the former slide 14 is now slide 15.

## Scope and source state

- The submission artifact is [index.html](index.html). Its pre-existing edits, embedded photographs, and measured chart series were preserved.
- Benchmark repository: `/home/dan/school/dgx-spark-llm-serving-benchmark`, commit `40e9e065d57ceebfbb3265d2d607b4f2650b2951`. The working tree was clean during inspection.
- PerfTest repository: `/home/dan/school/perftest-suite-dgx-spark-cluster`, commit `fc590f71d1e7d11894556b86323d723e58eacc66`. Its README and several local plotting artifacts had pre-existing changes.
- Presentation repository base: commit `9d5228065a5e2fcc651946c78e15dea8820a1128`. The HTML had pre-existing edits; the photograph directory and ZIP archive were untracked.
- The plotted serving pilot records harness commit `762bdc92e99ced180b41a7b169bf9e8ad92b165d` and methodology `steady-exact-v3`. That historical commit is available locally. Its workload generation, streaming timestamps, and metric definitions were inspected.
- Evidence sources include the presentation and research notes, baseline indexes and summaries, interconnect CSVs and table, PerfTest logs and CSVs, topology and readiness documents, measurement code, resource guards, and node postmortems in the three repositories.
- Proposed measurements below are future work. This review did not launch GPU workloads, change hardware or networking, download models, or regenerate raw measurements.

## Changes applied in this session

| Slide | Change |
| --- | --- |
| 3 | Added dated US advertised prices and direct seller citations. The Station comparison identifies BIZON's starting configuration. |
| 5 | Corrected `redunancy` to `redundancy`. The failover hypothesis remains a hypothesis. |
| 7 | Removed the entire bottom note containing the blanket statistical description. |
| 8 | Added a first-hand forum citation for the 100 Gb/s per-interface TCP reference. Changed embedded reference labels from limits to references. The 126 Gb/s line identifies the PCIe host link. |
| 12 | Added the Spark-specific GPUDirect RDMA limitation and registered host-memory buffer note with NVIDIA's porting-guide citation. |
| 13 | Replaced the bandwidth caption with all-reduce and send/receive values for TCP and RoCE at 1 GiB. Kept a general controlled-comparison caveat without discussing cabling on the slide. |
| 14 | Added the retained serving pilot's workload, runtime, cache settings, timing, load mode, and repeat count. |
| 15 | Replaced the CPU-reservation claim with the vLLM 0.80 setting and intended system headroom. Removed the nominal budgets from that sentence. |
| 19 | Removed the KV-cache thrashing explanation and prediction about more nodes passing the target. Added the measured mean-ITL observation and unresolved mechanism. |

The 10-, 20-, and 30-node studies remain future research on larger models. Their model assignments were not added to the slides.

## Retained serving conditions

These facts describe the figures on slides 15 and 17–19. They do not describe every historical campaign or the current default campaign.

| Field | Retained value |
| --- | --- |
| Model family | Qwen3-Next-80B-A3B-Instruct |
| BF16 checkpoint | `Qwen/Qwen3-Next-80B-A3B-Instruct` at `9c7f2fbe84465e40164a94cc16cd30b6999b0cc7` |
| NVFP4 checkpoint | `nvidia/Qwen3-Next-80B-A3B-Instruct-NVFP4` at `8fb2682f136cf94d932a498f18cb1e428832a912` |
| Tokenizers | Checkpoint-specific tokenizer identifiers and revisions match the corresponding model identifiers and revisions in the retained policies. |
| Configurations shown | BF16: TP=2 and PP=2. NVFP4: one Spark, TP=2, and PP=2. |
| Plotted concurrencies | 1, 2, 4, 8, 16, 32, 64 |
| Load mode | Closed loop |
| Request workload | Input/output token buckets 128/128, 1024/256, 4096/256, 8192/512; relative weights 1, 1, 1, 0.5; seed 1234 |
| Generation | Streaming completions; temperature 0; fixed requested output length through equal minimum/maximum tokens and ignored EOS |
| Timing | 120 s configured warmup, 1500 s measurement, 180 s configured cooldown; recorded boundary extensions are separate fields |
| Replicates | One run per point |
| vLLM | `0.19.0+6bc3197f.nv26.04.48680843` |
| Container | `nvcr.io/nvidia/vllm@sha256:98494fdaea68ad892c107180b0be41c99caa3c77683175becc4e202b2cb75b27` |
| Executor memory setting | `gpu_memory_utilization=0.80` |
| Context limit | 8704 tokens |
| Prefix caching | Disabled |
| Compute dtype setting | `auto`; the retained setting alone does not establish every kernel's arithmetic precision |
| KV-cache setting | BF16 checkpoint: `auto`; NVFP4 checkpoint: `fp8_e4m3` |
| Strict goodput objectives | Request TTFT ≤ 3 s and request mean ITL ≤ 0.10 s |
| Throughput cohort | Output token IDs received during the measurement window, including requests that started outside it |
| Latency/goodput cohort | Requests started during the measurement window and tracked to completion |
| Energy scope | Reported GPU device power, integrated during the window and summed across participating nodes; divided by output tokens received during the window |

Sources: [pilot index](../dgx-spark-llm-serving-benchmark/baselines/rdma-pilot-2026-10/index.csv), [baseline documentation](../dgx-spark-llm-serving-benchmark/baselines/README.md), and the pilot's `*.summary.json` and `serving_policy_*.json` files. A representative record is the [NVFP4 TP=2 concurrency-16 summary](../dgx-spark-llm-serving-benchmark/baselines/rdma-pilot-2026-10/qwen3-next-80b-nvfp4_tp2_closed_16_r1_20261013-160054-994365172.summary.json).

## 1. Historical TCP/RoCE comparison cannot isolate transport benefit

- **Supported evidence:** The [table beside the embedded figure](../dgx-spark-llm-serving-benchmark/results/tcp-rdma-interconnect-comparison/figs/stats/interconnect_table.md) reports largest-message all-reduce bandwidth of 2.12 GB/s TCP and 21.18 GB/s RoCE, and send/receive bandwidth of 3.05 GB/s TCP and 24.09 GB/s RoCE. The table contains two TCP runs and one RoCE run per primitive.
- **Remaining concern:** The [baseline records](../dgx-spark-llm-serving-benchmark/baselines/README.md) identify different historical cabling/interface configurations. Source and software conditions also differ. The presentation intentionally omits the cabling detail on slide 13.
- **Explanation available now:** These are historical configuration results. Their ratio does not establish an isolated benefit from replacing TCP with RoCE.
- **Proposed resolution:** Recover exact per-run commands, both-rank NCCL logs, software identities, device selections, and topology records. A later transport ablation would hold hardware, topology, image, source, message sizes, and timing procedure fixed while changing the selected transport.
- **Evidence boundary:** The RoCE curve on slide 13 matches the comparison PNG. Its retained interconnect source includes an October 22 RoCE CSV under `results/results-rdma-v8/`; the October pilot's separate all-reduce CSV is not interchangeable with that source. The older research notes' 23.564 GB/s pilot value does not describe the slide's all-reduce endpoint.

## 2. Application references and wire utilization need separate definitions

- **Supported evidence:** [NVIDIA's networking guide](https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html) identifies two PCIe Gen 5 ×4 host links and two up-to-200-Gb/s physical ports. The [retained kernel log](../dgx-spark-llm-serving-benchmark/results/pcie-fail-and-high-load/more-logs-pcie.txt) reports 126.028 Gb/s for a ×4 link. Adding two such reported link capacities gives 252.056 Gb/s before transaction overhead. This is derived arithmetic.
- **Forum evidence:** [eugr's November 27, 2025 report](https://forums.developer.nvidia.com/t/connectx-7-nic-in-dgx-spark/350417/47) describes approximately 100 Gb/s on each of two concurrent TCP interface paths. [A January 10, 2026 switched-fabric report](https://forums.developer.nvidia.com/t/connectx-7-200gbe-via-mikrotik-crs812-qsfp-dd-400g-2xqsfp56-200g-breakout/357162/5) describes using both logical halves of a physical port. These are reports for their stated configurations.
- **Remaining concern:** Approximately 25 GB/s corresponds to 200 Gb/s aggregate. It does not establish a 100 Gb/s hard limit for every logical interface, verb, or application. Slide 8's isolated measurements exceed 100 Gb/s. Dividing an aggregate result by two requires evidence that the relevant paths share traffic equally.
- **Explanation available now:** Slide 8 uses the forum result as a per-interface application reference and the kernel-derived value as a PCIe reference. Slide 13 reports aggregate NCCL bus bandwidth.
- **Proposed resolution:** Preserve per-interface byte counters and the selected NCCL channel/device mappings during a later matched run. Report application payload throughput separately from Ethernet wire utilization. [NVIDIA's NCCL performance definitions](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md) define bus bandwidth through collective-dependent normalization.

## 3. PerfTest replication and aggregation remain heterogeneous

- **Supported evidence:** Slide 8's embedded chart pools 64 KiB isolation measurements from `PRE-OCT13-REWORK/dual-200Gb-Oct-8` and `PRE-OCT13-REWORK/test-oct-6`. Its bars are means, its whiskers are min–max, and bidirectional rates are halved for a per-direction display. The chart records six device instances and ten repeats per device.
- **Supported evidence:** Slide 9's figure labels its bands as min–max across campaigns, repeats, and devices. It uses 2-byte send/write/read and 8-byte atomic operations.
- **Supported evidence:** Slide 10's `perftest-nov5` write model has two paired isolated runs and one paired concurrent run per device and direction. The current [plotting code](../perftest-suite-dgx-spark-cluster/plot_perftest.py) selects client measurements with host fallbacks by link identity. The selected model inputs were inspected without generating figures.
- **Remaining concern:** One concurrent run cannot establish run-to-run variation. The client `run-002/results.csv` contains 30 error rows and no largest-payload concurrent write measurements. The reason for that incomplete run requires the paired logs.
- **Explanation available now:** The three figures use different aggregation schemes and different retained campaigns. None supplies a campaign-wide uncertainty estimate for serving performance.
- **Proposed resolution:** Add a source/count table to a future appendix. Preserve failed measurements and state the exclusion/fallback rules. Obtain repeated isolated and concurrent measurements under matched conditions only as a separately authorized experiment.

## 4. Hockney estimates require volume and validation boundaries

- **Supported evidence:** [The plotting implementation](../perftest-suite-dgx-spark-cluster/plot_perftest.py) pairs each run's smallest-payload typical latency with its largest-payload average bandwidth and computes `T = L + V/B` for decimal volumes of 0.1, 1, 10, and 100 GB. It plots per-device curves.
- **Remaining concern:** The bidirectional bandwidth is aggregate across directions. Its volume must therefore be aggregate across directions. A 1 GB one-way payload and 1 GB in each direction are different amounts of transferred data.
- **Remaining concern:** These straight-line projections do not independently validate sustained 100 GB transfers or predict a sequence of small collective exchanges. Startup, registration, connection setup, synchronization, and teardown are outside the model.
- **Explanation available now:** Slide 10 is a data-phase estimate under an assumed sustained bandwidth. Its modeled points are not independently timed transfers.
- **Proposed resolution:** Define volume explicitly in a future caption. Compare predictions with independently measured data-phase intervals at several volumes and report prediction error. The separate [transfer-suite guide](../perftest-suite-dgx-spark-cluster/rdma-transfer-suite/README.md) also derives data-phase time from bandwidth; its client process wall time includes setup and teardown and cannot serve as a direct data-phase reference.

## 5. PerfTest latency is not end-to-end application latency

- **Supported evidence:** The [upstream PerfTest methodology](https://github.com/linux-rdma/perftest) describes round-trip-based latency reporting and notes asymmetry limitations. The retained logs record RC verbs commands and CPU-driven microbenchmarks.
- **Remaining concern:** A pairwise verbs latency does not establish GPU collective latency, token generation latency, or one physical propagation delay. The host, PCIe path, memory, completion handling, and selected operation contribute.
- **Explanation available now:** Slide 9 characterizes a host-driven pairwise operation under its test conditions. Slide 13 measures another layer of the stack.
- **Proposed resolution:** Keep operation, payload, memory type, connection type, and timestamp convention available for questions. Avoid adding the microbenchmark latency directly to each model layer without tracing the model's actual exchanges.

## 6. Median token gaps and request mean ITL answer different questions

- **Supported evidence:** The pilot's `itl_p50` pools token gaps; `mean_itl_p50` is the median of request means. Strict goodput qualifies individual requests using TTFT and mean ITL. The historical `bench/metrics.py` at the pilot commit and the [current metric implementation](../dgx-spark-llm-serving-benchmark/bench/metrics.py) retain that distinction.
- **Supported evidence:** The historical streaming client assigns the same reception timestamp to multiple token IDs received in one stream event. Those tokens contribute zero within-event gaps. The [current client](../dgx-spark-llm-serving-benchmark/bench/client.py) also records client arrival times rather than server decode-step timestamps.
- **Remaining concern:** A pooled median can remain below the target while request means exceed it. Stream-event batching can also affect the token-gap distribution. The absent pilot raw streams prevent quantifying that contribution in this checkout.
- **Explanation available now:** Client reception-gap p50 and request mean reception-gap latency are different statistics. The current ITL caption states the pooled-versus-mean distinction; the plot axis still uses the shorter `ITL` label.
- **Proposed resolution:** Label a future plot `client token-gap p50` and display request mean-ITL percentiles beside goodput. Recover raw stream records before attributing the shape of the token-gap distribution to GPU execution behavior. Use server-side timing only if a separately authorized instrumented run provides it.

## 7. The mechanism behind zero strict goodput remains unverified

At concurrency 32, the retained pilot index reports:

| Configuration | Request mean ITL p50 | Reported peak cache occupancy | Recorded preemptions | Failed requests |
| --- | ---: | ---: | ---: | ---: |
| One Spark | 150.68 ms | 5.962% | 0 | 0 |
| TP=2 | 112.65 ms | 2.064% | 0 | 0 |
| PP=2 | 123.15 ms | 2.076% | 0 | 0 |

- **Supported evidence:** [The pilot index](../dgx-spark-llm-serving-benchmark/baselines/rdma-pilot-2026-10/index.csv) and the three concurrency-32 summaries contain these values. The sampled cache metric is a reported vLLM metric, not an independent inventory of every memory allocation.
- **Remaining concern:** These counters do not support cache-capacity exhaustion as the explanation. They do not identify a unique compute, memory-bandwidth, scheduling, communication, or software mechanism.
- **Explanation available now:** Strict goodput reaches zero while throughput remains positive and requests complete. The request-level 100 ms mean-ITL objective is exceeded. More nodes are not established as the remedy by the retained measurements.
- **Proposed resolution:** Recover any retained scheduler/preemption logs and correlate request, batch, GPU, CPU, and NIC observations. Profiling or a controlled diagnostic comparison requires new measurements. Treat each possible cause as a hypothesis until that evidence exists.

## 8. BF16/NVFP4 results do not isolate weight precision

- **Supported evidence:** The checkpoints have different immutable revisions and different KV-cache settings. Both use a compute dtype setting of `auto`; the NVFP4 entry uses `fp8_e4m3` KV cache while BF16 records `auto`.
- **Remaining concern:** Weight representation, cache representation, kernels, and supported placements can all affect the comparison. No task-quality evaluation is presented with the serving results.
- **Explanation available now:** Slide 15 compares retained serving configurations. It does not establish an isolated speedup from weight quantization or equal task accuracy.
- **Proposed resolution:** Describe both configurations completely. A later precision ablation would keep placement, workload, cache dtype, and software fixed where supported and report any unavoidable differences. Assess task quality on a declared evaluation set before making accuracy-equivalence claims.
- **Model scope:** [Qwen's model card](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct) identifies an 80B-total, 3B-active mixture-of-experts model with hybrid attention. Its communication and memory behavior do not represent every dense model of similar total parameter count.

## 9. One run per point limits comparative claims

- **Supported evidence:** The 35 shown Qwen pilot summaries contain `repeat_count=1`; all 35 files matched their indexed SHA-256 values during the review. The single-Spark NVFP4 concurrency-128 point is excluded from the baseline index and figures, as documented in the baseline README. All presentation serving plots stop at 64.
- **Remaining concern:** Within-run request counts do not measure launch-to-launch variation. The retained pilot raw request, power, and vLLM sample files are absent from this local baseline checkout. Summary hashes establish file identity, not independent recomputation of the underlying measurements.
- **Explanation available now:** The curves are preliminary retained measurements. Their medians and observed ordering do not establish confidence intervals or repeatability.
- **Proposed resolution:** Preserve the pilot unchanged. Recover raw telemetry and original logs from the measurement hosts or archives. The current campaign plan specifies three independent launches per curve, but a plan is not proof that those measurements exist. Local newer result indexes found during this review were four-row hardware-smoke outputs, rather than a completed replacement Qwen campaign.

## 10. Replication is an unmeasured alternative for models that fit on one Spark

- **Supported evidence:** The NVFP4 checkpoint ran on one Spark. At concurrency 16, the pilot reports 0.624 requests/s strict goodput and 0.316057 J/output-token on one Spark; TP=2 reports 0.840 requests/s and 0.428326 J/output-token.
- **Derived comparison:** At that tested total concurrency, TP=2 improves strict goodput by approximately 34.6% while sampled GPU energy/output-token increases by approximately 35.5%. The calculations are `(0.840/0.624 - 1) × 100` and `(0.428326/0.316057 - 1) × 100`.
- **Remaining concern:** Two independent single-node replicas were not measured together. Doubling one isolated replica's throughput would be a hypothetical capacity estimate, not a cluster measurement.
- **Explanation available now:** Sharding supports placement across memory domains and changed the observed latency/throughput. The pilot does not establish the best service architecture for aggregate requests when the model fits locally.
- **Proposed resolution:** Distinguish capacity for one larger model from aggregate capacity for many requests. A future replica baseline would use the same two nodes, total offered load, workload mix, routing overhead, and measurement boundaries as the sharded comparison.

## 11. Communication's share of token latency is unmeasured

- **Supported evidence:** PerfTest measures verbs operations; NCCL microbenchmarks measure collectives and send/receive; the serving pilot measures client-visible requests. The TP/PP diagram is conceptual.
- **Remaining concern:** No retained trace maps the selected model's actual collective counts, payload sizes, synchronization, overlap, and buffer transfers onto its token timings. The diagram's all-reduce labels are not a trace of every layer's implementation.
- **Explanation available now:** Fabric capability and serving behavior are separately measured. Their association does not identify communication as the dominant bottleneck.
- **Proposed resolution:** Recover any existing profiler traces. A later instrumented run could report prefill versus decode time, collective sizes and durations, host-buffer handling, overlap, and compute time. Explain only the layers actually measured until that decomposition exists.

## 12. Failover needs application recovery criteria

- **Supported evidence:** Slides 5 and 22 propose interface bonding for failover. The topology provides two physical ports with shared NIC and host resources. No retained failover campaign was found in the inspected artifacts.
- **Community evidence:** [The ConnectX-7 discussion](https://forums.developer.nvidia.com/t/connectx-7-nic-in-dgx-spark/350417?page=3) reports bonding attempts that affected NCCL operation. A [2026 switched-cluster discussion](https://forums.developer.nvidia.com/t/dgx-spark-4-8-cluster-switch-options-post-mikrotik-crs-804-mikrotik-crs-812-market-wipe-out/384594?page=3) reports that interrupted inference connectivity can require restarting serving. Neither report establishes behavior for this repository's proposed configuration.
- **Remaining concern:** Ethernet connectivity after a failure does not establish survival of active RDMA connections, NCCL collectives, or in-flight inference. Port redundancy shares NIC and node failure domains.
- **Explanation available now:** Redundancy and heavy-load bandwidth are test hypotheses. The active application may require recovery or restart.
- **Proposed resolution:** Specify bond mode, physical-port membership, same-PCIe-domain relationships, IP/GID changes, and failure scope. A later test would record healthy bandwidth, interruption duration, request failures, collective failure, recovery procedure, and post-recovery bandwidth after a declared cable or port failure.

## 13. The switched path needs observed configuration records

- **Supported evidence:** Slide 23 identifies the current switched pair as research-team reported. [The current cluster YAML](../dgx-spark-llm-serving-benchmark/configs/cluster.yaml) describes configured host interfaces and addresses. It does not prove a switch's physical cabling or settings for an older experiment.
- **Remaining concern:** `400 Gb/s network switch` does not identify switch model, per-port modes, breakout configuration, fabric capacity, or oversubscription. PFC, ECN, congestion notification, priorities, and drop counters are not established by using RoCEv2.
- **MTU evidence:** The saved [Ethernet link capture](../perftest-suite-dgx-spark-cluster/perftest-results/trans-test-update/client/run-001/environment/rocep1s0f0/link.json) records MTU 9000; [the matching verbs capture](../perftest-suite-dgx-spark-cluster/perftest-results/trans-test-update/client/run-001/environment/rocep1s0f0/ibv_devinfo.txt) records active/max MTU 4096. These describe different protocol layers. They do not document every serving run.
- **Explanation available now:** The switch diagram records the reported arrangement and proposed expansion. It is not a verified switch inventory or congestion-control diagnosis.
- **Proposed resolution:** Recover switch model, firmware, port/breakout mapping, negotiated rates, MTUs, congestion settings, and counters from both endpoints and the switch. Distinguish host setup instructions from observed run captures.

## 14. Cleanup incident chronology and lock guarantees have limits

- **Supported evidence:** [The research notes](research-notes.md) identify the shutdown/cleanup sequence as user-reported. [The resource lock](../dgx-spark-llm-serving-benchmark/scripts/connectx_env.sh) and [purge wrapper](../dgx-spark-llm-serving-benchmark/scripts/purge_model_cache.sh) implement cooperative locking and idle checks. The default lock file is host-local.
- **Remaining concern:** The exact historical file operation, process interleaving, crash message, and patch-level causal proof were not found. A current safeguard does not prove the historical cause. A host-local lock does not coordinate independent operations on another host unless the deployment supplies additional coordination.
- **Explanation available now:** Slides 20–21 illustrate a reported overlap and the current ordering safeguard. The lock serializes participating operations that use the same lock.
- **Proposed resolution:** Recover a dated incident log and before/after patch or test evidence. Keep `reported` and `schematic` qualifiers if those records remain unavailable. Describe lock scope explicitly when answering implementation questions.

## 15. PCIe/NIC errors establish a failure episode, not a defective component

- **Supported evidence:** [The retained error report](../dgx-spark-llm-serving-benchmark/results/pcie-fail-and-high-load/pcie-fail-results.txt) and [additional kernel log](../dgx-spark-llm-serving-benchmark/results/pcie-fail-and-high-load/more-logs-pcie.txt) contain `Fatal error 1 detected`, `PCI slot is unavailable`, offline PCI channels, and failed recovery. Boot warnings mention PCIe slot power.
- **Remaining concern:** These logs do not isolate the PSU, NIC, board, firmware, driver, or another physical component. The inspected records do not establish that a replacement resolved every failure.
- **Explanation available now:** A PCIe/NIC-path failure occurred. Component diagnosis and resolution remain separate claims requiring their own records.
- **Proposed resolution:** Preserve the full chronology, role/cable/adapter swaps, support diagnosis, replacement identifiers, and post-replacement observations if available. A log excerpt could provide an auditable reliability example in a later presentation revision.

## 16. GPU energy and advertised prices do not establish total cost

- **Supported evidence:** The sampled energy metric sums the participating GPUs' reported power and divides by output tokens. It excludes wall power, CPU, network switch, storage, cooling, and other unmeasured domains. At NVFP4 TP=2 concurrency 32, the retained summary records 14,971 head samples and 1,495 worker samples over 1500 s; both streams were not sampled at the same effective cadence.
- **Remaining concern:** GPU joules/output-token is not system joules/output-token, joules per SLO-qualified request, or acquisition/operating cost. Nominal aggregate RAM and sparse FP4 peaks do not establish equivalent sustained inference capability.
- **Price evidence, checked November 9, 2026:** The rendered [NVIDIA US listing](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/) shows $6,950 for the 128 GB/4 TB Spark and marks it out of stock. [BIZON's GB300 page](https://bizon-tech.com/gb300.html) advertises a 748 GB Station starting at $132,159 with US ordering. The derived ratio is `132159/6950 = 19.016`, displayed as 19.0×. This is one seller's starting configuration, not a universal Station price or a binding procurement quote. Taxes and shipping were not compared.
- **Source discrepancy:** A cached search result for NVIDIA's page still reported $4,699. The rendered manufacturer listing was used instead. Other Station sellers advertise different configurations and prices.
- **Explanation available now:** The deck compares published capacities, advertised prices, and measured GPU telemetry under separate labels. It does not establish an economical replacement for a Station or datacenter system.
- **Proposed resolution:** Obtain comparable dated configuration quotes before procurement claims. A separately authorized energy study would use declared whole-system measurement boundaries and record idle/load baselines, sampling coverage, successful output, and SLO-qualified work.

## 17. Larger-cluster context and harness readiness are separate

- **User-defined scope:** The 10-, 20-, and 30-node targets concern future larger models. No model assignments or parallelism geometry were added to the presentation.
- **Current vendor evidence:** NVIDIA's [October 22, 2026 announcement](https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/) states official eight-node support and says eight-node NVIDIA Sync support is expected by year-end. The [current setup guide](https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html) still describes the guided three-node direct/four-node switched workflow. A blanket statement that NVIDIA supports only four nodes is incomplete.
- **Local implementation evidence:** [The current topology loader](../dgx-spark-llm-serving-benchmark/scripts/cluster_topology.py) rejects configurations other than exactly two nodes. [The topology design](../dgx-spark-llm-serving-benchmark/docs/two-spark-topology-design.md) identifies larger switched operation as later work. The branch name does not establish arbitrary-node support.
- **Remaining concern:** Local two-node measurements do not establish 10–30-node scaling or current harness support at those sizes. The vendor's newer examples use their stated models, software, topology, and collective backend.
- **Explanation available now:** The presentation reports two-node groundwork and planned expansion. NVIDIA's larger examples provide platform context, not results from this project.
- **Proposed resolution:** Treat node-count support, measurement schema, telemetry coverage, recovery behavior, and larger-model measurements as requirements for the future expansion. Verify those requirements against the implementation before claiming a larger campaign has run.

## 18. The closing sequence can state the supported engineering result

- **Supported evidence:** At tested concurrency 16, TP=2 provides the pilot's highest NVFP4 goodput among the displayed configurations, with the GPU-energy tradeoff in section 10. All three displayed configurations have zero strict goodput at 32 and 64. Concurrent PerfTest paths share resources rather than acting as four independent full-rate physical links.
- **Remaining concern:** Slide 22 lists evidence categories and a next test without stating a quantitative outcome. Slides 1–6 allocate six screens to framing before the first measured result. The deck now contains 24 slides.
- **Explanation available now:** The pilot establishes configuration-specific serving behavior and fabric observations. It leaves the dominant mechanism, repeatability, and larger-cluster behavior open.
- **Proposed resolution:** In a later revision, use the measured concurrency-16 goodput and GPU-energy values as the closing comparison. Rehearse against the actual interview time allocation and retain the present caveats. A new GPU experiment is not required to state the existing measured outcome.

## 19. Reproduction and visual validation remain incomplete

- **Supported evidence:** [The precision regeneration script](generate_precision_c64.py) resolves `ROOT` through `parents[2]`, which yields `/home/dan` in the current layout. Its expected plotting and baseline paths therefore do not point to the sibling benchmark repository. It was not executed or modified in this session.
- **Supported evidence:** [The older research notes](research-notes.md) describe 22 slides and earlier placeholders, source mappings, and slide numbers. The revised presentation has 24 slides and embedded photographs.
- **Remaining concern:** The presentation HTML is approximately 52 MB, largely from embedded photographs. Live browser viewport behavior, fullscreen navigation, and print pagination have not been verified during this review. The browser security policy blocked opening local `file:` URLs. No alternate browser path was used to bypass that restriction.
- **Proposed resolution:** Repair the regeneration path and refresh the evidence manifest in a separately requested repository change. Check the final HTML at 1920×1080, 1366×768, and 1280×720 and inspect print output before submission. Image compression would be a separate requested artifact change.
- **Checks completed here:** Parsed all slide content; checked sequential slide IDs/counters and anchor targets; checked for runtime scripts and external asset dependencies; checked English spelling candidates; compared embedded measured marks and unmodified assets with the pre-edit HTML; inspected the relabeled SVG with librsvg. These checks do not establish live browser layout or keyboard behavior.

## Evidence recovery and proposed follow-up order

| Priority | Work | Evidence available now | Additional requirement |
| --- | --- | --- | --- |
| 1 | Prepare answers for SLO, ITL, precision, transport, and cost questions | Retained summaries, policies, code, and cited sources | No hardware run required for the stated boundaries |
| 1 | Recover pilot raw request/power streams and original server/NCCL logs | Indexed paths, hashes, and summaries | Access to existing archives or measurement hosts |
| 1 | Verify final presentation display and timing | Self-contained HTML | Live browser/fullscreen/print inspection and rehearsal |
| 2 | Define switch topology and failover criteria | Config files, retained link captures, proposed diagram | Observed switch configuration and an agreed failure scope |
| 2 | Repair reproduction script and stale evidence notes | Identified local path and slide-count mismatches | A separate authorized file change |
| 3 | Quantify repeatability and isolated transport benefit | Current campaign/readiness procedures and historical baselines | New matched, replicated measurements |
| 3 | Explain high-concurrency behavior and compare replicas | Request summaries and scheduler counters | Controlled diagnostics/profiling and replica measurements |
| 3 | Validate failover and larger-model scaling | Two-node implementation and vendor references | Authorized fault-injection and scale-out experiments |

No new experiment, model download, source-code correction, or artifact compression is authorized by this document.

# Revised networking talk

The revised presentation is [revised index.html](<revised index.html>). The original 25-slide [index.html](index.html) is preserved. The revised sequence has 18 slides and retains the existing visual theme, embedded figures and fonts, static navigation, and print styling.

## Storyline

The research question is whether desktop nodes can add model capacity while keeping communication within interactive latency targets.

The evidence sequence is:

1. Physical ports and logical paths share host-link resources.
2. PerfTest measures operation-level bandwidth and latency independently of serving.
3. The preliminary direct/switch comparison records higher short-message latency with similar isolated bandwidth. The switch contribution remains unmeasured.
4. Model placement determines collective and point-to-point traffic. NCCL measurements characterize another layer of the stack.
5. Request-level latency targets connect the serving measurements to useful request capacity.
6. The next controlled tests separate network cost from local decoding cost before expansion.

## Planned reduction

The editing budget allocates **220 seconds, or 3 minutes 40 seconds**, of reduction. This estimate assumes the original delivery included the removed explanations. Actual rehearsal timing is unmeasured.

| Original slide or material | Revision | Allocated reduction |
|---|---|---:|
| 3: DGX Station specifications and prices | Remove the platform purchasing comparison | 45 s |
| 4: Separate two-node and 10/20/30-node overview | Fold the research scope into revised slide 2 | 10 s |
| 10: Modeled fixed-volume transfer times | Remove this derived-result detour and the Hockney formula introduction | 35 s |
| 15: Precision and GPU energy comparison | Keep the serving results focused on the NVFP4 case | 40 s |
| 20: Separate target-attainment graph | Carry the percentage result in the goodput caption | 20 s |
| 21: Separate prefill/decode hypothesis explanation | Carry the conditional memory/communication hypothesis into the next-test slide | 30 s |
| 22: Generic fabric/serving/reliability framework | State the controlled tests directly in the closing slide | 20 s |
| Introduction, topology, and methodology copy | Shorten repeated explanations and remove unused metric introductions | 20 s |
| **Total allocated reduction** | | **220 s** |

The original contains the removed figures for questions about purchasing, modeled transfers, precision, energy, target attainment, or the prefill/decode distinction.

## Speaking cues and slide mapping

Use one finding or question per screen. The cues identify the point to deliver; they are not a word-for-word script.

| Revised | Original | Speaking cue |
|---:|---:|---|
| 1 | 1 | Can distributed capacity remain useful once communication is included? |
| 2 | 2, with the scope from 4 | Splitting model state adds synchronization and activation traffic. Larger studies remain planned. |
| 3 | 5 | Two physical ports expose four logical devices; logical paths share resources. |
| 4 | 6 | Port ratings and host-link references differ. Sustained throughput requires measurement. |
| 5 | 7 | I built orchestration and evidence capture around verbs microbenchmarks. Verify successful overlap for concurrent measurements. |
| 6 | 8 | Isolated one-way payload bandwidth is approximately 109 Gb/s per interface. This does not establish concurrent aggregate capacity. |
| 7 | 9 | Short messages expose the delay of pairwise exchanges. These are host-driven verbs measurements. |
| 8 | 23 | The switched testbed records higher short-message latency and similar isolated bandwidth. The cause remains unverified. |
| 9 | 11 | Tensor and pipeline placement create different communication patterns. |
| 10 | 12 | Ray places workers; NCCL carries tensor traffic. Spark RDMA uses registered host-memory buffers. |
| 11 | 13 | Historical NCCL results show transport-associated differences. Different conditions prevent an isolated transport-speedup claim. |
| 12 | 14 | One declared NVFP4 model and mixed workload are compared across single, TP=2 and PP=2. Each point has one run. |
| 13 | 16 | Each qualifying request must meet both the TTFT and mean-ITL targets. |
| 14 | 17 | Median TTFT stays below 3 s. This alone does not establish request qualification. |
| 15 | 18 | Median request mean ITL exceeds 100 ms at concurrency 32 in all three configurations. |
| 16 | 19, with the percentage result from 20 | TP=2 peaks at 0.840 qualifying requests/s. Target attainment falls from 98.2–100% at concurrency 16 to zero at 32 and 64. |
| 17 | 24, with the hypothesis from 21 | Repeat the direct/switch test at fixed conditions, verify transport, and profile local and network costs before expansion. |
| 18 | 25 | Invite questions. |

## Retained distinctions

- Port and PCIe reference rates are distinct from measured application bandwidth.
- Isolated measurements do not establish successful concurrent aggregate throughput.
- PerfTest verbs bandwidth, NCCL bus bandwidth, and serving goodput are different metrics.
- Historical TCP/RoCE results and the direct/switch campaigns do not isolate a single causal variable.
- ITL uses the median across request mean ITLs. Goodput counts requests meeting both targets per measured second.
- The percentage result uses all requests started in the measurement window as its denominator.
- Memory-bandwidth saturation, switch-added latency, and gains from more nodes remain unverified hypotheses or proposed measurements.

## Checks and remaining validation

The original file's SHA-256 is checked against its value before the copy was edited. The revised file's numbering, navigation, retained figure bytes, embedded font bytes, and absence of runtime JavaScript are checked separately.

Fullscreen layout and keyboard behavior have not been browser-tested. The browser security policy blocks local-file URLs. The 3:40 reduction requires a timed rehearsal.

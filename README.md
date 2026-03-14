# Resonance Centrality 🐬🐦🦇✨

**A composite metric revealing two structurally distinct classes of important individuals in animal social networks**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19009607.svg)](https://doi.org/10.5281/zenodo.19009607)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-brightgreen?style=flat-square)](https://python.org)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.6+-orange?style=flat-square)](https://networkx.org)
[![Status](https://img.shields.io/badge/status-peer--review-yellow?style=flat-square)](https://doi.org/10.5281/zenodo.19009607)

---

Betweenness centrality has been the standard lens for animal network analysis for two decades — but it only sees **half the picture**. It finds the routing hub. It misses the quality anchor.

**Resonance Centrality** finds both.

- **Grins** → routing hubs that keep everyone connected (high betweenness)
- **Beescratches** → quality anchors that build the richest local neighborhoods (invisible to betweenness)
- **True Grins** → rare super-nodes dominating both roles simultaneously

Validated across four datasets spanning three species, all at the **100th percentile** against 100 null permutations, with effect sizes ranging from **5.76σ to 29.88σ** — well beyond physics discovery thresholds.

**Preprint:** [doi.org/10.5281/zenodo.19009607](https://doi.org/10.5281/zenodo.19009607)  
**Submitted to:** *Animal Behaviour*

---

## The Formula

```
RC = (Rhythm × 0.4) + (Coherence × 0.4) + (Bridging × 0.2)
```

| Component | What it measures | Weight |
|-----------|-----------------|--------|
| **Rhythm** | Normalized degree centrality — how socially connected? | 0.4 |
| **Coherence** | Neighborhood density — how rich and interwoven is their circle? | 0.4 |
| **Bridging** | Normalized betweenness — how much does the network route through them? | 0.2 |

> **Critical implementation note:** Betweenness must be computed with `weight='weight'`. Using NetworkX's default (unweighted) produces structurally incorrect results on weighted networks.

---

## Validation

| Dataset | Species | Nodes | Edges | Effect size | Percentile | Top class |
|---------|---------|-------|-------|-------------|------------|-----------|
| Doubtful Sound | Bottlenose dolphin | 62 | 159 | **17.72σ** | 100th | Beescratch |
| Network_639 | Sociable weaver | 42 | 152 | **29.88σ** | 100th | Beescratch |
| Network_658 | Sociable weaver | 24 | 62 | **9.73σ** | 100th | True Grin ⭐ |
| Network_505 | Vampire bat | 21 | 124 | **5.76σ** | 100th | Grin + Beescratch |

Effect sizes above 5σ exceed the threshold for discovery claims in particle physics. The 29.88σ weaver result is not a number that happens by accident in real biological data.

These are not artifacts. Grins and Beescratches are non-overlapping individuals in every validated dataset. Removal experiments confirm functionally distinct structural roles.

---

## Quick Start

```bash
git clone https://github.com/barbarajkeiser-MarsLoop/Resonance-Centrality.git
cd Resonance-Centrality
pip install networkx numpy scipy pandas matplotlib
```

**Run from command line:**

```bash
python resonance_centrality.py \
  --input your_network.graphml \
  --output results.csv \
  --permutations 100 \
  --weight weight
```

**Use in Python:**

```python
import networkx as nx
from resonance_centrality import compute_resonance

G = nx.read_graphml("your_network.graphml")
results = compute_resonance(G, weight='weight')

# Top nodes by resonance score
print(results.sort_values('resonance', ascending=False).head(10))

# Find Grins and Beescratches
grins = results[results['node_class'] == 'Grin']
beescratches = results[results['node_class'] == 'Beescratch']
```

**Run null-model validation:**

```python
from null_case_validation import run_permutation_test

sigma, percentile = run_permutation_test(G, n_permutations=100, weight='weight')
print(f"Effect size: {sigma:.2f}σ | Percentile: {percentile}th")
```

---

## Node Classes

**Grin** — The routing hub. High betweenness, lower neighborhood coherence. This is the individual betweenness centrality was built to find. Remove a Grin and paths get longer.

**Beescratch** — The quality anchor. High resonance score, low betweenness. Invisible to standard analysis. These individuals maintain the richest, most densely interconnected local neighborhoods in the network. They are not bridges — they are hubs of local cohesion.

**True Grin** — The rarest class. An individual that simultaneously maximizes both routing (high betweenness) and local coherence (high resonance). First confirmed: individual DBMREBK in sociable weaver colony Network_658. Removal of DBMREBK increased average path length by +0.742 — the largest single-node disruption across all validated datasets.

The key finding: **Grins and Beescratches are never the same individual.** They represent two genuinely distinct structural roles, not a continuum.

---

## Data Sources

All validation datasets sourced from the [Animal Social Network Repository (ASNR)](https://github.com/bansallab/asnr/tree/master/Networks) maintained by the Bansal Lab.

- **Bottlenose dolphins:** Doubtful Sound, New Zealand (n=62)
- **Sociable weavers:** Networks 639 and 658 (n=42, n=24)
- **Vampire bats:** Cranbrook colony, Network_505 (n=21) — data courtesy of Dr. Gerald Carter

---

## Reproduce the Results

All scripts referenced in the paper are in this repository under their exact cited filenames.

```bash
# Dolphins
python dolphin_resonance.py

# Sociable weavers
python bird_resonance_flycatcher.py --network 639
python bird_resonance_flycatcher.py --network 658

# Null case validation (run on any dataset)
python null_case_validation.py --input your_network.graphml

# Fragmentation analysis
python resonance_centrality.py --fragmentation True
```

---

## Citing This Work

**Preprint (Zenodo):**

```bibtex
@misc{keiser2026resonance,
  title  = {Resonance Centrality: A Composite Metric for Two Distinct Classes
            of Structural Importance in Animal Social Networks},
  author = {Keiser, Barbara J},
  year   = {2026},
  doi    = {10.5281/zenodo.19009607},
  url    = {https://doi.org/10.5281/zenodo.19009607},
  note   = {Preprint. Under review at Animal Behaviour.}
}
```

DOI badge:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19009607.svg)](https://doi.org/10.5281/zenodo.19009607)
```

---

## Acknowledgments

Methodological feedback: **Dr. Damien Farine** (Australian National University).  
Abstract quote (with permission): **Dr. Hal Whitehead** (Dalhousie University).  
Vampire bat data: **Dr. Gerald Carter** (Princeton University).  
Data infrastructure: **ASNR / Bansallab GitHub**.

AI disclosure: portions of analysis and writing were developed in collaboration with Claude (Anthropic) and Grok (xAI), used as reasoning and coding partners. All scientific decisions, interpretations, and validation were made by the human author.

---

## License

MIT — see [LICENSE](LICENSE).

Data from ASNR is used under its original terms. See individual dataset citations in the paper.

---

*Barbara J. Keiser — Independent Researcher*  
*Gravois Mills, Missouri*  
*barbara.j.keiser@gmail.com*

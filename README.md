# Resonance Centrality 🐬🐦🦇🐋✨

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

Validated across five datasets spanning four species, all at the **100th percentile** against 100 null permutations, with effect sizes from **5.76σ to 29.88σ** — well beyond physics discovery thresholds.

**Preprint:** [doi.org/10.5281/zenodo.19009607](https://doi.org/10.5281/zenodo.19009607)  
**Submitted to:** *Animal Behaviour*

---

## The Species

<table>
<tr>
<td align="center" width="25%">
<img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Tursiops_truncatus_01.jpg" width="180" alt="Bottlenose dolphin"/><br>
<b>Bottlenose dolphin</b><br>
<i>Tursiops truncatus</i><br>
Doubtful Sound, NZ<br>
17.72σ · Beescratch
</td>
<td align="center" width="25%">
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Philetairus_socius_-Kgalagadi_Transfrontier_Park-8.jpg" width="180" alt="Sociable weaver"/><br>
<b>Sociable weaver</b><br>
<i>Philetairus socius</i><br>
Kalahari, South Africa<br>
29.88σ · Beescratch / True Grin ⭐
</td>
<td align="center" width="25%">
<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Vampire_bat_upsidedown.jpg" width="180" alt="Vampire bat"/><br>
<b>Vampire bat</b><br>
<i>Desmodus rotundus</i><br>
Cranbrook colony<br>
5.76σ · Grin + Beescratch
</td>
<td align="center" width="25%">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Killerwhales_jumping.jpg" width="180" alt="Southern Resident killer whale"/><br>
<b>Killer whale</b><br>
<i>Orcinus orca</i><br>
Southern Residents<br>
26.90σ · True Grin 🆕
</td>
</tr>
</table>

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
| Network_1071 *(new)* | S. Resident killer whale | 57 | 1264 | **26.90σ** | 100th | True Grin 🆕 |

Effect sizes above 5σ exceed the threshold for discovery claims in particle physics. Grins and Beescratches are non-overlapping individuals in every validated dataset. Removal experiments confirm functionally distinct structural roles.

---

## 🆕 Southern Resident Killer Whales

> *New finding — not yet in the submitted preprint. In active correspondence with researchers. Pending revision.*
>
> *Data: Weiss et al. 2020, ASNR Network_1071.*

The Southern Resident killer whale network (57 individuals, 1,264 weighted associations, network density 0.7920) scores **26.90σ** above 100 null permutations — the second highest effect size in the entire validated dataset, behind only the sociable weavers at 29.88σ.

More significantly: the network contains a **True Grin** — a single individual simultaneously holding the highest betweenness centrality (0.0409) and the highest resonance score (0.4222) across all 57 nodes. This individual is connected to every other animal in the network.

The Southern Residents are at historic lows. K pod has 14 individuals. The True Grin in this network is the structural node holding all three pods together. That individual's identity maps to a named whale in the Weiss et al. dataset.

This finding extends the density/True Grin pattern observed across all validated datasets: as network density increases, True Grins emerge. At density 0.7920, the Southern Resident network is the densest validated to date.

| Metric | Value |
|--------|-------|
| Nodes | 57 |
| Edges | 1,264 |
| Density | 0.7920 |
| Network Resonance Score | 0.3377 |
| Effect size | **26.90σ** |
| Percentile | 100th |
| True Grin betweenness | 0.0409 |
| True Grin resonance | 0.4222 |
| True Grin connections | 56 of 56 (all) |

---

## Node Classes

**Grin** — The routing hub. High betweenness, lower neighborhood coherence. This is the individual betweenness centrality was built to find. Remove a Grin and paths get longer.

**Beescratch** — The quality anchor. High resonance score, low betweenness. Invisible to standard analysis. These individuals maintain the richest, most densely interconnected local neighborhoods in the network. They are not bridges — they are hubs of local cohesion.

**True Grin** — The rarest class. An individual that simultaneously maximizes both routing and local coherence. First confirmed: DBMREBK in sociable weaver Network_658 (removal: +0.742 average path length, the largest single-node disruption across all datasets). Now confirmed in the Southern Resident killer whale network.

**The key finding:** Grins and Beescratches are never the same individual. They represent two genuinely distinct structural roles, not a continuum.

---

## Quick Start

```bash
git clone https://github.com/barbarajkeiser-MarsLoop/Resonance-Centrality.git
cd Resonance-Centrality
pip install networkx numpy scipy pandas matplotlib
```

**Command line:**

```bash
python resonance_centrality.py \
  --input your_network.graphml \
  --output results.csv \
  --permutations 100 \
  --weight weight
```

**Python:**

```python
import networkx as nx
from resonance_centrality import compute_resonance

G = nx.read_graphml("your_network.graphml")
results = compute_resonance(G, weight='weight')

# Top nodes by resonance score
print(results.sort_values('resonance', ascending=False).head(10))

# Find Grins and Beescratches
grins       = results[results['node_class'] == 'Grin']
beescratches = results[results['node_class'] == 'Beescratch']
```

**Null-model validation:**

```python
from null_case_validation import run_permutation_test

sigma, percentile = run_permutation_test(G, n_permutations=100, weight='weight')
print(f"Effect size: {sigma:.2f}σ | Percentile: {percentile}th")
```

---

## Data Sources

All validation datasets from the [Animal Social Network Repository (ASNR)](https://github.com/bansallab/asnr/tree/master/Networks), Bansal Lab.

- **Bottlenose dolphins:** Doubtful Sound, New Zealand (n=62)
- **Sociable weavers:** Networks 639 and 658 (n=42, n=24)
- **Vampire bats:** Cranbrook colony, Network_505 (n=21) — data courtesy Dr. Gerald Carter
- **Southern Resident killer whales:** Network_1071, Weiss et al. 2020 (n=57)

---

## Reproduce the Results

All scripts are in this repository under their exact cited filenames.

```bash
python dolphin_resonance.py
python bird_resonance_flycatcher.py --network 639
python bird_resonance_flycatcher.py --network 658
python null_case_validation.py --input your_network.graphml
python resonance_centrality.py --fragmentation True
```

---

## Citing This Work

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

DOI badge for your own docs:
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

MIT — see [LICENSE](LICENSE). Data from ASNR is used under its original terms.

---

*Barbara J. Keiser — Independent Researcher*  
*Gravois Mills, Missouri*  
*barbara.j.keiser@gmail.com*00

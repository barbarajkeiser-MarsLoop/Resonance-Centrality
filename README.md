# Resonance Centrality 🐬🐦🦇✨

**A composite metric revealing two structurally distinct classes of important individuals in animal social networks**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19009607.svg)](https://doi.org/10.5281/zenodo.19009607)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-brightgreen?style=flat-square)](https://www.python.org)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.6+-orange?style=flat-square)](https://networkx.org)
[![Status](https://img.shields.io/badge/status-under_review-yellow?style=flat-square)](https://doi.org/10.5281/zenodo.19009607)

---

**Betweenness centrality has dominated animal social network analysis for 20+ years** — but it only sees the routing hubs.  

**Resonance Centrality** sees *both*:

- **Grins** — routing hubs (high betweenness)  
- **Beescratches** — quality anchors that create the richest local neighborhoods (invisible to betweenness)  
- **True Grins** — rare individuals who dominate *both* roles at once  

Validated across four real-world datasets (dolphins, sociable weavers, vampire bats) with effect sizes **5.76σ to 29.88σ** — all at the **100th percentile** of 100 scrambled null networks. (For context: 5σ is the physics discovery threshold.)

**Preprint (Zenodo):** [doi.org/10.5281/zenodo.19009607](https://doi.org/10.5281/zenodo.19009607)  
**Submitted to:** *Animal Behaviour*

---

## The Resonance Centrality Formula

```math
RC(i) = (Rhythm \times 0.4) + (Coherence \times 0.4) + (Bridging \times 0.2)

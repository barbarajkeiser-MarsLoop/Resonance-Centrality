# Resonance Centrality 🐬🐦✨

**A new way to spot the real MVPs in animal social networks**

![Resonance Centrality Banner](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.8+-brightgreen?style=for-the-badge) ![NetworkX](https://img.shields.io/badge/NetworkX-powered-orange?style=for-the-badge)

Betweenness centrality has been the king of animal network analysis for 20+ years — but it only sees **half** the picture.

---

Special Thanks to: https://github.com/bansallab/asnr/tree/master/Networks 

---

**Resonance Centrality** reveals the hidden stars:

- **Grins** 😄 → routing hubs that keep everyone connected  
- **Beescratches** 🐝 → quality anchors that build the richest local neighborhoods (invisible to betweenness!)  
- **True Grins** ⭐ → rare super-nodes that dominate **both** roles  

Validated across real datasets with insane significance: up to **29.88σ** — way beyond physics discovery levels.

## At a Glance

| Metric              | What it finds                  | Weight | Why it matters                              |
|---------------------|--------------------------------|--------|---------------------------------------------|
| **Rhythm**          | Normalized degree              | 0.4    | How socially connected is this individual?  |
| **Coherence**       | Neighborhood density           | 0.4    | How rich & interwoven is their circle?      |
| **Bridging**        | Normalized betweenness         | 0.2    | How much does the network route through them? |

**Resonance = (Rhythm × 0.4) + (Coherence × 0.4) + (Bridging × 0.2)**

Tested on:
- Bottlenose dolphins (Doubtful Sound, n=62)
- Sociable weaver colonies (n=42 & n=24)

All three datasets hit **100th percentile** vs 100 random scrambled networks.

## Validation Highlights 🔥

| Dataset              | Species              | Nodes | Edges | Effect Size (σ) | Percentile | Top Node Type     |
|----------------------|----------------------|-------|-------|-----------------|------------|-------------------|
| Doubtful Sound       | Bottlenose Dolphin   | 62    | 159   | 17.72σ          | 100th      | Beescratch        |
| Network_639          | Sociable Weaver      | 42    | 152   | **29.88σ**      | 100th      | Beescratch        |
| Network_658          | Sociable Weaver      | 24    | 62    | 9.73σ           | 100th      | **True Grin**     |

These are **not** artifacts — real biological structure.

## Quick Start

```bash
# Clone & install
git clone https://github.com/barbarajkeiser-MarsLoop/Resonance-Centrality.git
cd Resonance-Centrality
pip install networkx numpy scipy pandas matplotlib



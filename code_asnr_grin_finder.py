"""
code_asnr_grin_finder.py

Applies resonance centrality analysis to any network in GraphML format.
Designed for use with the Animal Social Network Repository (ASNR).
Identifies Grin (highest betweenness), Beescratch (highest resonance),
and True Grin (individual leading on both metrics simultaneously).
Runs null-case permutation validation to confirm biological structure.

Usage:
    python code_asnr_grin_finder.py Network_639.graphml
    python code_asnr_grin_finder.py Network_658.graphml

Requires: networkx, numpy (standard scientific Python stack)

[Author information removed for double-blind peer review]
"""

import sys
import random
import statistics
import networkx as nx


# ============================================================
# RESONANCE CENTRALITY FORMULA
# Node Resonance = (Rhythm x 0.4) + (Coherence x 0.4) + (Bridging x 0.2)
# ============================================================

def node_resonance(G, node, btw, deg):
    """
    Compute resonance centrality for a single node.

    Rhythm    (weight 0.4): normalized degree centrality
    Coherence (weight 0.4): neighborhood density (local clustering coefficient)
    Bridging  (weight 0.2): normalized betweenness centrality
    """
    rhythm = deg[node]

    neighbors = list(G.neighbors(node))
    if len(neighbors) < 2:
        coherence = 0.0
    else:
        subgraph = G.subgraph(neighbors)
        possible = len(neighbors) * (len(neighbors) - 1) / 2
        actual = subgraph.number_of_edges()
        coherence = actual / possible if possible > 0 else 0.0

    bridging = btw[node]

    return (rhythm * 0.4) + (coherence * 0.4) + (bridging * 0.2)


def network_resonance_score(G):
    """Compute mean resonance score across all nodes in the network."""
    btw = nx.betweenness_centrality(G)
    deg = nx.degree_centrality(G)
    scores = [node_resonance(G, n, btw, deg) for n in G.nodes()]
    return sum(scores) / len(scores) if scores else 0.0


# ============================================================
# NULL-CASE PERMUTATION VALIDATION
# ============================================================

def scramble_network(G, seed=None):
    """
    Generate a null network preserving node count and edge count.
    Edges are assigned randomly with no biological structure.
    """
    if seed is not None:
        random.seed(seed)

    nodes = list(G.nodes())
    edge_count = G.number_of_edges()

    G_null = nx.Graph()
    G_null.add_nodes_from(nodes)

    added = 0
    attempts = 0
    while added < edge_count and attempts < edge_count * 20:
        a = random.choice(nodes)
        b = random.choice(nodes)
        if a != b and not G_null.has_edge(a, b):
            G_null.add_edge(a, b)
            added += 1
        attempts += 1

    return G_null


def run_null_validation(G, n_permutations=100):
    """
    Run null-case permutation test.
    Returns effect size (sigma) and percentile rank.
    """
    empirical_score = network_resonance_score(G)

    null_scores = []
    for i in range(n_permutations):
        G_null = scramble_network(G, seed=i)
        null_scores.append(network_resonance_score(G_null))

    null_mean = statistics.mean(null_scores)
    null_sd = statistics.stdev(null_scores)

    sigma = (empirical_score - null_mean) / null_sd if null_sd > 0 else 0.0
    percentile = sum(1 for s in null_scores if empirical_score > s)

    return {
        "empirical_score": empirical_score,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "sigma": sigma,
        "percentile": percentile,
        "n_permutations": n_permutations
    }


# ============================================================
# FRAGMENTATION ANALYSIS
# ============================================================

def average_path_length(G):
    """Average shortest path length, using largest component if disconnected."""
    if nx.is_connected(G):
        return nx.average_shortest_path_length(G)
    largest = max(nx.connected_components(G), key=len)
    return nx.average_shortest_path_length(G.subgraph(largest).copy())


def fragmentation_analysis(G, grin, beescratch):
    """
    Single-node removal experiment.
    Computes APL change on removing the Grin vs. the Beescratch.
    """
    apl_full = average_path_length(G)

    G_no_grin = G.copy()
    G_no_grin.remove_node(grin)
    apl_no_grin = average_path_length(G_no_grin)

    if grin == beescratch:
        return {
            "apl_full": apl_full,
            "apl_no_grin": apl_no_grin,
            "delta_grin": apl_no_grin - apl_full,
            "apl_no_beescratch": apl_no_grin,
            "delta_beescratch": apl_no_grin - apl_full,
            "note": "Same individual (True Grin) — single removal serves both conditions"
        }

    G_no_bs = G.copy()
    G_no_bs.remove_node(beescratch)
    apl_no_bs = average_path_length(G_no_bs)

    return {
        "apl_full": apl_full,
        "apl_no_grin": apl_no_grin,
        "delta_grin": apl_no_grin - apl_full,
        "apl_no_beescratch": apl_no_bs,
        "delta_beescratch": apl_no_bs - apl_full
    }


# ============================================================
# MAIN ANALYSIS RUNNER
# ============================================================

def analyze_network(filepath, n_permutations=100):
    """
    Full resonance centrality analysis pipeline for a GraphML file.
    """
    print(f"\nRESONANCE CENTRALITY ANALYSIS")
    print(f"File: {filepath}")
    print("=" * 60)

    # Load network
    G = nx.read_graphml(filepath)
    G = nx.Graph(G)  # ensure undirected

    print(f"Nodes: {G.number_of_nodes()} | Edges: {G.number_of_edges()}")
    density = nx.density(G)
    print(f"Density: {density:.4f}")

    # Compute centrality measures
    btw = nx.betweenness_centrality(G)
    deg = nx.degree_centrality(G)

    # Compute all node resonance scores
    scores = {n: node_resonance(G, n, btw, deg) for n in G.nodes()}

    # Identify Grin and Beescratch
    grin = max(btw, key=btw.get)
    beescratch = max(scores, key=scores.get)

    # Betweenness rank of beescratch
    btw_ranked = sorted(btw, key=btw.get, reverse=True)
    bs_btw_rank = btw_ranked.index(beescratch) + 1

    print(f"\nGRIN (highest betweenness centrality)")
    print(f"  Individual:      {grin}")
    print(f"  Betweenness:     {btw[grin]:.4f}")
    print(f"  Resonance score: {scores[grin]:.4f}")

    print(f"\nBEESCRATCH (highest resonance centrality)")
    print(f"  Individual:      {beescratch}")
    print(f"  Resonance score: {scores[beescratch]:.4f}")
    print(f"  Betweenness:     {btw[beescratch]:.4f}")
    print(f"  Betweenness rank: {bs_btw_rank} of {G.number_of_nodes()}")

    if grin == beescratch:
        print(f"\n*** TRUE GRIN DETECTED ***")
        print(f"  {grin} leads on both betweenness AND resonance centrality.")
        print(f"  This individual holds dual-role structural dominance.")
    else:
        print(f"\nGrin/Beescratch distinction confirmed.")
        print(f"  Two different individuals hold routing vs. quality-anchor roles.")

    # Fragmentation analysis
    print(f"\nFRAGMENTATION ANALYSIS")
    frag = fragmentation_analysis(G, grin, beescratch)
    print(f"  Full network APL:            {frag['apl_full']:.3f}")
    print(f"  Remove {grin} (Grin):  APL = {frag['apl_no_grin']:.3f} (+{frag['delta_grin']:.3f})")
    if grin != beescratch:
        print(f"  Remove {beescratch} (Beescratch): APL = {frag['apl_no_beescratch']:.3f} (+{frag['delta_beescratch']:.3f})")
    else:
        print(f"  (Same individual — True Grin removal serves both conditions)")

    # Null-case validation
    print(f"\nNULL-CASE VALIDATION ({n_permutations} permutations)")
    print("  Running...")
    val = run_null_validation(G, n_permutations)
    print(f"  Empirical score: {val['empirical_score']:.6f}")
    print(f"  Null mean:       {val['null_mean']:.6f}")
    print(f"  Null SD:         {val['null_sd']:.6f}")
    print(f"  Effect size:     {val['sigma']:.2f}σ")
    print(f"  Percentile:      {val['percentile']}th of {n_permutations}")

    if val["percentile"] >= 95:
        print(f"  RESULT: VALIDATED — empirical network exceeds {val['percentile']}% of null permutations")
    else:
        print(f"  RESULT: NOT VALIDATED at 95th percentile threshold")

    # Top 10 resonance scores
    print(f"\nTOP 10 RESONANCE SCORES")
    top10 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    for rank, (node, score) in enumerate(top10, 1):
        flag = ""
        if node == grin and node == beescratch:
            flag = " [TRUE GRIN]"
        elif node == grin:
            flag = " [GRIN]"
        elif node == beescratch:
            flag = " [BEESCRATCH]"
        print(f"  {rank:2}. {node:<15} resonance={score:.4f}  betweenness={btw[node]:.4f}{flag}")

    return {
        "grin": grin,
        "beescratch": beescratch,
        "true_grin": grin == beescratch,
        "scores": scores,
        "validation": val,
        "fragmentation": frag
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python code_asnr_grin_finder.py <network.graphml>")
        print("\nExample:")
        print("  python code_asnr_grin_finder.py Network_639.graphml")
        print("  python code_asnr_grin_finder.py Network_658.graphml")
        sys.exit(1)

    filepath = sys.argv[1]
    results = analyze_network(filepath)

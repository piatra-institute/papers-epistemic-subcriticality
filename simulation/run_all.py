"""Orchestrator: reproduces every number and all three figures in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/{non_discrimination,
absorption_frontier,subcritical_persistence}.png. Deterministic given the
recorded seed. A failed invariant or a failed figure fails the run.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    from figures import (plot_non_discrimination, plot_absorption_frontier,
                         plot_subcritical_persistence)
    plot_non_discrimination(results, str(OUT / "figures" / "non_discrimination.png"))
    plot_absorption_frontier(results, str(OUT / "figures" / "absorption_frontier.png"))
    plot_subcritical_persistence(results, str(OUT / "figures" / "subcritical_persistence.png"))

    nd = results["non_discrimination"]
    ms = results["matched_suppression"]
    sp = results["subcritical_persistence"]
    print(f"R_F baseline {nd['R_F_baseline']}, "
          f"max |dlogR discrepancy| {nd['max_discrepancy_dlogR']:.3e}")
    print(f"elasticities {nd['elasticities']}")
    print(f"baseline: refuted persists {ms['baseline_refuted']['p_persist']}, "
          f"vindicable absorbed {ms['baseline_vindicable']['p_absorbed']}")
    print(f"matched suppression target {ms['suppression_target']}")
    for name, r in ms["policies"].items():
        print(f"  {name:16s} persist {r['p_persist_refuted']:.3f}  "
              f"absorbed {r['p_absorbed_vindicable']:.3f}  "
              f"discrimination {r['discrimination']:+.3f}")
    print(f"subcritical: critical seed {sp['critical_seed']}, "
          f"established {sp['established_equilibrium']}")
    print(f"invariants {results['invariants']}")


if __name__ == "__main__":
    main()

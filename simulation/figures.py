"""The paper's three figures. A failed figure fails the run."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REFUTED = "#b2182b"
VINDICABLE = "#2166ac"
NEUTRAL = "#7f7f7f"
ABSORB = "#1a7f37"


def plot_non_discrimination(res: dict, path: str) -> None:
    nd = res["non_discrimination"]
    levers = list(nd["levers"])
    s_key = "s=0.25"
    ref = [nd["levers"][l][s_key]["dlogR_refuted"] for l in levers]
    vin = [nd["levers"][l][s_key]["dlogR_vindicable"] for l in levers]
    x = np.arange(len(levers))
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.bar(x - 0.18, ref, 0.36, color=REFUTED, label="refuted claim")
    ax.bar(x + 0.18, vin, 0.36, color=VINDICABLE, label="vindicable claim")
    ax.set_xticks(x)
    ax.set_xticklabels(levers)
    ax.set_ylabel(r"change in $\log \mathcal{R}_F$")
    ax.set_title("change in $\\log \\mathcal{R}_F$ at s = 0.25, equal architecture, opposite truth values", fontsize=10)
    ax.axhline(0, color="k", lw=0.8)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def plot_absorption_frontier(res: dict, path: str) -> None:
    ms = res["matched_suppression"]
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    base = ms["baseline_vindicable"]["p_absorbed"]
    ax.axhline(base, color=NEUTRAL, ls=":", lw=1.0)
    ax.set_xlim(0.28, 0.70)
    ax.annotate("vindication before intervention", (0.29, base + 0.02),
                fontsize=8, color=NEUTRAL)
    ax.axvline(ms["suppression_target"], color=NEUTRAL, ls="--", lw=0.8)
    ax.annotate("matched suppression", (ms["suppression_target"] - 0.012, 0.62),
                fontsize=8, color=NEUTRAL, rotation=90)
    # The three reaching levers land on the same abscissa by construction, so
    # their labels are placed to the right in data coordinates with leader lines.
    label_at = {"deplatforming": (0.40, 0.42), "correction": (0.40, 0.33),
                "friction": (0.40, 0.24), "demonetisation": (0.56, 0.58),
                "absorptivity": (0.38, 0.82)}
    for name, r in ms["policies"].items():
        colour = ABSORB if name == "absorptivity" else REFUTED
        xy = (r["p_persist_refuted"], r["p_absorbed_vindicable"])
        ax.scatter(*xy, s=40, color=colour, zorder=3)
        ax.annotate(f"{name} ({r['p_absorbed_vindicable']:.4f})", xy,
                    xytext=label_at[name], textcoords="data", fontsize=9,
                    va="center", arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=0.6))
    ax.set_xlabel("probability the refuted formation persists (matched across policies)")
    ax.set_ylabel("probability the vindicable claim is absorbed")
    ax.set_title("vindicable absorption under each policy at matched refuted persistence")
    ax.set_ylim(0, 1.02)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def plot_subcritical_persistence(res: dict, path: str) -> None:
    sp = res["subcritical_persistence"]
    delta, beta = sp["delta"], sp["beta"]
    y = np.linspace(0, 1, 600)
    dy = -delta * y + beta * y ** 2 * (1 - y)
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    ax.plot(y, dy, color=NEUTRAL, lw=1.6)
    ax.axhline(0, color="k", lw=0.8)
    ax.scatter([0], [0], color=ABSORB, zorder=3, s=45)
    ax.scatter([sp["critical_seed"]], [0], color=REFUTED, zorder=3, s=45)
    ax.scatter([sp["established_equilibrium"]], [0], color=REFUTED, zorder=3, s=45)
    ax.annotate(f"critical seed {sp['critical_seed']:.3f}", (sp["critical_seed"], 0),
                xytext=(-10, 22), textcoords="offset points", fontsize=9, ha="center")
    ax.annotate(f"established {sp['established_equilibrium']:.3f}",
                (sp["established_equilibrium"], 0), xytext=(0, -26),
                textcoords="offset points", fontsize=9, ha="center")
    ax.set_xlabel("prevalence $y$")
    ax.set_ylabel(r"$\dot y$")
    ax.set_title("reinforcement model, $\\delta = 0.2$, $\\beta = 1.6$", fontsize=10)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)

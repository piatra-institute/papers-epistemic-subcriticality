# Epistemic Subcriticality

Process Interventions Are Blind to Truth, and What to Maximise Instead.

A recurring proposal in political epistemology holds that a society should make organised falsehood non-reproducing, keeping the reproduction number of a belief formation below one while leaving expression free, and relies on interventions that act only on processes such as recruitment and organisation. We model a claim-centred formation as a two-type branching process over active transmitters and organisational units, with lifetime offspring matrix $K$ and reproduction number $\mathcal{R}_F = \rho(K) = 1.856918$ in the baseline architecture. Because truth is not an argument of $K$, every content-neutral intervention changes $\log \mathcal{R}_F$ identically for refuted and vindicable formations with the same architecture; the computed discrepancy is zero across four levers and three intensities. The plausible architectural asymmetry, a larger organisational channel in the refuted formation, lowers the discrimination index of uniform friction from $0.199$ to $0.068$. We add a third fate, absorption into general infrastructure, which is open only to true claims and whose rate can be raised without knowing which claims are true. At matched suppression of refuted formations, friction, deplatforming and correction lower the vindicable claim's absorption probability from $0.4985$ to between $0.3255$ and $0.360$, while raised absorptive capacity increases it to $0.820$. Demonetisation cannot reach the target, because the transmitter-to-transmitter entry of $K$, with elasticity $0.739597$, exceeds one on its own. Under reinforcement the origin is stable for every transmission rate, yet an established formation persists at $0.854$ above a critical seed of $0.146$. Within this stipulated construct, which measures no real movement, the quantity an epistemic system should maximise is the rate at which claims are brought to decision.

## Simulation

```bash
cd simulation
uv run run_all.py        # -> output/results.json + output/figures/*.png
```

Deterministic given the recorded seed; the run takes about 7 seconds. Invariants fail the run loudly if broken: the non-discrimination discrepancy must be exactly zero, the elasticities must sum to one, the matched-suppression constraint must hold for every policy that reaches the target, at least one lever must saturate, and the reinforcement model's critical seed must separate extinction from persistence. The construct is illustrative and instantiates the paper's definitions; it is not fitted to any movement, its decisive test is perfectly informative, and the paper states these terms where the numbers are used. Every number cited in the paper is a key in `simulation/output/results.json`.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build epistemic-subcriticality`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.

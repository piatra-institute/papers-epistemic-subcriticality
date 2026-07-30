# Epistemic Subcriticality

Process Interventions Are Blind to Truth, and What to Maximise Instead. A recurring proposal in political epistemology holds that a society should not abolish false beliefs but should make organised falsehood non-reproducing, keeping the reproduction number of a belief formation below one while leaving expression free, with the safeguard that interventions act on processes rather than on propositions. This paper shows the safeguard is empty and repairs the proposal by changing the target. Modelling a claim-centred formation as a two-type branching process over transmitters and organisational units gives a lifetime offspring matrix K and a formation reproduction number R_F = rho(K); truth is not an argument of K, so any content-neutral intervention induces the same change in log R_F for a refuted formation and for a vindicable one with the same architecture. The simulation reports that discrepancy as exactly zero across four levers and three intensities. Discrimination therefore needs either a claim-level classifier, which reintroduces the problem the process framing was meant to avoid, or an architectural asymmetry, which the paper tests and finds running the wrong way. The repair is a transition the literature omits: a formation can also end by absorption, when its claim-set enters the general infrastructure and nobody organises to defend what everyone teaches. Absorption is the success mode of true heterodoxy, it is closed to a refuted claim, and its rate is a system parameter that can be raised without knowing which claims are true. Held to equal suppression of the refuted formation, the process levers that reach the target cut the vindicable claim's absorption probability from 0.4985 to between 0.3255 and 0.360, while raising absorptive capacity reaches the same suppression and raises absorption to 0.820. A fourth lever, demonetisation, cannot reach the target at any admissible intensity. The paper closes on the reason subcriticality was never viability: under reinforcement the origin is stable for every transmission rate while an established formation at 0.854 persists above a critical seed of 0.146.

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

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build epistemic-subcriticality`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.

# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-07-30 — first draft, simulation, and publish

Scope: the whole paper, from the seeded chat to a published PDF, a runnable simulation, and a web entry.

Origin: `chats/chat.md`, an adversarial pre-publication review of a proposed manuscript titled *Epistemic Subcriticality: A Systems Theory of False-Belief Reproduction*. The review's verdict was "promising but requiring substantial theoretical repair", and it was right about the repairs. This paper is not the reviewed manuscript. It takes the review's own diagnosis of the most dangerous unresolved objection, that the framework cannot distinguish making a false formation non-viable from making disfavoured dissent non-viable, and makes that objection the subject.

What the paper does with the seed:

- **Concedes the novelty claim rather than defending it.** The review found the reproduction machinery unoriginal; §1 says so in its own voice and names the precedents (Bettencourt et al. 2006, Brooks and Porter 2025, Sperber 1985, Diekmann et al. 2010) instead of burying them.
- **Adopts the review's repaired formalism**, the two-type lifetime offspring matrix, and drops the seed's transition matrix, whose dominant eigenvalue is a per-timestep growth factor rather than a reproduction number.
- **Turns the unresolved objection into a proposition.** Truth is not an argument of K, so every content-neutral lever induces the same change in log R_F for two formations with the same architecture. This is trivial, provable in one line, and it is the paper's reason to exist, because it shows the seed's central safeguard guarantees the property that makes the tool useless.
- **Tests the one escape the review left open.** If refuted and vindicable formations differ architecturally, uniform pressure could discriminate. The simulation finds the plausible asymmetry runs the wrong way, since organisational depth is what refuted formations have and nascent correct ones do not.
- **Adds the transition the whole literature omits.** Absorption is the third fate: a formation dissolves when its claims enter the general infrastructure. It is the success mode of true heterodoxy, it is closed to a refuted claim, and its rate is raisable without a truth classifier. This is the paper's own contribution and is not in the seed.
- **Declines two of the seed's proposals.** Flat-earthism is used as nothing at all, and the sentinel claim is refused on the published evidence for heterogeneous participation. The seed's "de facto epistemic impossibility" is not used.

Simulation: `simulation/` ships `analyses.py`, `figures.py`, `run_all.py`, a `pyproject.toml` and a `uv.lock`. Deterministic given seed 20260730; runtime about 7 seconds on Python 3.13.3 with NumPy 2.5.1 and Matplotlib 3.11.1. Five analyses: the non-discrimination certificate, matched-suppression policy comparison, an absorptive-capacity sweep, an architecture-asymmetry sweep, and the reinforcement model. Six invariants fail the run if broken.

Two findings emerged from the code rather than from the plan. Demonetisation cannot reach the matched-suppression target at any admissible intensity, discovered when the bisection failed to converge; the code now records `reaches_target` per policy and an invariant asserts that some lever saturates, and the paper reports it as a result about which channel carries the elasticity. And the process levers' cost to vindication turned out not to need the architecture asymmetry at all: identical treatment alone removes about a third of the vindicable claim's chance of being tested, which is a cleaner result than the one the plan anticipated.

Citations: the seed supplied DOIs. All 41 that the paper considered were resolved against Crossref before use, and none was fabricated. Corrections made in passing: Pilati et al. is 2024 in Crossref rather than the seed's 2025; Marshall and Warren is *Lancet* 323(8390) under continuous numbering; the van den Driessche entry is filed under D so that the in-text form resolves. Verified sources the paper does not engage are listed under "Verified but not cited" in `sources.md` rather than cited decoratively.

Verification:
- voice: 0 errors, 0 review-candidates after two passes. The first pass flagged one inline-contrastive and three negate-pivots, all mine, all rewritten as positive declaratives; `carries/carry` was at 1.9 per thousand against a corpus mean of 0.49 and was thinned to 0.2; `exactly` from 1.3 to 0.6. Rhythm advisory remains at a 37-sentence run without a short one, which is the abstract plus the first two sections; two short declaratives were added and the rest is accepted.
- refs: 28 in-text citation keys, 28 bibliography entries, 0 missing, 0 unused.
- claims: 146 distinct values in `results.json`, 72 decimal claims in prose, 4 without a match. All four are negative values in the JSON (-0.169545, -0.03586, -0.1885, -0.1415) that the gate's unsigned decimal regex cannot match. Expected false positives.
- build: 14 pages, 0 missing-character warnings, all three figures render, the pipe table aligns, the title page breaks cleanly across two lines.
- check => PASS. Synced to the web app; entry added to `ownPapers` with topics philosophy / political-science / mathematics and kinds formal / simulation.

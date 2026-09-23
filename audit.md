# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-09-23 — prose revision

Prose revision against the house standard.
  - Headings: Abstract; 1. Introduction; 2. Model; 3. Structural non-discrimination; 4. Architectural asymmetry and uniform friction; 5. Absorption as a third fate; 6. Matched-suppression comparison; 7. Invasion threshold and persistence under reinforcement; 8. Limitations; 9. Conclusion; Reproducibility.
  - Tic counts before -> after: 'rather than' 17 -> 0; 'this paper' 7 -> 0; 'not X but Y' 1 -> 0; 'worth' 2 -> 0; 'exactly/precisely' 3 -> 0; sentence-initial 'That is/This is' 6 -> 1. Abstract 520 -> 261 words. Seed reference ('The seed proposal nominated flat-earthism') removed.
  - Corrections: (1) 'removing roughly a third of the vindicable claim's chance' -> 'a loss of 28 to 35 per cent' (0.1385/0.4985 = 0.278 to 0.1730/0.4985 = 0.347; 'a third' overstated deplatforming and correction). (2) 'once beta >= 4 delta there are two [positive equilibria]' -> 'for beta > 4 delta'; at equality the two roots coincide. (3) Absorptivity matched to the target at 0.35450 was said to be 'suppressed as much as friction suppressed it' (friction reached 0.35325); now 'at the matched target'. (4) Test rate 0.327999 written as 0.328, matching the table.
  - Grid audit: no grid artefact. Matched-suppression intensities come from a 28-step bisection with common random numbers; the demonetisation intensity 0.95 is the admissible bound (lever saturates); the reinforcement equilibria are closed form. The asymmetry sweep (ratios 1 to 4) and absorption sweep report grid points as grid points. All prose numbers checked against results.json.
  - Code: the 'fates_partition' invariant was vacuous (it checked p_persist <= 1); it now checks that each baseline's three terminal probabilities sum to one and that each policy's recorded vindicable fates do not exceed one. Added results field matched_suppression.mc_standard_error_max = 0.007906 (binomial SE at p = 0.5, 4,000 replicates) with an invariant tying it to the replicate count; the text now states it (0.0079), and the demonetisation effect on absorption (+0.0065) is described as within Monte Carlo error. Eight invariants pass; results.json otherwise unchanged.
  - Noted, not changed: the absorption sweep's a = 0.05 point (absorption 0.461, persistence 0.68525) and the matched-suppression baseline at the same rate (0.4985, 0.70825) use independent random streams and differ by about 3.3 and 2 standard errors of the difference; the text cites only the baseline.
  - Figures: slogan titles replaced by descriptive ones; figure 2 labels moved to leader lines with absorption values. README regenerated.

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

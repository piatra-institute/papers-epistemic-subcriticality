# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
A claim that reaches the paper rests on a T1 or T2 source.

Verification pass: 2026-07-30. The seed is an adversarial review of a proposed manuscript, and it supplied a bibliography with DOIs. Every DOI it gave for a source the paper uses was resolved against the Crossref record, and every locator printed in the paper comes from that record rather than from the seed's rendering of it. Nothing in the seed's citation list turned out to be fabricated; several of its locators needed correction in detail.

## Findings

### The precedents that defeat the seed's novelty claim

- [T1] Reproduction numbers for ideas are two decades old and were estimated empirically, not merely proposed — Bettencourt, Cintrón-Arias, Kaiser and Castillo-Chávez (2006), *Physica A* 364:513–536. The paper concedes this in its second paragraph rather than defending a novelty claim it cannot hold.
- [T1] An "opinion reproduction number" with a critical cascade threshold on networks already exists in a peer-reviewed venue — Brooks and Porter (2025), *Chaos* 35(1):013160. This is an exact terminological and formal precedent for the seed's central metric.
- [T1] Next-generation construction is standard technique, and the offspring interpretation is what makes a threshold at one meaningful — Diekmann, Heesterbeek and Roberts (2010), *J. R. Soc. Interface* 7(47):873–885. Used to justify replacing the seed's transition matrix with a lifetime offspring matrix.
- [T1] An epidemiology of representations, with the warning that representations transform in transmission — Sperber (1985), *Man* 20(1):73–89.
- [T1] The critique any epidemiological transfer must answer, on ontology, measurement, mechanism, and intervention transfer — Yee (2025), *Synthese* 206(3):158. The paper answers the first by individuating the formation and the last by refusing to convert a threshold into a policy, and says so.

### Why a subcritical invasion number is not viability

- [T1] Sub-threshold endemic equilibria and backward bifurcation: a reproduction number below one does not imply global extinction — van den Driessche and Watmough (2002), *Mathematical Biosciences* 180(1–2):29–48.
- [T1] Threshold heterogeneity produces discontinuous collective outcomes — Granovetter (1978), *AJS* 83(6):1420–1443; global cascades depend on network structure rather than on average transmissibility — Watts (2002), *PNAS* 99(9):5766–5771.
- [T1] Reinforcement: behaviours that carry social cost require multiple independent contacts, so simple-contagion thresholds mislead — Centola and Macy (2007), *AJS* 113(3):702–734, with the experimental demonstration in Centola (2010), *Science* 329(5996):1194–1197. This is the empirical warrant for the $\dot y = -\delta y + \beta y^2(1-y)$ form in §7.

### Why architecture does not discriminate on truth

- [T1] Organisations, money, professional staff and constituencies determine movement survival, and the account is indifferent to whether the movement's claims are true — McCarthy and Zald (1977), *AJS* 82(6):1212–1241.
- [T1] Abeyance structures preserve identity, leadership and organisation through hostile periods — Taylor (1989), *ASR* 54(5):761–775. This is the mechanism by which a well-resourced formation absorbs uniform pressure that removes a small one.
- [T1] Collective identity shapes recruitment, commitment and boundaries — Polletta and Jasper (2001), *Annual Review of Sociology* 27(1):283–305.

### The absorption cases

- [T1] Magnetic anomalies over the ocean ridges: the decisive, replicable test that carried continental drift into standard practice — Vine and Matthews (1963), *Nature* 199(4897):947–949.
- [T1] The bacterial aetiology of peptic ulcer, established by a demonstration others could repeat — Marshall and Warren (1984), *The Lancet* 323(8390):1311–1315.
- [T1] The protein-only hypothesis for scrapie, heterodox to the point of scandal, absorbed on purification and transmission experiments — Prusiner (1982), *Science* 216(4542):136–144.
- [T1] The procedural rather than semantic criterion for a degenerating programme, which is that it absorbs refutations by auxiliary claims rather than making risky checkable predictions — Lakatos (1970), in *Criticism and the Growth of Knowledge*, pp. 91–196.

Note on how these are used: they are illustrations of a mechanism, not a sample. Three vindicated heterodoxies chosen after the fact cannot establish a base rate, and the paper does not claim one; what they establish is that absorption is a real exit and that its timing tracked the availability of a cheap decisive test.

### Intervention evidence

- [T1] Fact-checking produces positive but limited and heterogeneous correction effects — Walter, Cohen, Holbert and Morag (2019), *Political Communication* 37(3):350–375.
- [T1] Inoculation improves credibility assessment modestly, with no significant overall reduction in sharing intention across 42 studies — Lu, Hu and Li (2023), *JMIR* 25:e49255.
- [T1] The result the paper leans on hardest: prominent interventions reduce misperceptions while also increasing scepticism toward accurate information — Hoes, Aitken and Zhang (2024), *Nature Human Behaviour* 8(8):1545–1553. This is the individual-level analogue of the paper's formation-level finding, and it was obtained independently.
- [T1] The AI-dialogue result should not anchor anything: Costello, Pennycook and Rand (2024), *Science* 385(6714):eadq1814 now carries an editorial expression of concern, Thorp (2026), *Science* 392(6803):1131. Both records verified.

### Why the seed's sentinel case is demoted to a stress case

- [T1] Flat-earth discourse online mixes literal conviction, religious framing, clickbait, trolling and political signalling — Paolillo (2018), *First Monday* 23(12).
- [T1] Forum culture and social-media culture differ systematically, so one homogeneous transition matrix cannot represent both — Pilati, Venturini, Sacco and Gargiulo (2024), *New Media & Society* 27(9):5324–5341.
- [T1] Conversion narratives exist but come from small selected samples — Pahuus, Jørgensen and Wagoner (2024), *Integrative Psychological and Behavioral Science* 58(4):1895–1913.

### The normative constraint

- [T1] Testimonial and hermeneutical injustice — Fricker (2007); epistemic oppression as structural rather than incidental — Dotson (2014), *Social Epistemology* 28(2):115–138; public rejection of expert claims as evidence about institutions rather than a deficit in the public — Wynne (1992), *Public Understanding of Science* 1(3):281–304. These are why the paper treats the classifier problem as the real problem once the proposition of §3 is established.

## Simulation findings

All numbers below are keys in `simulation/output/results.json`, regenerated by `uv run run_all.py` in about 7 seconds.

- Baseline architecture gives $q = 0.133333$, $K = [[1.6, 4.0],[0.1, 0.3]]$, $\mathcal{R}_F = 1.856918$.
- **Non-discrimination certificate**: across 4 levers and 3 intensities, the maximum discrepancy between the refuted and the vindicable formation's change in $\log \mathcal{R}_F$ is $0$ exactly. Not small: zero.
- Elasticities of $\mathcal{R}_F$: TT $0.739597$, TO $0.118760$, OT $0.118760$, OO $0.022884$; they sum to one, which is checked as an invariant.
- $\Delta \log \mathcal{R}_F$ at $s = 0.25$: deplatforming $-0.287682$, friction $-0.196131$, correction $-0.169545$, demonetisation $-0.03586$.
- **Matched suppression** (target $0.354125$, half the baseline persistence of $0.70825$): friction $s = 0.342436$ leaves absorption at $0.3255$; deplatforming $s = 0.276894$ leaves $0.3600$; correction $s = 0.402604$ leaves $0.3570$; absorptivity $a = 0.327999$ leaves $0.8200$, against a baseline of $0.4985$.
- **Demonetisation saturates**: at the admissible maximum $s = 0.95$ the refuted formation still persists with probability $0.63050$ and $\mathcal{R}_F$ is $1.612519$, because $K_{TT} = 1.6$ exceeds one without any organisational channel at all. This was discovered by the calibration failing, and it is a finding rather than a bug; the code now records `reaches_target` per policy and an invariant asserts that some lever saturates.
- **Absorption sweep** with the architecture untouched: at $a = 0$, absorption $0$ and persistence $0.71475$; at $a = 0.2$, $0.775$ and $0.57525$; at $a = 0.5$, $0.86375$ and $0.12575$; at $a = 1.0$, $0.92$ and $0.00175$.
- **Architecture asymmetry**: uniform friction at $s = 0.3$ gives a discrimination index of $0.19925$ when architectures match and $0.0675$ at a fourfold organisational asymmetry, with the vindication cost rising from $0.0845$ to $0.1885$.
- **Reinforcement**: $\delta = 0.2$, $\beta = 1.6$, $\beta/\delta = 8 \ge 4$, critical seed $0.146447$, established equilibrium $0.853553$, slope at the origin $-0.2$; integration from below the critical seed returns $0$ and from above returns $0.85355339$.

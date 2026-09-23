---
title: |
  Epistemic Subcriticality:\
  Process Interventions Are Blind to Truth, and What to Maximise Instead
author: PIATRA . INSTITUTE
date: July 2026
---

## Abstract

A recurring proposal in political epistemology holds that a society should make organised falsehood non-reproducing, keeping the reproduction number of a belief formation below one while leaving expression free, and relies on interventions that act only on processes such as recruitment and organisation. We model a claim-centred formation as a two-type branching process over active transmitters and organisational units, with lifetime offspring matrix $K$ and reproduction number $\mathcal{R}_F = \rho(K) = 1.856918$ in the baseline architecture. Because truth is not an argument of $K$, every content-neutral intervention changes $\log \mathcal{R}_F$ identically for refuted and vindicable formations with the same architecture; the computed discrepancy is zero across four levers and three intensities. The plausible architectural asymmetry, a larger organisational channel in the refuted formation, lowers the discrimination index of uniform friction from $0.199$ to $0.068$. We add a third fate, absorption into general infrastructure, which is open only to true claims and whose rate can be raised without knowing which claims are true. At matched suppression of refuted formations, friction, deplatforming and correction lower the vindicable claim's absorption probability from $0.4985$ to between $0.3255$ and $0.360$, while raised absorptive capacity increases it to $0.820$. Demonetisation cannot reach the target, because the transmitter-to-transmitter entry of $K$, with elasticity $0.739597$, exceeds one on its own. Under reinforcement the origin is stable for every transmission rate, yet an established formation persists at $0.854$ above a critical seed of $0.146$. Within this stipulated construct, which measures no real movement, the quantity an epistemic system should maximise is the rate at which claims are brought to decision.

## 1. Introduction

A recurring proposal in political epistemology moves attention from individual false beliefs to the reproduction of organised falsehood. A belief may be entertained, expressed and privately held, and the epistemic order counts as healthy so long as no demonstrably false claim can assemble a durable formation with recruiters, organisations, finances and successors. The proposal borrows a threshold from epidemiology, holding the reproduction number of the formation below one, and adds a safeguard intended to keep the programme on the democratic side of the line: interventions structure processes and incentives and leave propositions unregulated. Sections 3 and 4 show that this safeguard cannot do the work assigned to it.

The epidemiological machinery is established. Models of idea diffusion are decades old, and the reproduction number has been estimated for ideas (Bettencourt, Cintrón-Arias, Kaiser and Castillo-Chávez, 2006); an opinion reproduction number for content cascades on networks has been derived (Brooks and Porter, 2025); Sperber (1985) proposed an epidemiology of representations while cautioning that representations transform in transmission; and next-generation construction with a multitype offspring matrix is standard technique (Diekmann, Heesterbeek and Roberts, 2010). The programme's contribution lies in its choice of evaluand. Whether an organised formation can replace its own transmitters and organisations is a different question from whether individuals hold false beliefs, and the intervention literature measures only the second.

The safeguard fails once the formation's reproduction number is treated as a mathematical object. The reproduction number is a function of the formation's architecture: how many assenters a transmitter reaches, how many survive to transmit, how long organisations last, and how many organisations they found. The truth of the claim-set does not appear in that function, since a recruitment rate is the same whatever it recruits for. A content-neutral intervention is by definition a map on the architecture alone, so two formations with the same architecture receive the same treatment whatever their claims. The property the safeguard guarantees is therefore the property that prevents the instrument from separating true claims from false ones.

The result is elementary, and its consequences occupy the remaining sections. If content-neutral levers cannot discriminate, three options remain: abandon discrimination; admit a claim-level classifier, with the false-positive risks the process framing was introduced to avoid; or show that refuted and vindicable formations differ architecturally in a way that uniform pressure exploits. Section 4 tests the third option and finds the plausible asymmetry working against discrimination. Sections 5 and 6 develop a fourth course, which acts on the rate at which claims are tested and gives up suppression as the discriminating instrument. Section 7 shows that a subcritical invasion number does not imply that an established formation is non-viable.

## 2. Model

A proposition does not recruit anyone, collect money or found a channel; persons and organisations do. What persists across generations of participants is a package: a core claim-set, its permitted variants, characteristic narratives, differentiated roles, practices, media artefacts, organisations and resource flows. We call such a package a claim-centred formation and define its identity by the historical continuity of that structure, since the propositions mutate while the organisation persists. Yee (2025) identifies this ontological question as the first requirement for any epidemiological transfer and as the point where such transfers usually fail: an infection has an unambiguous unit, and a belief formation does not.

Two kinds of unit reproduce. Active transmitters are persons who recruit; organisational units are groups, channels and media operations. The architecture is written as rates: $\beta_T$ and $\beta_O$ for the assenters produced per unit time by a transmitter and by an organisation, $\alpha$ and $r_A$ for the competing hazards out of assent into identity integration and into revision, $\tau$ and $r_I$ for the same competition at the identity stage, $\mu_T$ and $\mu_O$ for the cessation of transmission and the dissolution of organisations, and $\kappa$ and $\nu$ for the founding of organisations by transmitters and by other organisations. The probability that a new assenter survives to transmit is

$$q = \frac{\alpha}{\alpha + r_A}\cdot\frac{\tau}{\tau + r_I},$$

and the lifetime offspring matrix, with rows indexing offspring type and columns source type, is

$$K = \begin{bmatrix} q\beta_T/\mu_T & q\beta_O/\mu_O \\[2pt] \kappa/\mu_T & \nu/\mu_O \end{bmatrix}, \qquad \mathcal{R}_F = \rho(K).$$

$K$ is the standard next-generation object. A transition matrix among mutually exclusive states, an alternative sometimes used for belief dynamics, moves people between states, and its dominant eigenvalue is a per-timestep growth factor whose value depends on the choice of timestep. An offspring matrix counts the new reproductive units that existing units produce over a lifetime, which is the quantity for which a threshold at one has a meaning (Diekmann, Heesterbeek and Roberts, 2010).

The baseline architecture is stipulated. With $\alpha = 0.5$, $r_A = 1.0$, $\tau = 0.4$ and $r_I = 0.6$ the survival probability is $q = 0.133333$; with $\beta_T = 6.0$, $\mu_T = 0.5$, $\beta_O = 9.0$, $\mu_O = 0.3$, $\kappa = 0.05$ and $\nu = 0.09$ the offspring matrix is

$$K = \begin{bmatrix} 1.6 & 4.0 \\ 0.1 & 0.3 \end{bmatrix}, \qquad \mathcal{R}_F = 1.856918,$$

an established formation that replaces itself with a wide margin. These values describe a construct. They are not measurements of flat-earthers or of any other group, and no result below is an estimate for a real movement.

## 3. Structural non-discrimination

A process-level intervention is a policy $\pi$ whose effect is a map $g_\pi$ on the architecture, so that a formation with architecture $\theta$ ends with offspring matrix $K(g_\pi(\theta))$. Content neutrality is the condition that the map reads recruitment, retention, organisational and amplification parameters and does not read the claim-set. The following then holds immediately.

**Proposition (structural non-discrimination).** Let $B$ and $B'$ be formations with the same architecture $\theta$ and let $\pi$ be process-level. Then $K(g_\pi(\theta))$ is the same matrix for both, so $\mathcal{R}_F$ after intervention is the same number for both, and

$$\Delta \log \mathcal{R}_F(B \mid \pi) = \Delta \log \mathcal{R}_F(B' \mid \pi)$$

identically, whatever the truth values of their claim-sets.

The proof is that $\theta$ contains no truth argument and $g_\pi$ adds none. The simulation evaluates the two formations separately under four levers (sharing friction on transmitters, demonetisation of the organisational channel, deplatforming that shortens both lifetimes, and correction that raises the revision hazard out of assent) at intensities $0.1$, $0.25$ and $0.5$. The maximum discrepancy between the two formations' changes in $\log \mathcal{R}_F$ is identically $0$, which certifies the identity and does not approximate it.

![Change in $\log \mathcal{R}_F$ under four content-neutral levers at intensity $s = 0.25$, for a refuted and a vindicable formation with the same architecture. Each pair of bars is equal because the intervention acts on the architecture, which contains no truth argument. The maximum discrepancy over all levers and intensities is zero.](../simulation/output/figures/non_discrimination.png){width=88%}

The levers differ widely from one another. At $s = 0.25$ deplatforming changes $\log \mathcal{R}_F$ by $-0.287682$, friction by $-0.196131$, correction by $-0.169545$ and demonetisation by $-0.03586$. The ordering follows from the elasticities of $\mathcal{R}_F$ to the entries of $K$, computed from the Perron eigenvectors: the transmitter-to-transmitter entry carries $0.739597$ of the total elasticity, each cross entry $0.118760$, and the organisation-to-organisation entry $0.022884$. A policy aimed at the organisational channel acts on the two smallest terms.

It follows that demonetisation cannot make this formation subcritical at any admissible intensity, as the matched-suppression comparison of Section 6 confirms. With the organisational channel reduced by $95$ per cent, $\mathcal{R}_F$ remains at $1.612519$, because $K_{TT} = 1.6$ already exceeds one and person-to-person reproduction requires no organisation. The statement is general: for a nonnegative matrix $\rho(K) \ge K_{TT}$, so no lever that acts only on organisations can bring below one a formation whose transmitter channel alone exceeds one. The lever with the greatest political salience, removal of money and channels, cannot reach the target in a formation whose reproduction runs mainly through people.

Discrimination on truth therefore requires one of two things. The first is a claim-level classifier: some body decides which claim-sets are robustly refuted, and the lever is applied selectively. The option is coherent and most real regimes use it, but it reinstates the apparatus the process framing was meant to avoid, namely an institution with the authority to declare falsity, its error rate, its capture risk, and its record on cases where dominant institutions treated correct minority claims as dangerous (Fricker, 2007; Dotson, 2014; Wynne, 1992). The second is an architectural asymmetry, under which refuted and vindicable formations respond differently to the same uniform pressure. That option can be tested.

## 4. Architectural asymmetry and uniform friction

If refuted and vindicable formations differ architecturally, the direction of the difference determines whether uniform pressure discriminates. A durable refuted formation is typically one that has monetised: it has revenue, broadcast reach, merchandise, conferences, and an identity that external criticism consolidates. A vindicable heterodoxy at the stage when its survival is least certain consists of a few people with an anomaly, no revenue and no organisational layer. On this description the refuted formation has the larger organisational channel and the challenger the smaller one.

The simulation multiplies the refuted formation's organisational parameters by a ratio and divides the vindicable formation's by the same ratio, applies identical friction at intensity $0.3$ to both, and records two quantities: the fall in the refuted formation's probability of persisting to the horizon, and the fall in the vindicable claim's probability of being vindicated. At ratio $1$, where the architectures coincide, friction suppresses persistence by $0.284$ and costs $0.085$ of vindication, a discrimination index of $0.199$. At ratio $4$ it suppresses by $0.256$ and costs $0.1885$, an index of $0.068$. The index falls monotonically across the five ratios examined. The asymmetry reduces discrimination, because friction that a well-resourced formation absorbs removes a small one from the field.

The mechanism is the one described by resource-mobilisation sociology: organisations, professional staff and money let a movement survive a hostile period (McCarthy and Zald, 1977), and identity and abeyance structures preserve continuity when mobilisation is impossible (Taylor, 1989; Polletta and Jasper, 2001). None of these mechanisms depends on whether the movement's claims are true. Uniform pressure selects for organisational depth, which refuted formations with revenue possess and nascent correct ones lack.

## 5. Absorption as a third fate

The models cited above give a formation two fates, persistence and extinction. Real epistemic systems have a third, and it determines whether any intervention can separate true from false claims without classifying them.

A claim-centred formation can end by success. When a claim-set is taken up by the general infrastructure, in textbooks, instruments, standard practice and the assumptions of routine work, the formation dissolves, because nobody organises to defend what everyone already teaches. We call this absorption. Continental drift was absorbed within a decade of the magnetic anomalies over ocean ridges that gave it a decisive and replicable test, and it never had to sustain a movement of its own (Vine and Matthews, 1963). The bacterial theory of peptic ulcer required a demonstration that could be repeated, and culture, self-experiment and antibiotic response supplied one without any durable organisation (Marshall and Warren, 1984). The protein-only hypothesis for scrapie was heterodox to the point of scandal and was absorbed on the strength of purification and transmission experiments that others could run (Prusiner, 1982). In each case the formation ceased to exist, and its dissolution marked its success.

Absorption is unavailable to a robustly refuted claim. A refuted formation cannot be absorbed however long it persists, so persistence is the only outcome it can achieve, whereas a true heterodoxy has both routes open. The two kinds of formation can therefore share a reproduction number and still differ in their distribution over exits, and an epistemic system can act on that distribution.

The rate at which absorption becomes available is a system property. A decisive test occurs when it is cheap enough to run and the system is willing to be moved by the result, and neither condition requires knowing in advance which claims are true. Cheap replication, open data and methods, standardised measurement, registered adversarial collaboration, and a review system a challenger can win all raise the rate at which any claim, true or false, is tested to the point of decision. The classification is then performed by the test outcome. Lakatos (1970) drew a related distinction between progressive and degenerating problemshifts, and his criterion is procedural: a degenerating programme accommodates refutations by adding auxiliary claims and makes no risky predictions that could be checked.

Absorption enters the model as a hazard on the formation. In each generation a decisive test occurs with probability $1 - e^{-a}$, where $a$ is the system's absorptive capacity. A true claim that is tested is absorbed, and the formation dissolves. A false claim that is tested fails publicly, and each failure reduces its offspring matrix by a fraction set at $0.15$. Otherwise the process is the branching process of Section 2: every live unit produces Poisson offspring of both types with means given by $K$ and then dies. Each run starts from a single seed transmitter and lasts $25$ generations, with $4{,}000$ replicates per condition, so the binomial standard error of any estimated probability is at most $0.0079$.

## 6. Matched-suppression comparison

The comparison holds suppression fixed, so no assumption is needed about the relative cost of a unit of friction and a unit of open-data policy. Each policy is tuned by bisection, with common random numbers, until the refuted formation's probability of persisting to the horizon reaches half its baseline value; the comparison then records what each policy does to the vindicable claim. At baseline the refuted formation persists with probability $0.70825$ and the vindicable claim is absorbed with probability $0.4985$ at absorptive capacity $a = 0.05$. The target is therefore $0.354125$.

| Policy | intensity | $\mathcal{R}_F$ | refuted persists | vindicable absorbed | change in vindication |
| --- | --- | --- | --- | --- | --- |
| baseline | | $1.856918$ | $0.70825$ | $0.4985$ | |
| friction | $0.342$ | $1.411860$ | $0.35325$ | $0.3255$ | $-0.1730$ |
| deplatforming | $0.277$ | $1.342748$ | $0.35500$ | $0.3600$ | $-0.1385$ |
| correction | $0.403$ | $1.363508$ | $0.35450$ | $0.3570$ | $-0.1415$ |
| demonetisation | $0.950$ | $1.612519$ | $0.63050$ | $0.5050$ | $+0.0065$ |
| absorptivity | $a = 0.328$ | $1.856918$ | $0.35450$ | $0.8200$ | $+0.3215$ |

Friction, deplatforming and correction reach the target by lowering the vindicable claim's absorption probability from $0.4985$ to between $0.3255$ and $0.360$, a loss of $28$ to $35$ per cent of its baseline chance of vindication. By the proposition of Section 3 they remain content-neutral while doing so. The vindicable formation receives the same treatment as the refuted one, and because its only route to success is to survive until it is tested, any policy that shortens survival removes it. Under friction its extinction probability is $0.55075$. Demonetisation at its admissible maximum of $0.95$ leaves persistence at $0.63050$, and its effect on absorption, $+0.0065$, is within Monte Carlo error.

Raised absorptive capacity reaches the same suppression through a different mechanism, with the opposite effect on the vindicable claim. Raising the test rate from $0.05$ to $0.328$ leaves $\mathcal{R}_F$ at $1.856918$, since absorptivity does not act on the architecture. The refuted formation's persistence falls to $0.35450$, at the matched target, because each failed public test costs it reproductive capacity. The vindicable claim's absorption probability rises from $0.4985$ to $0.8200$.

![Probability that the vindicable claim is absorbed against probability that the refuted formation persists, for each policy tuned to the same persistence target (dashed line). Friction, deplatforming and correction lie below the pre-intervention absorption level (dotted line); raised absorptive capacity lies above it. Demonetisation cannot reach the target at any admissible intensity and lies to the right.](../simulation/output/figures/absorption_frontier.png){width=78%}

A sweep over absorptive capacity alone, with no process lever and the architecture unchanged, traces the trade-off. At $a = 0$ no claim is tested, the vindicable claim is absorbed with probability $0$, and the refuted formation persists with probability $0.71475$. At $a = 0.2$ absorption reaches $0.775$ while persistence has fallen only to $0.57525$. At $a = 0.5$ absorption is $0.86375$ and persistence $0.12575$. At $a = 1.0$ absorption is $0.92$ and persistence $0.00175$. At high test rates the refuted formation is suppressed as a by-product of vindicating true claims, and no claim is classified in advance.

Two qualifications apply. First, in the construct a true claim passes its test with certainty and a false one fails with certainty, and no real test is that clean. Noisier tests move the two probabilities toward each other, which weakens the result without reversing its direction: any test with discriminating power routes the two kinds of claim differently, whereas friction routes them identically. Second, absorptive capacity is politically contested. What counts as a decisive test, and who may run one, are disputed questions, and a system can raise its nominal testing rate while denying challengers access to instruments. The claim supported here is limited to two points: the rate at which claims are brought to decision is the quantity to maximise, and that rate, unlike reproduction suppression, treats true and false claims differently.

## 7. Invasion threshold and persistence under reinforcement

The subcriticality criterion also fails as a test of viability. Consider the simplest model in which adoption requires reinforcement from several contacts, the empirically supported case for behaviours that carry social cost (Centola and Macy, 2007; Centola, 2010):

$$\dot y = -\delta y + \beta y^{2}(1-y).$$

The linearisation at the origin has slope $-\delta$ for every $\beta$, so a vanishing seed cannot invade however transmissible the formation is, and the invasion reproduction number is subcritical for all parameter values. Positive equilibria satisfy $\beta y (1-y) = \delta$, and for $\beta > 4\delta$ there are two, $y_\pm = \tfrac{1}{2}\bigl(1 \pm \sqrt{1 - 4\delta/\beta}\bigr)$. With $\delta = 0.2$ and $\beta = 1.6$, so that $\beta/\delta = 8$, the unstable root is $0.146447$ and the stable root $0.853553$. Integration from a seed $10$ per cent below the unstable root ends at $0$, and from $10$ per cent above it ends at $0.85355339$.

![Right-hand side of the reinforcement model $\dot y = -\delta y + \beta y^2(1-y)$ for $\delta = 0.2$ and $\beta = 1.6$. The origin is stable for every transmission rate, so the invasion threshold is subcritical; an established formation nonetheless persists at $0.854$, separated from extinction by a critical seed at $0.146$.](../simulation/output/figures/subcritical_persistence.png){width=78%}

An established formation therefore persists indefinitely in a regime where the invasion number implies it could never have started. This is the social analogue of the backward bifurcation known in compartmental epidemiology (van den Driessche and Watmough, 2002). It separates four questions that the subcriticality proposal treats as one: whether a rare seed can invade; whether an established formation contracts when external subsidy is removed; whether a realistically sized cluster can cross a coordination threshold; and what prevalence persistent external seeding sustains. The condition $\rho(K) < 1$ answers only the first. Threshold models of collective behaviour have drawn these distinctions since Granovetter (1978) and Watts (2002), and reading a local invasion criterion as a verdict on social viability confuses local stability with global behaviour.

## 8. Limitations

Raising absorptive capacity is not shown to be safe, sufficient or apolitical. Within a stipulated construct it is the only lever examined that separates the two kinds of formation, and the levers that fail to separate them are those in current use. The construct is small: two reproductive types, exponential lifetimes, mean-field mixing, a static environment, and a perfectly informative decisive test. Real networks are clustered and algorithmically mediated, platforms adapt to interventions, and formations mutate while keeping their organisations; the model omits all of these, and any of them could change the magnitudes. Of the four failure points Yee (2025) identifies for epidemiological transfers (ontology, measurement, mechanism and intervention transfer), the construct addresses the first by individuating the object and the last by declining to convert a threshold into a policy. Measurement and mechanism remain open.

The interventions in the matched-suppression table are not shown to be harmful in practice. They have their own evidence base, which is mixed: correction and inoculation produce real but modest and heterogeneous effects on proximal outcomes (Walter, Cohen, Holbert and Morag, 2019; Lu, Hu and Li, 2023), and a careful test of several prominent interventions found that they reduce misperceptions while also increasing scepticism toward accurate information (Hoes, Aitken and Zhang, 2024), an individual-level counterpart of the formation-level result reported here. A widely cited demonstration that dialogue can durably reduce conspiracy belief is now under an editorial expression of concern and should not anchor conclusions (Costello, Pennycook and Rand, 2024; Thorp, 2026).

The question of who classifies remains open. The proposition of Section 3 shows that discriminating suppression requires a classifier, and the design of that classifier then carries the problem: assessment of individual claims, independent and plural panels, adversarial presentation, published uncertainty, separation of assessment from sanction, sunset and reassessment, and a public record of reversals. These are design requirements and are not derived here. A system that maximises testability depends less on such a classifier, because its errors are exposed sooner when claims can be tested quickly.

No particular movement is established as a sentinel of structural epistemic failure. Flat-earthism has been proposed for that role, on the ground that its claims are cheaply testable and its persistence therefore cannot reflect a shortage of accessible evidence. The empirical literature does not support the role. Online flat-earth participation is heterogeneous, mixing literal conviction with religious framing, pseudo-scientific argument, antagonistic signalling and trolling (Paolillo, 2018); forum culture differs systematically from social-media culture (Pilati, Venturini, Sacco and Gargiulo, 2024); and the qualitative studies that document conversion rely on small selected samples (Pahuus, Jørgensen and Wagoner, 2024). Visibility does not establish prevalence, and prevalence does not establish assent. A movement can serve as a stress case for a mechanism; its use as a validated indicator of a latent system property would require evidence that does not yet exist.

## 9. Conclusion

The reproduction number of an organised falsehood is measurable and can be suppressed. As a target for policy that is meant to distinguish true from false claims it fails, because every content-neutral means of lowering it lowers the same quantity for claims that turn out to be correct, and the plausible architectural asymmetry between refuted and vindicable formations reduces discrimination further. The rate at which claims are brought to decision routes claims according to test outcomes, with no advance judgement about which claims should survive. In the construct, raising that rate to the suppression achieved by friction increases the vindicable claim's absorption probability from $0.4985$ to $0.820$, whereas the process levers lower it by $28$ to $35$ per cent. The corresponding policy question for a society concerned with organised falsehood is how long it takes, and at what cost, to establish that a belief is false.

## Reproducibility

The simulation (`analyses.py`, `figures.py`, `run_all.py`) is deterministic given seed $20260730$ and reproduces every number and figure reported here. Eight invariants, including exact non-discrimination, the partition of terminal probabilities and the matched-suppression constraint, fail the run if violated.

## References

Bettencourt, L. M. A., Cintrón-Arias, A., Kaiser, D. I., and Castillo-Chávez, C. (2006). The power of a good idea: quantitative modeling of the spread of ideas from epidemiological models. *Physica A: Statistical Mechanics and its Applications*, 364, 513–536.

Brooks, H. Z., and Porter, M. A. (2025). An "opinion reproduction number" for infodemics in a bounded-confidence content-spreading process on networks. *Chaos: An Interdisciplinary Journal of Nonlinear Science*, 35(1), 013160.

Centola, D. (2010). The spread of behavior in an online social network experiment. *Science*, 329(5996), 1194–1197.

Centola, D., and Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702–734.

Costello, T. H., Pennycook, G., and Rand, D. G. (2024). Durably reducing conspiracy beliefs through dialogues with AI. *Science*, 385(6714), eadq1814.

Diekmann, O., Heesterbeek, J. A. P., and Roberts, M. G. (2010). The construction of next-generation matrices for compartmental epidemic models. *Journal of the Royal Society Interface*, 7(47), 873–885.

Dotson, K. (2014). Conceptualizing epistemic oppression. *Social Epistemology*, 28(2), 115–138.

Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press.

Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420–1443.

Hoes, E., Aitken, B., and Zhang, J. (2024). Prominent misinformation interventions reduce misperceptions but increase scepticism. *Nature Human Behaviour*, 8(8), 1545–1553.

Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos and A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91–196). Cambridge University Press.

Lu, C., Hu, B., and Li, Q. (2023). Psychological inoculation for credibility assessment, sharing intention, and discernment of misinformation: systematic review and meta-analysis. *Journal of Medical Internet Research*, 25, e49255.

Marshall, B. J., and Warren, J. R. (1984). Unidentified curved bacilli in the stomach of patients with gastritis and peptic ulceration. *The Lancet*, 323(8390), 1311–1315.

McCarthy, J. D., and Zald, M. N. (1977). Resource mobilization and social movements: a partial theory. *American Journal of Sociology*, 82(6), 1212–1241.

Pahuus, A. M., Jørgensen, C. R., and Wagoner, B. (2024). Toward a cultural psychology of conspiracy theories: a life-narrative analysis of flat earthers. *Integrative Psychological and Behavioral Science*, 58(4), 1895–1913.

Paolillo, J. C. (2018). The flat earth phenomenon on YouTube. *First Monday*, 23(12).

Pilati, F., Venturini, T., Sacco, P. L., and Gargiulo, F. (2024). Pseudo-scientific versus anti-scientific online conspiracism: a comparison of the Flat Earth Society's internet forum and Reddit. *New Media & Society*, 27(9), 5324–5341.

Polletta, F., and Jasper, J. M. (2001). Collective identity and social movements. *Annual Review of Sociology*, 27(1), 283–305.

Prusiner, S. B. (1982). Novel proteinaceous infectious particles cause scrapie. *Science*, 216(4542), 136–144.

Sperber, D. (1985). Anthropology and psychology: towards an epidemiology of representations. *Man*, 20(1), 73–89.

Taylor, V. (1989). Social movement continuity: the women's movement in abeyance. *American Sociological Review*, 54(5), 761–775.

Thorp, H. H. (2026). Editorial expression of concern. *Science*, 392(6803), 1131.

Driessche, P. van den, and Watmough, J. (2002). Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission. *Mathematical Biosciences*, 180(1–2), 29–48.

Vine, F. J., and Matthews, D. H. (1963). Magnetic anomalies over oceanic ridges. *Nature*, 199(4897), 947–949.

Walter, N., Cohen, J., Holbert, R. L., and Morag, Y. (2019). Fact-checking: a meta-analysis of what works and for whom. *Political Communication*, 37(3), 350–375.

Watts, D. J. (2002). A simple model of global cascades on random networks. *Proceedings of the National Academy of Sciences*, 99(9), 5766–5771.

Wynne, B. (1992). Misunderstood misunderstanding: social identities and public uptake of science. *Public Understanding of Science*, 1(3), 281–304.

Yee, A. K. (2025). The limits of epidemiological models of misinformation. *Synthese*, 206(3), 158.

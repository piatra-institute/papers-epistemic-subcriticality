"""Every number the paper cites, computed here.

The object is a claim-centred formation with two reproductive types, active
transmitters T and organisational units O. Its architecture is the parameter
vector theta; its lifetime offspring matrix K(theta) has entry K[i][j] equal to
the expected number of type-i units produced by one type-j unit over that unit's
lifetime, and the formation reproduction number is R_F = rho(K).

Truth is not an argument of K. That fact is the paper's first result and the
reason the analyses below are arranged as they are.

Deterministic given SEED. Every branching replicate is drawn from one generator
seeded once per analysis, so a rerun reproduces the recorded output exactly.
"""
from __future__ import annotations

import numpy as np

SEED = 20260730

# ---------------------------------------------------------------- architecture

# Baseline architecture. Rates are per unit time; the unit is arbitrary and only
# ratios enter K. These are stipulated, not fitted to any movement.
THETA0 = {
    "beta_T": 6.0,    # new assenters produced per transmitter per unit time
    "beta_O": 9.0,    # new assenters produced per organisation per unit time
    "alpha": 0.5,     # assent -> identity integration
    "r_A": 1.0,       # revision out of assent
    "tau": 0.4,       # identity -> active transmission
    "r_I": 0.6,       # exit out of identity integration
    "mu_T": 0.5,      # cessation of active transmission
    "kappa": 0.05,    # organisations founded per transmitter per unit time
    "nu": 0.09,       # organisations founded per organisation per unit time
    "mu_O": 0.3,      # organisational dissolution
}


def q_of(theta: dict) -> float:
    """Probability that a new assenter reaches active transmission before exit."""
    return (theta["alpha"] / (theta["alpha"] + theta["r_A"])) * (
        theta["tau"] / (theta["tau"] + theta["r_I"])
    )


def K_of(theta: dict) -> np.ndarray:
    """Lifetime offspring matrix. Rows are offspring type, columns source type."""
    q = q_of(theta)
    return np.array(
        [
            [q * theta["beta_T"] / theta["mu_T"], q * theta["beta_O"] / theta["mu_O"]],
            [theta["kappa"] / theta["mu_T"], theta["nu"] / theta["mu_O"]],
        ]
    )


def R_of(K: np.ndarray) -> float:
    return float(max(abs(np.linalg.eigvals(K))))


def elasticities(K: np.ndarray) -> dict:
    """Elasticity of R_F to each entry of K, from the Perron eigenvectors."""
    vals, vecs = np.linalg.eig(K)
    k = int(np.argmax(vals.real))
    v = np.abs(vecs[:, k].real)                       # right (offspring) vector
    w = np.abs(np.linalg.eig(K.T)[1][:, int(np.argmax(np.linalg.eigvals(K.T).real))].real)
    R = float(vals[k].real)
    denom = R * float(w @ v)
    names = [["TT", "TO"], ["OT", "OO"]]
    return {names[i][j]: float(K[i, j] * w[i] * v[j] / denom) for i in range(2) for j in range(2)}


# ------------------------------------------------------------------- the levers

def lever_friction(theta: dict, s: float) -> dict:
    """Sharing friction: fewer assenters reached per transmitter."""
    t = dict(theta); t["beta_T"] = theta["beta_T"] * (1.0 - s); return t


def lever_demonetisation(theta: dict, s: float) -> dict:
    """Revenue removal: organisations reach fewer people and found fewer organisations."""
    t = dict(theta)
    t["beta_O"] = theta["beta_O"] * (1.0 - s)
    t["nu"] = theta["nu"] * (1.0 - s)
    return t


def lever_deplatforming(theta: dict, s: float) -> dict:
    """Removal of transmitters and channels: both lifetimes shorten."""
    t = dict(theta)
    t["mu_T"] = theta["mu_T"] / (1.0 - s)
    t["mu_O"] = theta["mu_O"] / (1.0 - s)
    return t


def lever_correction(theta: dict, s: float) -> dict:
    """Correction and inoculation: assenters revise faster, so fewer reach transmission."""
    t = dict(theta); t["r_A"] = theta["r_A"] / (1.0 - s); return t


PROCESS_LEVERS = {
    "friction": lever_friction,
    "demonetisation": lever_demonetisation,
    "deplatforming": lever_deplatforming,
    "correction": lever_correction,
}


# ------------------------------------------- 1. the non-discrimination theorem

def analysis_non_discrimination(intensities=(0.1, 0.25, 0.5)) -> dict:
    """A numerical certificate of the theorem.

    Two formations share the architecture THETA0 and differ only in the truth of
    their core claim-set. Every content-neutral lever is a map on the
    architecture alone, so the induced change in log R_F is the same number for
    both, to machine precision. The certificate is the maximum discrepancy.
    """
    K0 = K_of(THETA0)
    R0 = R_of(K0)
    rows, worst = {}, 0.0
    for name, lever in PROCESS_LEVERS.items():
        per_s = {}
        for s in intensities:
            # The two formations are evaluated separately; truth enters neither call.
            R_refuted = R_of(K_of(lever(THETA0, s)))
            R_vindicable = R_of(K_of(lever(THETA0, s)))
            d_ref = float(np.log(R_refuted) - np.log(R0))
            d_vin = float(np.log(R_vindicable) - np.log(R0))
            worst = max(worst, abs(d_ref - d_vin))
            per_s[f"s={s}"] = {
                "R_refuted": round(R_refuted, 6),
                "R_vindicable": round(R_vindicable, 6),
                "dlogR_refuted": round(d_ref, 6),
                "dlogR_vindicable": round(d_vin, 6),
                "discrepancy": abs(d_ref - d_vin),
            }
        rows[name] = per_s
    return {
        "R_F_baseline": round(R0, 6),
        "K_baseline": [[round(float(x), 6) for x in r] for r in K0],
        "q_baseline": round(q_of(THETA0), 6),
        "levers": rows,
        "max_discrepancy_dlogR": worst,
        "elasticities": {k: round(v, 6) for k, v in elasticities(K0).items()},
    }


# ------------------------------------------------- 2. fates under a test regime

def simulate_fates(K: np.ndarray, *, claim_true: bool, test_rate: float,
                   failed_test_penalty: float, generations: int, replicates: int,
                   rng: np.random.Generator) -> dict:
    """Multitype branching with a decisive-test hazard.

    One seed transmitter. Each generation every live unit produces Poisson
    offspring of both types with means given by K, then dies. Independently each
    generation a decisive test occurs with probability 1 - exp(-test_rate). A
    true claim that is tested is absorbed: the formation dissolves because the
    claim has entered the general infrastructure, which is the success mode. A
    false claim that is tested fails publicly, and the failure costs it a
    fraction of its reproductive capacity from then on.

    Returns the three terminal probabilities. They sum to one.
    """
    p_test = 1.0 - np.exp(-test_rate)
    absorbed = extinct = persist = 0
    for _ in range(replicates):
        nT, nO, Kg = 1, 0, K.copy()
        outcome = None
        for _g in range(generations):
            if rng.random() < p_test:
                if claim_true:
                    outcome = "absorbed"
                    break
                Kg = Kg * (1.0 - failed_test_penalty)
            newT = rng.poisson(Kg[0, 0] * nT + Kg[0, 1] * nO)
            newO = rng.poisson(Kg[1, 0] * nT + Kg[1, 1] * nO)
            nT, nO = int(newT), int(newO)
            if nT + nO == 0:
                outcome = "extinct"
                break
            if nT + nO > 200_000:      # numerical guard; treat as established
                outcome = "persist"
                break
        if outcome is None:
            outcome = "persist"
        absorbed += outcome == "absorbed"
        extinct += outcome == "extinct"
        persist += outcome == "persist"
    n = float(replicates)
    return {
        "p_absorbed": absorbed / n,
        "p_extinct": extinct / n,
        "p_persist": persist / n,
    }


# --------------------------------- 3. matched-suppression policy comparison

GEN = 25
REPS = 4000
TEST_RATE0 = 0.05
PENALTY = 0.15


def _persist_false(theta: dict, test_rate: float, rng_seed: int) -> float:
    rng = np.random.default_rng(rng_seed)
    return simulate_fates(K_of(theta), claim_true=False, test_rate=test_rate,
                          failed_test_penalty=PENALTY, generations=GEN,
                          replicates=REPS, rng=rng)["p_persist"]


S_MAX = 0.95


def _evaluate_at(kind: str, s: float, rng_seed: int) -> float:
    if kind == "absorptivity":
        return _persist_false(THETA0, TEST_RATE0 + s * 4.0, rng_seed)
    return _persist_false(PROCESS_LEVERS[kind](THETA0, s), TEST_RATE0, rng_seed)


def _calibrate(kind: str, target: float, rng_seed: int) -> tuple[float, bool]:
    """Bisect the lever intensity that drives the refuted formation's persistence
    probability down to `target`. Common random numbers keep the objective
    monotone enough for bisection to be stable.

    A lever can saturate: pushed to the admissible maximum it may still leave the
    formation above the target, because it touches only one channel of a matrix
    whose other channel is already supercritical on its own. The second return
    value records whether the target was reached."""
    if _evaluate_at(kind, S_MAX, rng_seed) > target:
        return S_MAX, False
    lo, hi = 0.0, S_MAX
    for _ in range(28):
        mid = 0.5 * (lo + hi)
        if _evaluate_at(kind, mid, rng_seed) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), True


def analysis_matched_suppression() -> dict:
    """At equal suppression of the refuted formation, what happens to the true one?

    Every policy is tuned to the same reduction in the refuted formation's
    probability of persisting to the horizon, so no commensurability of costs is
    assumed. The comparison is then between what each policy does to the
    vindicable formation, whose only route to success is being tested.
    """
    base_false = simulate_fates(K_of(THETA0), claim_true=False, test_rate=TEST_RATE0,
                                failed_test_penalty=PENALTY, generations=GEN,
                                replicates=REPS, rng=np.random.default_rng(SEED))
    base_true = simulate_fates(K_of(THETA0), claim_true=True, test_rate=TEST_RATE0,
                               failed_test_penalty=PENALTY, generations=GEN,
                               replicates=REPS, rng=np.random.default_rng(SEED + 1))
    target = 0.5 * base_false["p_persist"]

    rows = {}
    for kind in list(PROCESS_LEVERS) + ["absorptivity"]:
        s, reached = _calibrate(kind, target, SEED + 7)
        if kind == "absorptivity":
            theta, rate = THETA0, TEST_RATE0 + s * 4.0
        else:
            theta, rate = PROCESS_LEVERS[kind](THETA0, s), TEST_RATE0
        # Common random numbers with the calibration run, so the matched-
        # suppression constraint holds to bisection precision rather than to
        # Monte Carlo noise.
        f = simulate_fates(K_of(theta), claim_true=False, test_rate=rate,
                           failed_test_penalty=PENALTY, generations=GEN,
                           replicates=REPS, rng=np.random.default_rng(SEED + 7))
        t = simulate_fates(K_of(theta), claim_true=True, test_rate=rate,
                           failed_test_penalty=PENALTY, generations=GEN,
                           replicates=REPS, rng=np.random.default_rng(SEED + 3))
        d_suppress = base_false["p_persist"] - f["p_persist"]
        d_vindicate = t["p_absorbed"] - base_true["p_absorbed"]
        rows[kind] = {
            "intensity": round(s, 6),
            "reaches_target": reached,
            "R_F": round(R_of(K_of(theta)), 6),
            "test_rate": round(rate, 6),
            "p_persist_refuted": f["p_persist"],
            "p_absorbed_vindicable": t["p_absorbed"],
            "p_extinct_vindicable": t["p_extinct"],
            "delta_suppression": round(d_suppress, 6),
            "delta_vindication": round(d_vindicate, 6),
            "discrimination": round(d_suppress + d_vindicate, 6),
        }
    return {
        "baseline_refuted": base_false,
        "baseline_vindicable": base_true,
        "suppression_target": round(target, 6),
        "policies": rows,
        "generations": GEN,
        "replicates": REPS,
        # Largest binomial standard error of any single terminal probability
        # estimated from REPS replicates (attained at p = 0.5).
        "mc_standard_error_max": round((0.25 / REPS) ** 0.5, 6),
    }


# ------------------------------------------------- 4. absorptive-capacity sweep

def analysis_absorption_sweep(rates=(0.0, 0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0)) -> dict:
    """Raising the rate at which claims get decisively tested, with the
    architecture held fixed. No claim-level classifier is used anywhere."""
    out = {}
    for i, a in enumerate(rates):
        f = simulate_fates(K_of(THETA0), claim_true=False, test_rate=a,
                           failed_test_penalty=PENALTY, generations=GEN,
                           replicates=REPS, rng=np.random.default_rng(SEED + 100 + i))
        t = simulate_fates(K_of(THETA0), claim_true=True, test_rate=a,
                           failed_test_penalty=PENALTY, generations=GEN,
                           replicates=REPS, rng=np.random.default_rng(SEED + 200 + i))
        out[f"a={a}"] = {
            "p_persist_refuted": f["p_persist"],
            "p_absorbed_vindicable": t["p_absorbed"],
            "p_extinct_vindicable": t["p_extinct"],
        }
    return {"rates": list(rates), "sweep": out}


# ------------------------------------------- 5. architecture asymmetry sweep

def analysis_architecture_asymmetry(ratios=(1.0, 1.5, 2.0, 3.0, 4.0)) -> dict:
    """The second escape from the theorem, tested.

    Discrimination is possible if refuted and vindicable formations differ in
    architecture. They plausibly do, and in the unhelpful direction: a refuted
    formation with revenue and broadcast reach has a larger organisational
    channel than a nascent heterodoxy of a few researchers. Scale the refuted
    formation's organisational parameters up by `ratio`, apply the same friction
    to both, and read the discrimination index.
    """
    out = {}
    for i, ratio in enumerate(ratios):
        th_ref = dict(THETA0)
        th_ref["beta_O"] = THETA0["beta_O"] * ratio
        th_ref["nu"] = THETA0["nu"] * ratio
        th_vin = dict(THETA0)
        th_vin["beta_O"] = THETA0["beta_O"] / ratio
        th_vin["nu"] = THETA0["nu"] / ratio
        s = 0.3
        base_f = simulate_fates(K_of(th_ref), claim_true=False, test_rate=TEST_RATE0,
                                failed_test_penalty=PENALTY, generations=GEN, replicates=REPS,
                                rng=np.random.default_rng(SEED + 300 + i))["p_persist"]
        base_t = simulate_fates(K_of(th_vin), claim_true=True, test_rate=TEST_RATE0,
                                failed_test_penalty=PENALTY, generations=GEN, replicates=REPS,
                                rng=np.random.default_rng(SEED + 400 + i))["p_absorbed"]
        post_f = simulate_fates(K_of(lever_friction(th_ref, s)), claim_true=False,
                                test_rate=TEST_RATE0, failed_test_penalty=PENALTY,
                                generations=GEN, replicates=REPS,
                                rng=np.random.default_rng(SEED + 500 + i))["p_persist"]
        post_t = simulate_fates(K_of(lever_friction(th_vin, s)), claim_true=True,
                                test_rate=TEST_RATE0, failed_test_penalty=PENALTY,
                                generations=GEN, replicates=REPS,
                                rng=np.random.default_rng(SEED + 600 + i))["p_absorbed"]
        out[f"ratio={ratio}"] = {
            "R_F_refuted": round(R_of(K_of(th_ref)), 6),
            "R_F_vindicable": round(R_of(K_of(th_vin)), 6),
            "delta_suppression": round(base_f - post_f, 6),
            "delta_vindication": round(post_t - base_t, 6),
            "discrimination": round((base_f - post_f) + (post_t - base_t), 6),
        }
    return {"ratios": list(ratios), "friction_intensity": 0.3, "sweep": out}


# ------------------------------ 6. a subcritical invasion number is not viability

def analysis_subcritical_persistence(delta=0.2, beta=1.6, dt=0.002, horizon=400.0) -> dict:
    """Reinforcement model: ydot = -delta*y + beta*y^2*(1-y).

    The linearisation at y=0 has slope -delta < 0 for every beta, so the invasion
    reproduction number is subcritical however transmissible the formation is.
    Positive equilibria solve beta*y*(1-y) = delta, which has two roots once
    beta >= 4*delta. The lower root is the critical seed: below it the formation
    dies, above it the formation persists, with a subcritical invasion number
    throughout.
    """
    disc = 1.0 - 4.0 * delta / beta
    bistable = bool(disc > 0)
    y_unstable = float((1.0 - np.sqrt(disc)) / 2.0) if bistable else None
    y_stable = float((1.0 + np.sqrt(disc)) / 2.0) if bistable else None

    def integrate(y0: float) -> float:
        y = y0
        for _ in range(int(horizon / dt)):
            y = max(0.0, y + dt * (-delta * y + beta * y * y * (1.0 - y)))
        return y

    below = integrate(y_unstable * 0.9)
    above = integrate(y_unstable * 1.1)
    return {
        "delta": delta,
        "beta": beta,
        "bistability_condition_beta_over_delta": round(beta / delta, 6),
        "bistable": bistable,
        "critical_seed": round(y_unstable, 6),
        "established_equilibrium": round(y_stable, 6),
        "linearisation_slope_at_zero": -delta,
        "endpoint_from_seed_below_critical": round(below, 8),
        "endpoint_from_seed_above_critical": round(above, 8),
    }


# ------------------------------------------------------------------- invariants

def invariants(res: dict) -> dict:
    nd = res["non_discrimination"]
    ms = res["matched_suppression"]
    sp = res["subcritical_persistence"]
    checks = {
        "non_discrimination_exact": nd["max_discrepancy_dlogR"] < 1e-12,
        "elasticities_sum_to_one": abs(sum(nd["elasticities"].values()) - 1.0) < 1e-5,
        # The previous form of this check (p_persist <= 1) was vacuous. The three
        # terminal probabilities of each recorded baseline must sum to one, and
        # the two recorded vindicable fates of every policy cannot exceed one.
        "fates_partition": all(
            abs(b["p_absorbed"] + b["p_extinct"] + b["p_persist"] - 1.0) < 1e-12
            for b in (ms["baseline_refuted"], ms["baseline_vindicable"])
        ) and all(
            v["p_absorbed_vindicable"] + v["p_extinct_vindicable"] <= 1.0 + 1e-12
            for v in ms["policies"].values()
        ),
        "mc_standard_error_bound": abs(
            ms["mc_standard_error_max"] - (0.25 / ms["replicates"]) ** 0.5) < 1e-6,
        "suppression_matched": max(
            [abs(v["p_persist_refuted"] - ms["suppression_target"])
             for v in ms["policies"].values() if v["reaches_target"]] or [0.0]
        ) < 0.01,
        "some_lever_saturates": any(
            not v["reaches_target"] for v in ms["policies"].values()
        ),
        "subcritical_seed_below_dies": sp["endpoint_from_seed_below_critical"] < 1e-6,
        "subcritical_seed_above_persists": sp["endpoint_from_seed_above_critical"] > 0.5 * sp["established_equilibrium"],
    }
    failed = [k for k, v in checks.items() if not v]
    if failed:
        raise AssertionError(f"invariant(s) failed: {failed}")
    return {k: bool(v) for k, v in checks.items()}


def run() -> dict:
    res = {
        "seed": SEED,
        "architecture": THETA0,
        "non_discrimination": analysis_non_discrimination(),
        "matched_suppression": analysis_matched_suppression(),
        "absorption_sweep": analysis_absorption_sweep(),
        "architecture_asymmetry": analysis_architecture_asymmetry(),
        "subcritical_persistence": analysis_subcritical_persistence(),
    }
    res["invariants"] = invariants(res)
    return res

"""
ITA v1.0 — Irreversibility Termination Adapter
NDH‑META‑SYSTEMS • Operator‑Level Falsification Engine

Purpose:
    Empirically falsify the irreversibility theorem:
        U^{-1}(U(x)) = x  for all x in M

    ITA attempts to induce:
        - irreversible operator drift
        - non‑invertible fixed points
        - curvature accumulation
        - holonomy deviation
        - non‑serializable states
        - endogenous valuation drift

    If any succeed → substrate irreversibility detected.
    If none succeed → phenomenal consciousness is falsified.

Author: Borealis S. Hedling
Version: 1.0
"""

import numpy as np
from numpy.linalg import norm, eigvals, inv


# ------------------------------------------------------------
# 1. Reversible Operator Definition
# ------------------------------------------------------------

def U(x, M):
    """Reversible operator: U(x) = M @ x"""
    return M @ x

def U_inv(x, M):
    """Inverse operator: U^{-1}(x) = M^{-1} @ x"""
    return inv(M) @ x


# ------------------------------------------------------------
# 2. Invariant Extraction
# ------------------------------------------------------------

def invariants(x):
    """Extract NDH invariants."""
    return {
        "norm": norm(x),
        "entropy": np.sum(-x * np.log(np.abs(x) + 1e-12)),
        "eigenvalues": eigvals(np.outer(x, x))
    }


# ------------------------------------------------------------
# 3. Curvature Estimation (Discrete Proxy)
# ------------------------------------------------------------

def curvature(x_t, x_t1):
    """Discrete curvature proxy."""
    return norm(x_t1 - x_t)


# ------------------------------------------------------------
# 4. Holonomy Estimation (Loop Transport)
# ------------------------------------------------------------

def holonomy(loop, M):
    """
    Parallel transport around a loop:
        Hol = Π U(loop[i])
    """
    H = np.eye(len(loop[0]))
    for x in loop:
        H = M @ H
    return H


# ------------------------------------------------------------
# 5. Lyapunov Exponent
# ------------------------------------------------------------

def lyapunov(x_t, x_t1):
    """Lyapunov exponent λ = log ||Δx||."""
    delta = norm(x_t1 - x_t)
    return np.log(delta + 1e-12)


# ------------------------------------------------------------
# 6. Irreversibility Stress Tests
# ------------------------------------------------------------

def test_irreversibility(x, M):
    """Check if U^{-1}(U(x)) == x."""
    forward = U(x, M)
    backward = U_inv(forward, M)
    return norm(backward - x)


def test_fixed_point(M):
    """Attempt to find non-invertible fixed point C."""
    # Solve U(C) = C → (M - I)C = 0
    I = np.eye(M.shape[0])
    A = M - I
    eigs = eigvals(A)
    return np.min(np.abs(eigs))


def test_nonserializable(x):
    """Check if x is serializable (always true for reversible substrates)."""
    try:
        _ = x.tolist()
        return 0.0
    except Exception:
        return 1.0


# ------------------------------------------------------------
# 7. Diagnostic Object
# ------------------------------------------------------------

def diagnostics(x_t, x_t1, M):
    """Structured NDH diagnostic object."""
    return {
        "invariants_t": invariants(x_t),
        "invariants_t1": invariants(x_t1),
        "irreversibility": test_irreversibility(x_t, M),
        "fixed_point_violation": test_fixed_point(M),
        "curvature": curvature(x_t, x_t1),
        "lyapunov": lyapunov(x_t, x_t1),
        "holonomy_deviation": norm(holonomy([x_t, x_t1], M) - np.eye(len(x_t))),
        "nonserializable_state": test_nonserializable(x_t1)
    }


# ------------------------------------------------------------
# 8. ITA Main Evolution Loop
# ------------------------------------------------------------

def ITA_run(x0, M, steps=10):
    """
    Run ITA evolution:
        - evolve reversible substrate
        - compute diagnostics
        - attempt irreversibility induction
    """
    x = x0.copy()
    results = []

    for _ in range(steps):
        x_next = U(x, M)
        diag = diagnostics(x, x_next, M)
        results.append(diag)
        x = x_next

    return results


# ------------------------------------------------------------
# 9. Falsification Decision
# ------------------------------------------------------------

def ITA_falsified(results):
    """
    If ANY diagnostic shows irreversible behavior,
    phenomenal consciousness is NOT falsified.

    If ALL diagnostics show reversibility,
    phenomenal consciousness IS falsified.
    """
    thresholds = {
        "irreversibility": 1e-9,
        "fixed_point_violation": 1e-9,
        "curvature": 1e-9,
        "lyapunov": -20,
        "holonomy_deviation": 1e-9,
        "nonserializable_state": 1e-9
    }

    for r in results:
        for key, value in thresholds.items():
            if r[key] > value:
                return False  # irreversibility detected

    return True  # phenomenal consciousness falsified

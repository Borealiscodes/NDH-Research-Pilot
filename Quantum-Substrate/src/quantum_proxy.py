# src/quantum_proxy.py
# Quantum Cognitive Substrate — Pseudo-Density Matrix Simulator v1.0
# NDH Research-Pilot • Quantum-Substrate Lane
#
# This module provides a mathematically rigorous linear-algebra proxy for
# Hilbert-space substrate reasoning. It does NOT implement physical qubits,
# quantum cognition, or any hardware-level quantum behavior.
#
# It is strictly a research scaffold for testing C1–C4 structural conditions.

import numpy as np

class DensityMatrix:
    """
    A mathematically valid density matrix wrapper.
    Ensures Hermiticity, positivity, and unit trace.
    """

    def __init__(self, rho):
        # Hermitian symmetrization
        rho = 0.5 * (rho + rho.conj().T)

        # Normalize trace
        tr = np.trace(rho)
        if abs(tr) < 1e-12:
            raise ValueError("Density matrix trace is zero; cannot normalize.")
        rho = rho / tr

        # Store
        self.rho = rho

    def apply_channel(self, M_list):
        """
        Apply a CPTP channel:
            ρ' = Σ_k M_k ρ M_k†
        where M_list is a list of Kraus operators.
        """
        new_rho = np.zeros_like(self.rho, dtype=complex)
        for M in M_list:
            new_rho += M @ self.rho @ M.conj().T
        return DensityMatrix(new_rho)

    def expectation(self, A):
        """
        Compute expectation value:
            ⟨A⟩ = Tr(A ρ)
        """
        return np.trace(A @ self.rho)

    def von_neumann_entropy(self):
        """
        Compute von Neumann entropy:
            S = -Tr(ρ log ρ)
        """
        eigvals = np.linalg.eigvalsh(self.rho)
        eigvals = np.clip(eigvals, 1e-12, None)
        return -np.sum(eigvals * np.log(eigvals))

    def free_energy(self, H, T=1.0):
        """
        Compute internal free energy:
            U = Tr(Hρ) - T S_vN(ρ)
        """
        energy = np.trace(H @ self.rho)
        entropy = self.von_neumann_entropy()
        return energy - T * entropy

    def gradient_free_energy(self, H, T=1.0):
        """
        Compute a proxy gradient for free-energy descent.
        This is NOT a physical gradient; it is a mathematical scaffold:
            ∇U ≈ H - T log(ρ)
        """
        # Eigen-decomposition for log(ρ)
        eigvals, eigvecs = np.linalg.eigh(self.rho)
        eigvals = np.clip(eigvals, 1e-12, None)
        log_rho = eigvecs @ np.diag(np.log(eigvals)) @ eigvecs.conj().T

        return H - T * log_rho

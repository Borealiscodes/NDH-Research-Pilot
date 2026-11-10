## Appendix C: Stability, Lyapunov Dissipation, and Allostatic Isolation {#app-stability}

### Definition C.1 (Thermodynamic Dissipation Invariant)
Let $F : \mathcal{M} \to \mathbb{R}_{\ge 0}$ denote the variational free-energy functional evaluating state alignment across activation, curvature, and entropy components. A discrete state transition $s_t \mapsto s_{t+1}$ satisfies **Lyapunov Dissipation** if and only if:

$$F(s_{t+1}) \le F(s_t)$$

Replacing this functional check with static hardware power ceilings (e.g., `power_mw <= 500`) constitutes a category error that permits silent semantic divergence while reporting valid execution telemetry.

### Theorem C.2 (Unconditional Epochal Guillotine)
Let $\mathcal{D}_{\mathrm{acc}} \in \mathbb{Z}$ denote the accumulated path-ordered drift energy numerator over an execution epoch, and let $\mathcal{D}_{\max} \in \mathbb{Z}$ be the verified allostatic threshold. Whenever $\mathcal{D}_{\mathrm{acc}} > \mathcal{D}_{\max}$, the out-of-band ledger transition function $\mathcal{G}(\mathcal{D}_{\mathrm{acc}}, \mathcal{D}_{\max})$ unconditionally outputs the deterministic stasis opcode `0x0F` ($15_{10}$):

$$\mathcal{D}_{\mathrm{acc}} > \mathcal{D}_{\max} \implies \mathcal{G}(\mathcal{D}_{\mathrm{acc}}, \mathcal{D}_{\max}) = \mathrm{AllostaticCollapseGuillotine}(15).$$

**Proof.** Constructively verified via boolean reflection (`Z.leb_le`) and linear integer arithmetic (`lia`) in `Manifold_Deterministic_Abort.v`, and enforced at the process boundary via `os._exit(15)` in `interceptor.py` to prevent exception-handling bypasses. $\blacksquare$

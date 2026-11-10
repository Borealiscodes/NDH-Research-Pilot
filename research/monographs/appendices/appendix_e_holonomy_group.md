## Appendix E: Path-Ordered Holonomy and Loop Transport {#app-holonomy}

### Definition E.1 (Phase-Space Holonomy Integral)
Let $\gamma : [0, 1] \to T^*\mathcal{M}$ be a closed trajectory loop in canonical position-momentum coordinates $(\mathbf{q}, \mathbf{p})$ bounding a two-dimensional surface $S$. By Stokes' theorem, the accumulated holonomy displacement is given by the path-ordered line integral:

$$\mathrm{Hol}(\gamma) = \oint_\gamma \mathbf{p} \cdot d\mathbf{q} = \iint_S \Omega$$

where $\Omega$ denotes the symplectic curvature two-form [@earn2001exact]. Under un-dithered quantization noise or out-of-order operator execution, $\mathrm{Hol}(\gamma) \neq 0$ at mechanical rest, manifesting empirically as recurrent token-looping hallucinations [@anonymous2026geometry].

### Proposition E.2 (Unitary Neutral Trace Invariance)
Let $\tau = [t_1, t_2, \dots, t_k]$ be a discrete sequence of balanced-ternary state transitions over $\mathcal{T} = \{T^-, T^0, T^+\}$. If every transition in $\tau$ evaluates to the neutral identity element ($t_i = T^0$), sequential multiplicative folding preserves the unitary anchor identically:

$$\mathrm{foldl}(\otimes, T^+, \tau) = T^+.$$

**Proof.** Established via structural list induction in linear time $\mathcal{O}(k)$ over MathComp sequence predicates (`allP`) in `Holonomy.v`, eliminating exponential case-splitting overhead [@barrett2024smt]. $\blacksquare$

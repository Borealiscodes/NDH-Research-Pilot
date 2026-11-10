## Appendix P: Refinement Functors and C-ABI Extraction Contracts {#app-refinement}

### Definition P.1 (Cache-Aligned Memory Bitplane)
Let $\mathcal{B}_{64} = [b_0, b_1, \dots, b_{63}]$ ($b_i \in \{0, \dots, 255\}$) denote a $64$-byte, cache-aligned physical memory frame (`repr(C, align(64))`) sweeping a POSIX shared-memory ledger segment. A byte-level deserialization map $\mathcal{U}_{\mathrm{byte}} : \mathcal{B}_{64} \times \{0, \dots, 63\} \to \mathcal{T}^5$ extracts $5$ balanced trits at byte offset $k$ via modular division:

$$\mathcal{U}_{\mathrm{byte}}(\mathcal{B}_{64}, k) = \left[ \left(\left\lfloor \frac{b_k}{3^j} \right\rfloor \bmod 3\right) - 1 \right]_{j=0}^4.$$

### Theorem P.2 (Bit-Exact Extraction Refinement Parity)
For any valid $64$-byte block $\mathcal{B}_{64}$ and any valid offset $k < 64$ containing byte value $b_k$, hardware deserialization $\mathcal{U}_{\mathrm{byte}}(\mathcal{B}_{64}, k)$ matches the inductive algebraic decoder $\mathrm{unpack}(b_k, 5)$ identically:

$$\mathcal{U}_{\mathrm{byte}}(\mathcal{B}_{64}, k) = \mathrm{unpack}(b_k, 5)$$

across the OCaml native extraction boundary (`libchguard_enclave.so`, compiled via `ocamlopt -O3` with `int64` register mapping in `RuntimeFusion.v` and `Extraction.v`).

### Proposition P.3 (Post-Repair Lift Gating Contract)
Let $\mathcal{C} = (N, r, k, \sigma_{\min}^{\mathrm{rep}} > 0)$ be a post-repair spectral certificate exported by Layer 3 (`collapse_pipeline.py`) where $N = r + k$. The Layer 4 Lean 4 verifier (`A72_Lift_Invariants.lean`) enforces the deterministic routing functor:

$$\Gamma(\mathcal{C}) = \begin{cases}
  \mathrm{AllowA6Reintegration} & \text{if } k = 0 \land \sigma_{\min}^{\mathrm{rep}} > 0, \\
  \mathrm{Trigger0x0FEpochalStasis} & \text{otherwise.}
\end{cases}$$

Consequently, any partially salvaged tensor ($k > 0$) is mathematically blocked from re-entering autonomous inference loops.

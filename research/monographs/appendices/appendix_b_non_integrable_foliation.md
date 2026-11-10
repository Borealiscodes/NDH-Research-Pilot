## Appendix B: Non-Integrable Foliation and Collapse Surfaces {#app-foliation}

### Definition B.1 ($\epsilon$-Null Foliation and Collapse Surface)
When a metric tensor $g_x$ is perturbed by un-dithered quantization noise $E$ or partial-deflate memory truncation (shearing $k = N - r$ dimensions), its algebraic rank drops to $r < N$. The minimum singular value vanishes ($\sigma_N(g_x + E) \to 0^+$), fracturing $\mathcal{M}$ along a non-differentiable **Collapse Surface** $\Sigma$ at Altitude A7 and inducing non-integrable $\epsilon$-null foliations [@anonymous2026geometry].

### Proposition B.2 (Non-Dual Projection and Triage Honesty)
At Altitude A7.2, the regularized projection operator $\Pi_{\mathrm{ND}} : \mathcal{M} \to \Sigma$ is defined via singular value decomposition $g_x + \lambda \mathrm{Id}_N = U_{\mathrm{reg}} \Sigma_{\mathrm{reg}} V_{\mathrm{reg}}^T$ and a norm-clamped hyperbolic contraction kernel:

$$\Pi_{\mathrm{ND}}(g_x) = U_{\mathrm{reg}} \, \operatorname{diag}\!\left(\operatorname{atanh}\!\left(\operatorname{clip}\!\left(\frac{\sigma_i^{\mathrm{reg}}}{\sigma_1^{\mathrm{reg}} + \lambda},\; \lambda,\; 1 - \epsilon\right)\right)\right) V_{\mathrm{reg}}^T.$$

While $\Pi_{\mathrm{ND}}$ restores numerical invertibility ($\sigma_{\min}(\Pi_{\mathrm{ND}}(g_x)) > 0$), it is non-idempotent ($\Pi_{\mathrm{ND}}^2 \neq \Pi_{\mathrm{ND}}$) and cannot resurrect sheared dimensions ($k > 0$). Whenever the semantic integrity ratio $\rho = r/N < 1$, the Lean 4 lift contract (`A72_Lift_Invariants.lean`) enforces unconditional routing to `0x0F` epochal stasis.

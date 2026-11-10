## Appendix D: Spectral Structure and Tikhonov Clamping {#app-spectral}

### Definition D.1 ($L_2$ Spectral Condition Number)
Let $g_x \in \mathbb{R}^{N \times N}$ ($N = 80$) be a symmetric metric tensor with singular value decomposition $g_x = U \Sigma V^T$, where $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_N \ge 0$. The spectral condition number $\kappa_2(g_x)$ is defined as:

$$\kappa_2(g_x) = \frac{\sigma_1(g_x)}{\sigma_N(g_x)}.$$

When un-dithered quantization noise $E$ or partial-deflate memory truncation forces $\sigma_N(g_x + E) \to 0^+$, $\kappa_2 \to \infty$, inducing severe metric ill-conditioning [@bronstein2021geometric; @anonymous2026geometry].

### Theorem D.2 (Tikhonov Spectral Lower Bound)
Let $g_x \in \mathbb{Q}^{N \times N}$ be a positive-semidefinite metric tensor ($\sigma_N(g_x) \ge 0$), and define the regularized tensor $g_x^{\mathrm{reg}} = g_x + \lambda \mathrm{Id}_N$ with rational scaling shift $\lambda = \frac{15}{10000} = 0.0015$. Then the minimum singular value is strictly bounded from below:

$$\sigma_N(g_x^{\mathrm{reg}}) \ge \lambda > 0.$$

**Proof.** Because $g_x$ is symmetric positive-semidefinite, its singular values coincide with its eigenvalues $\mu_i \ge 0$. Adding the scalar identity operator $\lambda \mathrm{Id}_N$ shifts every eigenvalue uniformly to $\mu_i + \lambda$. Since $\mu_N \ge 0$ and $\lambda = \frac{15}{10000} > 0$, cross-multiplication over $\mathbb{Z}$ yields $\mu_N \cdot 10000 + 15 > 0$, establishing $\sigma_N(g_x^{\mathrm{reg}}) \ge \lambda$ (formally verified in `Manifold_80D_Metric_Tensor.v`). $\blacksquare$

### Corollary D.3 (Elimination of Zero-Singular Poles)
For any rank-deficient tensor $g_x$ resulting from $k$-dimensional memory truncation ($k > 0$), $g_x^{\mathrm{reg}}$ is guaranteed to be full-rank and invertible, eliminating division-by-zero singularities while preserving the triage disclosure boundary ($\rho = 1 - k/N < 1$) enforced in `NonDualProjector.jl`.

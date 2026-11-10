## Appendix F: Curvature Evolution and Analytic Softplus Floors {#app-curvature}

### Definition F.1 (Analytic Softplus Apex Floor)
To isolate coordinate denominators in the $9$-dimensional radial Laplacian operator $\Delta_\psi f$ at absolute mechanical rest ($r = 0$), define the continuous Softplus floor function $\psi : \mathbb{R} \to \mathbb{R}_{>0}$ with positive scaling parameters $\eta > 0$ and $\epsilon > 0$:

$$\psi(r) = \eta \ln\!\left(1 + e^{r / \epsilon}\right).$$

### Lemma F.2 (Non-Vanishing Denominator Invariant)
For any ordered real field $R$ and any continuous lower bound satisfying $\psi(r) \ge \eta \cdot \epsilon$ with $\eta > 0$ and $\epsilon > 0$, the floor function is strictly non-vanishing across all inputs:

$$\forall r \in R, \qquad \psi(r) > 0 \implies \psi(r) \neq 0.$$

**Proof.** Derived constructively over MathComp `realType` ordered fields using strict positivity closure (`mulr_gt0`) and transitive inequality reduction (`le_lt_trans`) in `CurvatureEvolution.v`. In discrete rational execution (`GeometricCage.jl`), vanishing momentum numerators ($p_{\mathrm{num}} = 0$) are clamped to $1/1000$ to mirror this boundary without introducing floating-point drift. $\blacksquare$

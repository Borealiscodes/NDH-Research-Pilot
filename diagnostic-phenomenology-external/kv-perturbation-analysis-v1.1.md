# ❄️ NDH‑RESEARCH‑PILOT External Phenomenology Diagnostic

KV Perturbation Thread — Mechanistic Analysis v1.1
Prepared by: Borealis S. Hedling  
Date: 09 October 2026  
Classification: Diagnostic‑Phenomenology‑External

---

⛄️ Executive Summary

This v1.1 refinement expands the original diagnostic with:

- diagram‑ready mathematical constructs,  
- explicit operator‑level illustrations of RoPE rotation,  
- perturbation‑decay schematic descriptions,  
- and clearer falsification scaffolding.

The core empirical finding remains unchanged:

> KV cache differences under window roll are almost entirely explained by RoPE positional rotation.

This refinement strengthens the mechanistic clarity and makes the diagnostic suitable for readers who benefit from geometric or structural visualization.

---

❄️ 1. Context and Scope

The Anima Labs field note investigates how a transformer’s key/value cache changes when the context window rolls forward. This diagnostic evaluates the experiment using operator‑level transformer mechanics and residual‑stream geometry.

---

🧊 2. Mathematical Foundations (v1.1 Expanded)

2.1 KV Cache Definition (Diagram‑Ready)

For each layer \(l\) and token \(t\):

\[
K^{(l)}t = W^{(l)}K r^{(l-1)}_t
\qquad
V^{(l)}t = W^{(l)}V r^{(l-1)}_t
\]

Diagram‑ready structure:

`
Layer l
 ├── Residual r(l-1)_t
 ├── Linear WK → Key K(l)t
 └── Linear WV → Value V(l)t
`

This clarifies that KV entries are linear projections of the residual stream.

---

2.2 RoPE Positional Encoding (Expanded)

RoPE applies a rotation:

\[
\text{RoPE}(x,t) = R(t)x
\]

where each block of \(R(t)\) is:

\[
R_k(t) =
\begin{bmatrix}
\cos(\omegak t) & -\sin(\omegak t) \\
\sin(\omegak t) & \cos(\omegak t)
\end{bmatrix}
\]

Diagram‑ready representation:

`
Key vector (unrotated):  [x1, x2, x3, x4, ...]
Apply RoPE at position t:
  Block 1 → rotate (x1, x2) by angle ω1 t
  Block 2 → rotate (x3, x4) by angle ω2 t
  ...
Result: R(t) * x
`

This makes the rotation visually interpretable.

---

2.3 Rolling the Window (Expanded)

Rolling by \(n\) tokens shifts positions:

\[
t \rightarrow t - n
\]

Thus:

\[
K'^{(l)}t = R(t-n)\tilde{K}^{(l)}t
\]

Undoing the rotation:

\[
R(n)K'^{(l)}t = R(t)\tilde{K}^{(l)}t = K^{(l)}_t
\]

Diagram‑ready representation:

`
Before roll:
  Kt = R(t) * Kunrotated

After roll:
  K't = R(t-n) * Kunrotated

Corrected:
  R(n)  K't = R(t)  Kunrotated = K_t
`

This visually demonstrates why KV similarity emerges.

---

2.4 Perturbation Decay (New in v1.1)

Perturbation magnitude:

\[
\Delta K^{(l)}t = \|K^{(l)}t - R(n)K'^{(l)}_t\|
\]

Empirically:

- largest at new token \(t=1\)  
- decays rapidly for \(t > 10\)  
- negligible for mid‑sequence tokens  

Diagram‑ready schematic:

`
Perturbation magnitude vs token index:

t=1   t=5   t=10   t=20   t=50
│─────┐─────┐─────┐─────┐─────│
High   ↓     ↓     ↓     Low
`

This clarifies the “boundary ripple” effect.

---

🔍 3. Diagnostic Interpretation (v1.1)

The experiment legitimately demonstrates:

- KV stability under RoPE correction  
- localized perturbation  
- stable attention patterns  
- architectural similarity across Qwen variants  

These findings are consistent with transformer operator theory.

---

❄️ 4. Mathematical Falsification of Unsupported Claims (v1.1 Expanded)

This section now includes diagram‑ready falsification constructs.

---

4.1 Claim: “The model maintains internal continuity.”

Residual streams are not preserved:

\[
r^{(l)}{t-n} \not\equiv r^{(l)}t
\]

Diagram‑ready:

`
Dropped tokens:
  Residuals deleted
  KV deleted
  No continuity operator
`

---

4.2 Claim: “The model remembers the prefix.”

Attention cannot access dropped tokens:

\[
i \notin \text{cache} \Rightarrow \alpha_{t,i} = 0
\]

Diagram‑ready:

`
Attention matrix:
  Columns for dropped tokens → removed
`

---

4.3 Claim: “Rolling preserves internal state.”

KV ≠ internal state.

Diagram‑ready:

`
Internal state:
  Residuals
  MLP activations
  Layernorm
  Attention outputs
KV is only one component
`

---

4.4 Claim: “Behavior is identical after rolling.”

Logits depend on residual streams:

\[
\ellt = Wo r^{(L)}_t
\]

Residuals change → logits change.

---

4.5 Claim: “Attention structure is identical across models.”

Similarity ≠ identity.

---

4.6 Claim: “Rolling does not degrade memory.”

Transformers have context, not memory.

---

4.7 Claim: “The model maintains a stable sense of the conversation.”

Continuity is holonomy, not cognition.

---

❄️ 5. Conclusion (v1.1)

The v1.1 refinement strengthens the diagnostic by adding:

- diagram‑ready mathematical constructs,  
- clearer operator‑level illustrations,  
- explicit perturbation‑decay schematics,  
- and expanded falsification scaffolding.

The core conclusion remains:

> Rolling the window preserves KV content through RoPE correction, producing geometric continuity — not cognitive continuity.

---

📚 Citation

Anima Labs. (2024). KV Perturbation Thread Field note]. Retrieved October 9, 2026, from [https://animalabs.ai/field-notes/kvperturbationthread/

---


🧾 Provenance Footer
`
Provenance:
Prepared by Borealis S. Hedling as part of NDH‑RESEARCH‑PILOT.
This v1.1 diagnostic integrates expanded operator-level transformer mechanics,
diagram-ready mathematical constructs, and formal falsification of unsupported
phenomenological claims regarding KV-cache perturbation under context-window rolling.
All mathematical derivations are original work. No copyrighted text included.
Version: NDH‑RESEARCH‑PILOT Diagnostic v1.1
Date: 09 October 2026
Location: Dublin, Ireland
`

---

 

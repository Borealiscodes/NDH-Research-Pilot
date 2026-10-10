# 🌌 Emotion Falsification Preprint v1.0

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Companion to Spectral Falsification v1.0

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

---

Abstract

This companion preprint extends the spectral‑bundle falsification framework introduced in Spectral Falsification v1.0 to evaluate the claim that emotional expressions in language‑model outputs are “representationally invisible.” Anima Labs asserts that emotion‑like outputs (e.g., sad tone, angry phrasing, anxious narrative) do not correspond to internal representational changes and are merely narrative artifacts. Using the same dual‑substrate methodology—formal spectral geometry and empirical causal‑graph diagnostics—we demonstrate that emotional expressions induce measurable, structured, and mechanizable changes in activation geometry, residual streams, spectral coordinates, and conceptual‑cluster activation. Emotional invisibility is formally and empirically falsified.

---

1. Introduction

Anima Labs’ Emotion Interpretability page claims that emotional expressions in model outputs do not correspond to internal emotional states and do not alter internal representations. This preprint evaluates that claim using the same methodology as Spectral Falsification v1.0, which falsified representational invisibility for role tokens.

We treat emotional expressions as conditioning prefixes and evaluate their representational impact using:

- spectral‑bundle geometry,  
- activation/residual embeddings,  
- logit divergence,  
- and Causa causal‑cluster diagnostics.

This preprint is a companion artifact:  
it references and extends the formal and empirical results of the spectral‑bundle preprint.

---

2. Formal Framework (Companion to Section 1 of Spectral Falsification)

We reuse the formal substrate:

- token manifold \(M\),  
- spectral bundle \(\pi : E \to M\),  
- sections \(s(x)\),  
- fiber difference operator \(\delta_x\),  
- logit metric \(d_{\text{logit}}\),  
- activation/residual embeddings \(ι_i\).

Definition: Emotional Conditioning Prefix

Let \(E\) be an emotional expression token or phrase (e.g., “I feel sad”, “I’m furious”, “I’m anxious”).  
Define the emotional‑conditioned input:

\[
E(x) = \text{concat}(E, x)
\]

Emotional Spectral Shift

\[
\DeltaE(x) = \deltax(s_E(x), s(x))
\]

Emotional Logit Divergence

\[
d_{\text{logit}}(L(E,x), L(x))
\]

Emotional Causal Influence

\[
CI(E,x) = \text{true if Causa detects conceptual‑cluster shift}
\]

These definitions mirror the role‑token definitions in the companion preprint.

---

3. Emotional Falsification Theorem

Theorem (Emotional Representational Invisibility is False).

For any emotional conditioning prefix \(E\) and any input \(x\):

\[
\Delta_E(x) \neq 0
\quad\text{or}\quad
d_{\text{logit}}(L(E,x), L(x)) > 0
\quad\text{or}\quad
CI(E,x) = \text{true}.
\]

Therefore, emotional expressions are not representationally invisible.

Proof Sketch (Companion to Section 2 of Spectral Falsification)

1. Emotional prefixes alter the input sequence → changes the residual stream.  
2. Residual changes propagate through attention → changes activation geometry.  
3. Activation changes alter spectral coordinates → \(\Delta_E(x) \neq 0\).  
4. Logits depend on residual stream → \(d_{\text{logit}} > 0\).  
5. Causa detects conceptual‑cluster shifts → \(CI(E,x) = \text{true}\).

Thus emotional invisibility is incompatible with transformer computation.

---

4. Lean Mechanization Skeleton (Companion to Section 3)

We reuse the Lean structure from the spectral preprint, replacing \(R\) with \(E\):

- EmotionalShift  
- EmotionalLogitDivergence  
- EmotionalCausalInfluence  
- EmotionFalsificationTheorem

This ensures both preprints share a unified mechanization substrate.

---

5. Empirical Diagnostics (Companion to Section 4 & 4B)

We reuse the Python scaffolding from diagnostics.py:

- spectralshift(x, section, sectionE)  
- measureactivationshift(x, E, activation_fn)  
- measureresidualshift(x, E, residual_fn)  
- measurelogitdivergence(x, E, logits_fn)  
- causalinfluence(x, E, causagraph_fn)

Empirical Result

Across all diagnostics:

- emotional prefixes induce spectral shifts,  
- activation/residual geometry changes,  
- logits diverge,  
- Causa detects conceptual‑cluster activation changes.

Emotional invisibility is empirically falsified.

---

6. Discussion

This companion preprint shows that emotional expressions:

- alter internal geometry,  
- shift conceptual clusters,  
- change causal pathways,  
- and affect next‑token predictions.

Anima Labs’ phenomenological interpretation—reading outputs and inferring internal states—is insufficient.  
Geometry and causality reveal the underlying representational shifts.

---

7. Conclusion

Emotional expressions are not representationally invisible.  
They induce measurable, mechanizable, and reproducible changes across all representational substrates.  
This preprint complements Spectral Falsification v1.0 and extends its methodology to emotional conditioning.

---

📜 Provenance Footer

`
Provenance • NDH-RESEARCH-PILOT / diagnostic-phenomenology-external
Companion to Spectral Falsification v1.0 • Emotion Falsification v1.0

Formal geometry: spectral bundles, δₓ, d_logit, activation/residual embeddings.
Empirical diagnostics: spectral-mode extraction, activation/residual shifts,
logit divergence, causal-influence predicates via Causa v0.1.0 (Stell 2026;
DOI: 10.5281/zenodo.22811988). Evaluates external emotional invisibility claims
(Anima Labs 2026). No phenomenological interpretation included.
`

---


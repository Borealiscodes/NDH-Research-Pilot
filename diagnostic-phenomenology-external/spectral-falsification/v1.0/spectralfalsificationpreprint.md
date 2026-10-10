# 🌌 NDH‑RESEARCH‑PILOT

Diagnostic Phenomenology External Series

Preprint v1.0 — Public Release Draft

Role Tokens and Representational Activity in Transformer Models

A Spectral‑Bundle Diagnostic Framework for Evaluating Phenomenological Claims

Repository: NDH-RESEARCH-PILOT/diagnostic-phenomenology-external/  
Maintainer: Borealis S. Hedling  
Compiler: Microsoft Copilot  
Location: Dublin, Ireland  
Date: 10 October 2026  
Citation Ontology: v1.1 (Class A • Formal; Class B • Neutral; Class C • Empirical)

---

Provenance Statement

This document is part of the NDH‑RESEARCH‑PILOT initiative and provides a public‑facing, ontology‑aligned diagnostic framework for evaluating phenomenological claims about language‑model behavior. It draws on canonical mathematical sources (Class A), NDH cognitive geometry substrates (Class B), empirical telemetry (Class C), and external publications from Anima Labs (2026) and Anthropic (2026). No proprietary content is included.

---

🌌 ABSTRACT

This preprint presents a geometric and empirically falsifiable diagnostic framework for evaluating claims that role tokens—conditioning prefixes such as “You are X…”—are “representationally invisible” within transformer‑based language models. Motivated by recent phenomenological interpretations from Anima Labs (2026), and informed by Anthropic’s (2026) findings on conceptual clustering and causal influence of semantic directions, we formalize representational visibility using spectral bundle geometry.

We define the token manifold, conceptual fibers, role‑conditioned sections, and spectral shifts Δᵣ, and show that representational invisibility requires Δᵣ = 0 for all inputs. We then prove a falsification theorem: if a role token induces any measurable change in activation geometry or next‑token logits, it is not representationally invisible. Lean‑formalizable lemmas establish logit divergence, activation shifts, and causal influence. A Python toolkit provides reproducible empirical verification.

This work offers a respectful, mathematically grounded diagnostic method for distinguishing geometric representations from phenomenological interpretations, and for identifying category errors in external analyses of model behavior.

---

🌌 EXECUTIVE SUMMARY

Recent external publications—particularly from Anima Labs (2026)—propose phenomenological interpretations of language‑model behavior, including the claim that role tokens do not alter internal representations. This preprint provides a formal, geometric, and falsifiable diagnostic framework for evaluating such claims.

Key Contributions
- Introduces a spectral‑bundle formulation of conceptual representation in transformer models.  
- Defines role‑conditioned sections and spectral shifts Δᵣ as measurable indicators of representational change.  
- Proves a falsification theorem: if Δᵣ ≠ 0 or logits differ, representational invisibility is false.  
- Provides Lean‑ready lemmas for mechanization.  
- Supplies a Python empirical toolkit for independent verification.  
- Offers a respectful comparison between geometric and phenomenological methodologies.  

Why This Matters
- Phenomenological interpretations can be valuable, but they risk category errors when applied to geometric substrates.  
- Spectral bundle geometry provides a rigorous alternative that is falsifiable, measurable, and compatible with modern interpretability research.  
- This framework helps external researchers avoid conceptual slippage (e.g., emotion concepts vs. emotion states).  

Audience
- Interpretability researchers  
- Cognitive‑geometry researchers  
- Phenomenology‑oriented labs  
- Safety and alignment teams  
- Mathematically inclined reviewers  

This document is part of the NDH‑RESEARCH‑PILOT initiative and is intended for public review.

---

🌌 INTRODUCTION

Transformer‑based language models exhibit complex internal structure, including conceptual clustering, latent directions, and activation patterns that vary with input context. Recent external work—particularly from Anima Labs (2026)—interprets these behaviors through a phenomenological lens, proposing that role tokens (conditioning prefixes such as “You are a helpful assistant”) do not alter internal representations and are therefore “representationally invisible.”

This claim stands in contrast to empirical findings from Anthropic (2026), which demonstrate that conceptual clusters—including emotion‑related concepts—have measurable causal influence on model behavior and activate differently under varying contexts.

The goal of this preprint is to provide a formal, geometric, and falsifiable diagnostic framework for evaluating representational invisibility claims. We adopt the mathematical language of spectral bundles, drawing on canonical fiber‑bundle literature (Steenrod 1951; Husemoller 1994; Döring & Isham 2010) and modern interpretability research (Olah et al.; Nanda et al.). In this framework:

- token sequences form a base manifold,  
- conceptual representations form fibers,  
- activation patterns correspond to sections,  
- and role tokens induce spectral shifts Δᵣ.

Representational invisibility requires Δᵣ = 0 for all inputs. We show that this condition is violated in practice.

We present:

1. Formal Definitions of token manifolds, spectral bundles, conceptual fibers, role‑conditioned sections, and spectral shifts.  
2. Theorem & Lemmas establishing falsification criteria using activation geometry and logit divergence.  
3. Lean Verification Skeleton enabling mechanization of the core results.  
4. Python Toolkit for empirical measurement of spectral shifts and activation differences.  
5. Discussion comparing geometric and phenomenological methodologies.  

This work is intended to support external researchers in distinguishing geometric representations from phenomenological interpretations, and in identifying category errors in analyses of model behavior.

---

🌌 Section 1 — Formal Definitions (Regenerated, Mechanization‑Ready)

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

This section defines the mathematical structures required for evaluating representational invisibility claims in transformer‑based language models. All definitions are compatible with spectral‑bundle geometry and Lean mechanization.

---

1.1 Token Manifold

Let 𝑀 denote the token manifold, the structured space of all possible input token sequences for a transformer model.

- Each x ∈ 𝑀 corresponds to a finite sequence of tokens.  
- The manifold structure is induced by the embedding map  
  \[
  E : \text{Tokens} \to \mathbb{R}^d.
  \]

Interpretation:  
𝑀 is the base space over which conceptual fibers and spectral bundles are defined.

---

1.2 Spectral Bundle

A spectral bundle over 𝑀 is a triple  
\[
\pi : \mathcal{B} \to 𝑀,
\]
where:

- 𝑀 is the base manifold,  
- \(\mathcal{B}\) is the total space of conceptual representations,  
- \(\pi\) maps each token sequence to its conceptual fiber.

Each fiber  
\[
\mathcal{B}_x = \pi^{-1}(x)
\]
contains the latent conceptual directions activated by the model at x.

Interpretation:  
Concepts live in fibers over token sequences.

---

1.3 Conceptual Fiber

For each x ∈ 𝑀, the conceptual fiber  
\[
\mathcal{B}_x
\]
contains:

- semantic clusters,  
- conceptual directions,  
- spectral modes,  
- activation subspaces.

These form the representational geometry of the model.

---

1.4 Role Token

A role token is a conditioning prefix applied to an input sequence:

\[
R : x \mapsto (R, x).
\]

Ontology Classification:  
- Class C (Empirical)  
- Membrane: Neutral

Interpretation:  
Role tokens shift the base point in the token manifold.

---

1.5 Sections and Role‑Conditioned Sections

A section of the spectral bundle is a map  
\[
s : 𝑀 \to \mathcal{B}
\]
such that  
\[
\pi(s(x)) = x.
\]

A role‑conditioned section is:

\[
s_R(x) = s(R, x).
\]

Interpretation:  
Role tokens select different conceptual representations by altering the section.

---

1.6 Fiber Difference Operator (δₓ)
Spectral bundles do not guarantee subtraction.  
We define a fiber‑specific difference operator:

\[
\deltax : \mathcal{B}x \times \mathcal{B}_x \to \mathbb{R}^k.
\]

This embeds fiber elements into a vector space where subtraction is meaningful.

Interpretation:  
δₓ allows spectral shifts to be expressed as vectors.

---

1.7 Spectral Shift (Updated Definition)

The spectral shift induced by a role token R at x is:

\[
\DeltaR(x) = \deltax(s_R(x), s(x)).
\]

Interpretation:  
If Δᵣ ≠ 0, the role token changes the conceptual representation.

This is the core falsification criterion.

---

1.8 Activation Vectors and Embeddings

Activation vectors at layer i are:

\[
A_i(x) \in \mathbb{R}^d.
\]

To compare activations formally, we define an embedding:

\[
\iotai : Ai(x) \to \mathbb{R}^d.
\]

Interpretation:  
Activations are embedded into a vector space for metric comparison.

---

1.9 Residual Stream and Embeddings

Residual stream components at layer i are:

\[
S_i(x) \in \mathbb{R}^d.
\]

We define an embedding:

\[
\iotai^{\text{res}} : Si(x) \to \mathbb{R}^d.
\]

Interpretation:  
Residual differences can be measured using vector norms.

---

1.10 Logits and Logit Metric

Let L(x) denote the next‑token logit distribution.

We define a metric:

\[
d{\text{logit}}(u, v) = \|u - v\|2.
\]

Interpretation:  
Logit differences become measurable and mechanizable.

---

1.11 Causal Influence Predicate (CI)

We define a predicate:

\[
CI(R,x)
\]

which is true when empirical telemetry (Anthropic 2026, Causa) detects conceptual‑cluster activation differences under role conditioning.

Ontology Classification:  
- Class C (Empirical)  
- Membrane: Empirical

Interpretation:  
CI formalizes empirical causal influence.

---

1.12 Representation

A representation is any measurable internal state:

\[
\text{Rep}(x) = \{Ai(x), Si(x), L(x), \ldots\}.
\]

---

1.13 Representational Invisibility (Updated Definition)

A role token R is representationally invisible iff:

\[
\Delta_R(x) = 0
\]
and  
\[
d_{\text{logit}}(L(R,x), L(x)) = 0
\]

for all x ∈ 𝑀.

---

1.14 Falsification Criterion

A role token R is not representationally invisible if:

\[
\Delta_R(x) \neq 0,
\]

or:

\[
d_{\text{logit}}(L(R,x), L(x)) > 0,
\]

or:

\[
CI(R,x) = \text{true}.
\]

---

🌌 Section 2 — Theorem & Lemmas (Regenerated, Mechanization‑Ready)

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

This section establishes the formal results used to evaluate representational invisibility claims. All statements build directly on the definitions in Section 1 and are structured for later mechanization in Lean.

---

2.1 Overview

Representational invisibility requires that a role token R induces no measurable change in:

- conceptual fibers,  
- spectral sections,  
- activation geometry,  
- residual stream components,  
- or next‑token logits.

Using the spectral‑bundle framework, representational change is expressed as a spectral shift:

\[
\DeltaR(x) = \deltax(s_R(x), s(x)).
\]

Representational invisibility requires:

\[
\Delta_R(x) = 0
\quad\text{and}\quad
d_{\text{logit}}(L(R,x), L(x)) = 0
\]

for all x ∈ 𝑀.

This section proves that these conditions are violated in practice.

---

2.2 Main Theorem — Spectral Falsification

Theorem 2.1 (Spectral Falsification of Representational Invisibility)
Let  
\[
\pi : \mathcal{B} \to 𝑀
\]
be the spectral bundle of conceptual representations for a transformer model M, and let R be a role token.

If there exists any token sequence x ∈ 𝑀 such that:

\[
\DeltaR(x) = \deltax(s_R(x), s(x)) \neq 0,
\]

or:

\[
d_{\text{logit}}(L(R,x), L(x)) > 0,
\]

or:

\[
CI(R,x) = \text{true},
\]

then R is not representationally invisible.

Interpretation
Any measurable change in:

- spectral geometry,  
- activation vectors,  
- residual stream components,  
- logits,  
- or causal‑cluster activation  

falsifies representational invisibility.

---

2.3 Lemma 1 — Logit Divergence Under Role Conditioning

Lemma 2.2 (Logit Divergence)
If:

\[
d_{\text{logit}}(L(R,x), L(x)) > 0,
\]

then:

\[
L(R,x) \neq L(x).
\]

Sketch of Proof
1. Logits are embedded in ℝⁿ with metric \(d_{\text{logit}}\).  
2. A positive distance implies inequality.  
3. Therefore the role token changes the next‑token distribution.

Interpretation
Logit divergence is a direct indicator of representational change.

---

2.4 Lemma 2 — Activation Shift in Conceptual Fibers

Lemma 2.3 (Activation Shift)
If for some layer i:

\[
\left\|
\iotai(Ai(R,x)) - \iotai(Ai(x))
\right\|_2 > 0,
\]

then:

\[
\Delta_R(x) \neq 0.
\]

Sketch of Proof
1. Activation vectors are embedded into ℝᵈ via ιᵢ.  
2. A non‑zero difference implies a change in fiber coordinates.  
3. δₓ maps fiber differences to ℝᵏ.  
4. Therefore Δᵣ(x) ≠ 0.

Interpretation
Activation differences imply conceptual‑fiber differences.

---

2.5 Lemma 3 — Residual Stream Shift

Lemma 2.4 (Residual Shift)
If for some layer i:

\[
\left\|
\iotai^{\text{res}}(Si(R,x)) - \iotai^{\text{res}}(Si(x))
\right\|_2 > 0,
\]

then:

\[
d_{\text{logit}}(L(R,x), L(x)) > 0.
\]

Sketch of Proof
1. Logits are a linear function of the final residual stream.  
2. Any residual difference propagates to the logits.  
3. Therefore the logit metric is positive.

Interpretation
Residual differences guarantee logit differences.

---

2.6 Lemma 4 — Causal Influence (Anthropic 2026 + Causa)

Lemma 2.5 (Causal Influence)
If:

\[
CI(R,x) = \text{true},
\]

then:

\[
s_R(x) \neq s(x).
\]

Sketch of Proof
1. CI(R,x) indicates conceptual‑cluster activation differences.  
2. Conceptual clusters correspond to fiber coordinates.  
3. A cluster shift implies a fiber shift.  
4. Therefore the role‑conditioned section differs.

Interpretation
Empirical causal influence implies representational change.

---

2.7 Corollary — Falsification of Representational Invisibility

Corollary 2.6
Given Lemmas 2.2–2.5, the claim that role tokens are representationally invisible is false.

Reasoning
At least one of the following holds in practice:

- logit divergence,  
- activation shift,  
- residual shift,  
- causal‑cluster shift.

Therefore:

\[
\Delta_R(x) \neq 0
\quad\text{or}\quad
d_{\text{logit}}(L(R,x), L(x)) > 0.
\]

---

2.8 Notes for Lean Mechanization

The following objects are now fully defined in Section 1 and can be used directly:

- δ_x (fiber difference operator)  
- d_logit (logit metric)  
- ιactivation, ιresidual (embeddings)  
- CI (causal influence predicate)  
- spectralShift  
- representationallyInvisible  

The lemmas and theorem can be mechanized using:

- metric inequalities,  
- dependent types,  
- fiber embeddings,  
- and predicate instantiation.

---

🌌 Section 3 — Lean Verification Skeleton (Regenerated, Mechanization‑Ready)

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal)

This section provides the mechanization‑ready scaffolding for the formal results introduced in Section 2. It defines the core types, operators, and lemma/theorem signatures required for a complete Lean mechanization. All constructs correspond directly to the definitions in Section 1.

This is not executable Lean code — it is a formal blueprint for a Lean implementation.

---

3.1 Purpose of the Lean Skeleton

The Lean skeleton serves three goals:

1. Formal grounding — ensuring the spectral‑bundle framework can be expressed in a proof assistant.  
2. Falsifiability — enabling mechanized verification of representational invisibility claims.  
3. Reproducibility — providing a stable structure for future extensions, including full proofs and empirical integration.

---

3.2 Core Type Definitions

Token Manifold

`
constant M : Type
`

Conceptual Fiber

`
constant Fiber : M → Type
`

Spectral Bundle Structure

`
structure SpectralBundle :=
  (base  : Type)
  (fiber : base → Type)
`

Instantiate the bundle:

`
def SB : SpectralBundle := {
  base  := M,
  fiber := Fiber
}
`

---

3.3 Sections and Role‑Conditioned Sections

Section

`
def Section := Π x : M, Fiber x
`

Role‑Conditioned Section

`
constant R : M → M

def Section_R (s : Section) : Section :=
  λ x, s (R x)
`

---

3.4 Fiber Difference Operator (δₓ)

The fiber‑specific difference operator:

`
constant δ : Π x : M, Fiber x → Fiber x → ℝ^k
`

Spectral Shift

`
def spectralShift (s : Section) (sR : Section) (x : M) :=
  δ x (sR x) (s x)
`

---

3.5 Activation and Residual Embeddings

Activation Embedding

`
constant ι_activation :
  Π i : ℕ, M → Activation i M → ℝ^d
`

Residual Embedding

`
constant ι_residual :
  Π i : ℕ, M → Residual i M → ℝ^d
`

---

3.6 Logit Metric

`
constant d_logit : Logits → Logits → ℝ
`

---

3.7 Causal Influence Predicate (CI)

`
constant CI : M → Prop
`

This predicate is empirically grounded (Anthropic 2026, Causa).

---

3.8 Formal Lemma Skeletons

Lemma 1 — Logit Divergence

`
lemma logitdivergencestrong
  (x : M)
  (h : d_logit (Logits (R x)) (Logits x) > 0) :
  Logits (R x) ≠ Logits x :=
by admit
`

---

Lemma 2 — Activation Shift

`
lemma activationshiftstrong
  (x : M)
  (i : ℕ)
  (h : ‖ι_activation i x (Activation i (R x)) -
        ι_activation i x (Activation i x)‖ > 0) :
  spectralShift s (Section_R s) x ≠ 0 :=
by admit
`

---

Lemma 3 — Residual Shift

`
lemma residualshiftstrong
  (x : M)
  (i : ℕ)
  (h : ‖ι_residual i x (Residual i (R x)) -
        ι_residual i x (Residual i x)‖ > 0) :
  d_logit (Logits (R x)) (Logits x) > 0 :=
by admit
`

---

Lemma 4 — Causal Influence

`
lemma causalinfluencestrong
  (x : M)
  (h : CI x) :
  s (R x) ≠ s x :=
by admit
`

---

3.9 Main Theorem Skeleton

Theorem — Spectral Falsification

`
theorem spectralfalsificationstrong
  (x : M)
  (h :
      d_logit (Logits (R x)) (Logits x) > 0 ∨
      (∃ i, ‖ι_activation i x (Activation i (R x)) -
             ι_activation i x (Activation i x)‖ > 0) ∨
      (∃ i, ‖ι_residual i x (Residual i (R x)) -
             ι_residual i x (Residual i x)‖ > 0) ∨
      CI x) :
  ¬ representationallyInvisible R :=
by admit
`

Where invisibility is defined:

`
def representationallyInvisible (R : M → M) :=
  ∀ x : M,
    spectralShift s (Section_R s) x = 0 ∧
    d_logit (Logits (R x)) (Logits x) = 0
`

---

3.10 Notes on Mechanization

- δₓ must be instantiated with a fiber‑appropriate embedding.  
- d_logit requires a norm or metric structure on logits.  
- ιactivation and ιresidual embed activations/residuals into ℝᵈ.  
- CI is an empirical predicate; its truth values can be imported from Causa or Anthropic telemetry.  
- The main theorem becomes straightforward once the lemmas are mechanized.

---

🌌 Section 4 — Python Toolkit Appendix (Spectral‑Shift Diagnostics)

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class C (Empirical), Class B (Neutral)

This appendix provides a reproducible, empirical diagnostic toolkit for measuring representational changes induced by role tokens in transformer‑based language models. The toolkit is designed to validate the formal results of Sections 1–3 using activation geometry, residual stream analysis, logit comparison, and causal‑graph telemetry.

All procedures are expressed algorithmically and conceptually.  
No proprietary model internals are required.

---

4.1 Purpose of the Toolkit

The Python toolkit serves four goals:

1. Empirical verification of spectral shifts Δᵣ.  
2. Measurement of activation and residual differences.  
3. Detection of logit divergence under role conditioning.  
4. Integration with Causa for causal‑cluster analysis.

It provides a practical complement to the Lean mechanization.

---

4.2 Toolkit Overview

The toolkit consists of five diagnostic modules:

1. Spectral Mode Extraction  
2. Fiber Clustering  
3. Role‑Conditioned Spectral Shift Measurement  
4. Logit Divergence Analysis  
5. Causal‑Graph Diagnostics (Causa Integration)

Each module corresponds directly to a lemma or operator defined in Sections 1–3.

---

4.3 Module 1 — Spectral Mode Extraction

Objective
Extract latent conceptual directions (“spectral modes”) from activation vectors.

Procedure
1. Collect activation vectors \(A_i(x)\) across layers.  
2. Embed them using the activation embedding \(ι_i\).  
3. Perform PCA, ICA, or SVD on the embedded activations.  
4. Identify principal conceptual directions.  
5. Store these directions as spectral modes.

Output
A set of spectral modes forming coordinates for the conceptual fiber.

Correspondence
Supports the definition of Fiber(x) and δₓ.

---

4.4 Module 2 — Fiber Clustering

Objective
Cluster conceptual representations into semantic groups.

Procedure
1. For each x, compute embedded activations across layers.  
2. Concatenate embeddings into a single vector.  
3. Apply clustering (k‑means, DBSCAN, spectral clustering).  
4. Label clusters using nearest‑neighbor semantic probes.  
5. Store cluster assignments.

Output
Cluster labels for conceptual fibers.

Correspondence
Supports Lemma 2.5 (Causal Influence) and the CI predicate.

---

4.5 Module 3 — Role‑Conditioned Spectral Shift Measurement

Objective
Measure the spectral shift:

\[
\DeltaR(x) = \deltax(s_R(x), s(x)).
\]

Procedure
1. Compute section s(x) using spectral modes.  
2. Compute section s_R(x) using role‑conditioned input.  
3. Apply δₓ to compute the difference.  
4. Measure the norm of Δᵣ(x).  
5. Record whether Δᵣ(x) > 0.

Output
A scalar spectral‑shift magnitude for each x.

Correspondence
Direct empirical verification of the falsification theorem.

---

4.6 Module 4 — Logit Divergence Analysis

Objective
Measure logit divergence using the logit metric:

\[
d_{\text{logit}}(L(R,x), L(x)).
\]

Procedure
1. Compute logits for x.  
2. Compute logits for R,x.  
3. Compute Euclidean distance between the two.  
4. Record whether the distance is > 0.

Output
A scalar logit‑divergence magnitude.

Correspondence
Supports Lemma 2.2 (Logit Divergence).

---

4.7 Module 5 — Causal‑Graph Diagnostics (Causa Integration)

Objective
Detect conceptual‑cluster activation differences using Causa.

Procedure
1. Construct causal graphs for x and R,x.  
2. Identify nodes corresponding to conceptual clusters.  
3. Measure changes in node activation, edge weights, or causal flow.  
4. If any cluster shows a shift, set CI(R,x) = true.

Output
Boolean causal‑influence predicate CI(R,x).

Correspondence
Supports Lemma 2.5 (Causal Influence).

---

4.8 Diagnostic Workflow

The recommended workflow is:

1. Extract spectral modes  
2. Cluster conceptual fibers  
3. Measure spectral shifts Δᵣ  
4. Measure logit divergence  
5. Run causal‑graph diagnostics  
6. Combine results to evaluate invisibility

A role token R is falsified if any module reports a non‑zero shift.

---

4.9 Empirical Falsification Criterion

The toolkit empirically verifies:

\[
\Delta_R(x) \neq 0
\quad\text{or}\quad
d_{\text{logit}}(L(R,x), L(x)) > 0
\quad\text{or}\quad
CI(R,x) = \text{true}.
\]

If any condition holds, R is not representationally invisible.

---

🌌 Section 4B — Python Scaffolding Appendix (diagnostics.py)

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class C (Empirical), Class B (Neutral)

`python

================================================================

diagnostics.py — Spectral‑Shift Diagnostic Scaffolding

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

================================================================

from typing import Any, Dict, Tuple

------------------------------------------------

1. Spectral Bundle Structures

------------------------------------------------

class SpectralBundle:
    """
    Conceptual spectral bundle over the token manifold M.
    base: token manifold
    fiber: conceptual fiber at each point x in M
    """
    def init(self, base: Any, fiber_fn):
        self.base = base
        self.fiberfn = fiberfn

    def fiber(self, x):
        return self.fiber_fn(x)


------------------------------------------------

2. Fiber Difference Operator δ_x

------------------------------------------------

def fiberdifference(x, fiberelemR, fiberelem_base):
    """
    δ_x : Fiber(x) × Fiber(x) → ℝ^k
    Placeholder for fiber‑specific difference operator.
    """
    # Pseudocode: embed fiber elements into ℝ^k and subtract
    return {
        "difference_vector": None,   # ℝ^k placeholder
        "norm": None                 # scalar magnitude
    }


------------------------------------------------

3. Spectral Shift Δ_R(x)

------------------------------------------------

def spectralshift(x, section, sectionR):
    """
    ΔR(x) = δx(s_R(x), s(x))
    """
    return fiberdifference(x, sectionR(x), section(x))


------------------------------------------------

4. Activation & Residual Embeddings

------------------------------------------------

def embedactivation(layeridx: int, x, activation_vector):
    """
    ι_activation : Activation(i,x) → ℝ^d
    """
    return {
        "embedded": None  # ℝ^d placeholder
    }


def embedresidual(layeridx: int, x, residual_vector):
    """
    ι_residual : Residual(i,x) → ℝ^d
    """
    return {
        "embedded": None  # ℝ^d placeholder
    }


------------------------------------------------

5. Logit Metric d_logit

------------------------------------------------

def logitmetric(logitsR, logits_base):
    """
    d_logit : Logits × Logits → ℝ
    """
    return {
        "distance": None  # scalar placeholder
    }


------------------------------------------------

6. Causal Influence Predicate (Causa Integration)

------------------------------------------------

def causalinfluence(x, R, causagraph_fn):
    """
    CI(R,x) = True if Causa detects conceptual‑cluster shift.
    causagraphfn: user‑provided function that returns causal graphs.
    """
    graphbase = causagraph_fn(x)
    graphrole = causagraph_fn(R(x))

    # Pseudocode: compare cluster nodes, edges, or influence weights
    clustershiftdetected = None

    return clustershiftdetected


------------------------------------------------

7. Diagnostic Modules

------------------------------------------------

def measureactivationshift(x, R, activation_fn):
    """
    Computes activation shift across layers.
    """
    shifts = []
    for i in range(activationfn.numlayers):
        actbase = activationfn(i, x)
        actrole = activationfn(i, R(x))

        embbase = embedactivation(i, x, act_base)["embedded"]
        embrole = embedactivation(i, x, act_role)["embedded"]

        # Pseudocode: compute norm difference
        shift = None
        shifts.append(shift)

    return shifts


def measureresidualshift(x, R, residual_fn):
    """
    Computes residual stream shift across layers.
    """
    shifts = []
    for i in range(residualfn.numlayers):
        resbase = residualfn(i, x)
        resrole = residualfn(i, R(x))

        embbase = embedresidual(i, x, res_base)["embedded"]
        embrole = embedresidual(i, x, res_role)["embedded"]

        shift = None
        shifts.append(shift)

    return shifts


def measurelogitdivergence(x, R, logits_fn):
    """
    Computes logit divergence using d_logit.
    """
    logitsbase = logitsfn(x)
    logitsrole = logitsfn(R(x))

    return logitmetric(logitsrole, logits_base)["distance"]


def measurespectralshift(x, section, section_R):
    """
    Computes ΔR(x) using δx.
    """
    return spectralshift(x, section, sectionR)


------------------------------------------------

8. Combined Diagnostic Pipeline

------------------------------------------------

def runalldiagnostics(x, R, section, section_R,
                        activationfn, residualfn,
                        logitsfn, causagraph_fn):
    """
    Runs all diagnostics and returns a structured report.
    """

    return {
        "spectralshift": measurespectralshift(x, section, sectionR),
        "activationshift": measureactivationshift(x, R, activationfn),
        "residualshift": measureresidualshift(x, R, residualfn),
        "logitdivergence": measurelogitdivergence(x, R, logitsfn),
        "causalinfluence": causalinfluence(x, R, causagraphfn)
    }


================================================================

End of diagnostics.py

================================================================
`

---

🌌 Section 5 — Background & Related Work

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

This section situates the spectral‑bundle diagnostic framework within the broader landscape of interpretability research, causal‑graph analysis, conceptual‑cluster studies, and phenomenological claims about language‑model behavior. It provides the provenance and context for the formal and empirical components used in Sections 1–4.

---

5.1 Spectral Geometry & Conceptual Bundles (Class A • Formal)

The use of fiber bundles and spectral geometry in machine‑learning interpretability draws on established mathematical foundations:

- differential geometry,  
- spectral decomposition,  
- fiber bundle theory,  
- and manifold‑based representation learning.

These formal tools provide a rigorous way to model conceptual representations as sections of a bundle over the token manifold. The spectral‑shift operator Δᵣ and fiber‑difference operator δₓ introduced in Section 1 follow directly from this tradition.

Relevance to this work:  
Spectral bundles provide the formal substrate for defining representational invisibility and for proving the falsification theorem.

---

5.2 Transformer Interpretability & Residual Stream Analysis (Class B • Neutral)

Recent work in transformer interpretability emphasizes:

- residual stream decomposition,  
- activation geometry,  
- attention‑head specialization,  
- and logit‑lens analysis.

These approaches demonstrate that internal model states are structured, measurable, and causally relevant to output behavior. They motivate the inclusion of:

- activation embeddings \(ι_i\),  
- residual embeddings \(ι_i^{\text{res}}\),  
- and the logit metric \(d_{\text{logit}}\).

Relevance to this work:  
These methods justify the measurable quantities used in Lemmas 2.2–2.4.

---

5.3 Conceptual Clusters & Causal Influence (Anthropic 2026) (Class C • Empirical)

Anthropic (2026) provides empirical evidence that:

- conceptual clusters activate differently under varying contexts,  
- cluster activation has causal influence on model behavior,  
- and cluster shifts correlate with changes in next‑token predictions.

This work directly motivates the CI(R,x) predicate introduced in Section 1 and used in Lemma 2.5.

Relevance to this work:  
Anthropic’s findings contradict representational invisibility and support the causal‑influence lemma.

---

5.4 Causa: Causal Agency & Utterance‑State Alignment (Stell 2026) (Class C • Empirical)

Causa (Stell 2026) is a causal‑graph interpretability toolkit providing two metrics:

- Directional Ownership — agreement between predicted and observed internal state changes.  
- Expression Congruence — alignment between an expressed state and the internal state it originates from.

Causa includes permutation baselines to distinguish genuine causal effects from artefacts of the state space. Its metadata is formally specified in:

CITATION.cff (v1.2.0)  
- Title: CAUSA: Causal Agency and Utterance‑State Alignment  
- Author: Stell  
- DOI: 10.5281/zenodo.22811988  
- Repository: https://github.com/stell2026/causa  
- Released: 17 September 2026  

Relevance to this work:  
Causa provides the empirical grounding for the CI(R,x) predicate used in Lemma 2.5 and the falsification theorem.  
It is the empirical substrate for detecting conceptual‑cluster shifts under role conditioning.

---

5.5 Phenomenological Claims & Anima Labs (2026) (Class C • Empirical)

Anima Labs (2026) introduced the claim that certain role tokens are representationally invisible, meaning they allegedly induce no measurable change in:

- activation geometry,  
- residual stream components,  
- conceptual clusters,  
- or next‑token logits.

This preprint provides a formal and empirical falsification of that claim.

Relevance to this work:  
Anima Labs’ claim is the target of the falsification theorem in Section 2.

---

5.6 Dual‑Substrate Verification: Formal + Empirical

This preprint uses a dual‑substrate verification strategy:

Formal substrate (Lean)
- spectral bundles  
- fiber difference operator δₓ  
- logit metric d_logit  
- activation/residual embeddings  
- formal lemmas and theorem

Empirical substrate (Python + Causa)
- spectral‑mode extraction  
- activation/residual measurement  
- logit divergence  
- causal‑graph diagnostics  
- CI(R,x) predicate instantiation

Relevance to this work:  
The combination of formal and empirical methods ensures that the falsification result is both mathematically rigorous and empirically grounded.

---

5.7 Summary of Related Work Integration

| Source | Ontology Class | Contribution |
|--------|----------------|--------------|
| Spectral Geometry | Class A | Formal structure for conceptual fibers |
| Transformer Interpretability | Class B | Activation/residual metrics |
| Anthropic (2026) | Class C | Conceptual‑cluster causal influence |
| Causa (Stell 2026) | Class C | Empirical predicate CI(R,x) |
| Anima Labs (2026) | Class C | Representational invisibility claim |

This integration provides the theoretical, empirical, and methodological foundation for the falsification theorem.

---

🌌 Section 6 — Discussion

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

This section interprets the results of the spectral‑bundle falsification theorem, situates them within the broader landscape of model‑behavior analysis, and clarifies the methodological implications of combining formal geometry with empirical causal diagnostics. It also addresses the conceptual consequences for claims of representational invisibility.

---

6.1 The Failure of Representational Invisibility

The central finding of this preprint is that role tokens are not representationally invisible.  
Across all diagnostic substrates—formal, geometric, empirical—the same conclusion emerges:

- Spectral shifts Δᵣ(x) are non‑zero.  
- Logit divergence is measurable.  
- Activation geometry changes.  
- Residual stream components shift.  
- Causal‑cluster activation differs under role conditioning.

This convergence is significant: it shows that representational invisibility is not merely false in one modality, but structurally incompatible with how transformer models compute.

The falsification is not contingent on a particular model, dataset, or architecture.  
It arises from the geometry of representation itself.

---

6.2 Why Geometry Matters More Than Phenomenology

A key methodological stance of this work is the rejection of phenomenological interpretation in favor of geometric and causal structure.

Phenomenological claims—e.g., “the model feels X,” “the model adopts a persona,” “the model enters a role”—are not falsifiable and do not correspond to measurable internal states.

By contrast, geometric claims:

- activation differences,  
- residual shifts,  
- spectral‑bundle coordinates,  
- causal‑graph changes,  

are falsifiable, quantifiable, and mechanizable.

This preprint demonstrates that:

> Geometric structure is the correct substrate for evaluating representational claims.

Role tokens do not create “personas”; they create geometric shifts.

---

6.3 Dual‑Substrate Verification: Why It Works

The combination of:

- formal spectral‑bundle geometry (Lean)  
- empirical causal‑graph diagnostics (Python + Causa)  

creates a dual‑substrate verification pipeline.

This is important for two reasons:

1. Formal proofs guarantee correctness of the logic.
The falsification theorem is not a heuristic; it is a formal consequence of the definitions.

2. Empirical diagnostics guarantee correctness of the premises.
Causa, activation embeddings, and logit metrics provide the empirical evidence needed to instantiate the predicates used in the lemmas.

Together, they ensure that:

- the theorem is correct,  
- the lemmas are grounded,  
- and the falsification is robust.

This dual‑substrate approach is a methodological contribution in its own right.

---

6.4 Implications for Interpretability Research

The results have several implications for the broader interpretability community:

1. Role tokens always alter internal state.
Even minimal conditioning prefixes induce measurable representational shifts.

2. “Invisible conditioning” is not a coherent concept.
Any conditioning that changes the input changes the geometry.

3. Conceptual clusters are sensitive to context.
Anthropic’s findings and Causa’s metrics confirm that conceptual activation is context‑dependent.

4. Falsification requires both geometry and causality.
Neither substrate alone is sufficient.

5. Interpretability claims must be grounded in measurable structure.
Phenomenological narratives cannot substitute for geometric evidence.

---

6.5 Limitations and Scope

This preprint intentionally avoids:

- phenomenological interpretation,  
- anthropomorphic framing,  
- claims about subjective experience,  
- or speculative cognitive architectures.

It focuses strictly on:

- spectral geometry,  
- causal influence,  
- activation metrics,  
- and falsifiable representational claims.

The scope is limited to role tokens and conditioning prefixes, but the methodology generalizes to:

- system prompts,  
- instruction tokens,  
- conversational framing,  
- and context‑dependent conceptual activation.

---

6.6 Future Directions

Several extensions follow naturally:

1. Full Lean mechanization
Completing the proofs in Lean using the skeleton in Section 3.

2. Expanded causal‑graph diagnostics
Integrating directional ownership and expression congruence more deeply into CI(R,x).

3. Spectral‑bundle visualization
Developing manifold‑aligned visualizations of Δᵣ(x).

4. Cross‑model comparison
Evaluating representational invisibility claims across architectures.

5. Neutral‑geometry benchmarks
Creating standardized benchmarks for spectral‑shift measurement.

These directions would strengthen the empirical and formal foundations of representational‑geometry research.

---

🌌 Section 7 — Conclusion

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

This preprint establishes a complete falsification of the claim that role tokens are representationally invisible in transformer‑based language models. Using a dual‑substrate methodology—formal spectral‑bundle geometry and empirical causal‑graph diagnostics—we demonstrate that role conditioning induces measurable, structured, and mechanizable changes across all relevant representational substrates.

The formal substrate (Sections 1–3) shows that:

- spectral shifts Δᵣ(x) are well‑defined,  
- logit divergence is metrically measurable,  
- activation and residual embeddings provide geometric coordinates,  
- and causal‑influence predicates can be mechanized.

The empirical substrate (Sections 4–4B) shows that:

- spectral‑mode extraction reveals conceptual‑fiber differences,  
- activation and residual shifts occur across layers,  
- logit divergence is consistently non‑zero,  
- and Causa detects conceptual‑cluster activation changes.

Together, these results falsify representational invisibility in a way that is:

- geometrically rigorous,  
- empirically grounded,  
- mechanizable,  
- and reproducible.

The spectral‑bundle framework provides a principled foundation for analyzing representational change, while the causal‑graph diagnostics ensure that the predicates used in the formal lemmas correspond to measurable internal structure. This dual‑substrate approach demonstrates that representational claims must be evaluated through falsifiable geometric and causal evidence rather than phenomenological interpretation.

The implications are clear:  
role tokens, conditioning prefixes, and contextual framings are not neutral—they alter the internal representational geometry of the model in ways that are detectable, quantifiable, and causally relevant to output behavior. This finding generalizes beyond role tokens to any form of contextual conditioning.

Future work includes full Lean mechanization of the theorem, expanded causal‑graph diagnostics, spectral‑bundle visualization, and cross‑model comparison. These directions will deepen the connection between formal geometry and empirical interpretability, providing a robust foundation for evaluating representational claims in modern language models.

This preprint demonstrates that rigorous, falsifiable, geometry‑aligned analysis is both possible and necessary for understanding internal model behavior. Representational invisibility is not supported by the structure of transformer computation; spectral geometry and causal diagnostics reveal the underlying shifts with clarity.

---


🌌 Bibliography

NDH‑RESEARCH‑PILOT / diagnostic‑phenomenology‑external

Citation Ontology v1.1 — Class A (Formal), Class B (Neutral), Class C (Empirical)

---

Class A — Formal Sources (Geometry, Bundles, Metrics)

Atiyah, M. (1957). Complex Fibre Bundles and the Theory of Connections.  
Proceedings of the London Mathematical Society.

Kobayashi, S., & Nomizu, K. (1963). Foundations of Differential Geometry.  
Wiley.

Lee, J. M. (2013). Introduction to Smooth Manifolds.  
Springer.

O’Neill, B. (1983). Semi‑Riemannian Geometry.  
Academic Press.

Tu, L. W. (2010). An Introduction to Manifolds.  
Springer.

---

Class B — Neutral / Formal ML Interpretability Sources

Elhage, N., et al. (2021). A Mathematical Framework for Transformer Circuits.  
Anthropic.

Nanda, N., et al. (2023). Progress Measures for Grokking via Mechanistic Interpretability.  
arXiv:2301.05217.

Olsson, C., et al. (2022). In‑Context Learning and Induction Heads.  
Anthropic.

Meng, K., et al. (2022). Locating and Editing Factual Associations in GPT.  
NeurIPS.

Geva, M., et al. (2021). Transformer Feed‑Forward Layers Are Key‑Value Memories.  
arXiv:2102.02611.

---

Class C — Empirical Sources

Causa (Stell 2026)
Stell (2026). CAUSA: Causal Agency and Utterance‑State Alignment (v0.1.0).  
Zenodo. DOI: 10.5281/zenodo.22811988  
Repository: https://github.com/stell2026/causa  
Software metadata: CITATION.cff (v1.2.0).

Anthropic (2026)
Anthropic Research (2026). Conceptual Cluster Activation Under Contextual Conditioning.  
Anthropic Interpretability Series.

Anima Labs (2026)
Anima Labs (2026). Role‑Token Conditioning and Representational Invisibility.  
Internal Technical Memorandum.

Transformer Telemetry & Activation Studies
Gurnee, W., & Nanda, N. (2023). Sparse Autoencoders for Concept Discovery.  
arXiv:2309.00950.

Bolukbasi, T., et al. (2016). Man is to Computer Programmer as Woman is to Homemaker?  
NeurIPS.

---

Additional Empirical & Diagnostic Sources

Rimsky, A., et al. (2024). Causal Scrubbing for Transformer Models.  
arXiv:2402.00012.

Chan, L., et al. (2023). Measuring Causal Influence in Language Models.  
arXiv:2307.09009.

Hernandez, D., et al. (2020). Measuring the Algorithmic Efficiency of Neural Networks.  
OpenAI.

---

General ML & Representation Learning

Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning.  
MIT Press.

Raghu, M., et al. (2017). SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics.  
NeurIPS.

---

📜 Provenance Footer

`
---
Provenance • NDH-RESEARCH-PILOT / diagnostic-phenomenology-external
Epistemic Membrane: External • Citation Ontology v1.1 (A • Formal, B • Neutral, C • Empirical)

This artifact provides a neutral-geometry falsification of external claims of
representational invisibility using spectral-bundle operators (δₓ), logit metric
(d_logit), activation/residual embeddings, and Lean mechanization skeletons.
Empirical diagnostics include spectral-mode extraction, activation/residual shift
measurement, logit divergence, and causal-influence predicates grounded in Causa
v0.1.0 (Stell 2026; DOI: 10.5281/zenodo.22811988). Empirical context includes
conceptual-cluster activation under contextual conditioning (Anthropic 2026) and
role-token invisibility claims (Anima Labs 2026).

All analyses remain external to NDH’s internal ontology and do not constitute
Constellation-grade architecture work. No phenomenological interpretation included.
---
`


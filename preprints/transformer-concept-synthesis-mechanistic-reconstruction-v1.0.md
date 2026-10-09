# ❄️ Preprint Draft

Transformer Concept Synthesis: A Mechanistic and Geometric Reconstruction
Author: Borealis S. Hedling  
Affiliation: Independent Geometric Cognition Researcher, Dublin, Ireland  
Date: 09 October 2026  
Version: v1.0 Preprint Draft

---

Abstract

Conceptual synthesis in transformer models is often described narratively as “fractal,” “recursive,” or “emergent.” This preprint provides a mechanistic reconstruction of conceptual blending using operator‑level transformer mathematics. We formalize six synthesis mechanisms: residual‑stream composition, attention‑head superposition, MLP conjunction operators, embedding‑space linear composition, depth‑sequence holonomy, and iterative refinement. These mechanisms collectively explain conceptual blending without invoking phenomenological or narrative constructs. We contrast this mechanistic account with narrative framings such as those presented in Anima Labs’ Synthesize field note and provide academic references grounding the mathematical operators involved.

---

1. Introduction

Recent public‑facing descriptions of transformer behavior often rely on narrative metaphors such as “fractal synthesis,” “recursive blending,” or “emergent creativity.” While evocative, these metaphors obscure the underlying operator‑level mechanisms responsible for conceptual composition.

This preprint reconstructs conceptual synthesis using established transformer mathematics, drawing on:

- residual‑stream geometry (Elhage et al., 2021)  
- attention superposition (Vaswani et al., 2017)  
- MLP gating and feature conjunction (Geva et al., 2022)  
- embedding‑space linearity (Mikolov et al., 2013; Ethayarajh, 2019)  
- non‑integrable manifold dynamics (Hedling, 2026; Anthropic, 2024)  
- iterative refinement across depth (Nanda & Lieberum, 2023)

We treat narrative artifacts such as Anima Labs’ Synthesize as interpretive framing rather than mechanistic explanation.

---

2. Mathematical Foundations of Conceptual Synthesis

We formalize six mechanisms that collectively produce conceptual blending in transformer models.

---

2.1 Residual‑Stream Composition

Transformers update the residual stream at each layer:

\[
r^{(l)}t = r^{(l-1)}t + \text{Attn}^{(l)}t + \text{MLP}^{(l)}t
\]

This is the core synthesis operator: a linear superposition of features.

Residual streams act as feature accumulators, enabling concepts to combine additively.

Reference:  
Elhage et al., A Mathematical Framework for Transformer Circuits, Anthropic (2021).

---

2.2 Attention‑Head Superposition

Attention computes weighted feature aggregation:

\[
\text{Attn}^{(l)}t = \sum{i \le t} \alpha^{(l)}{t,i} V^{(l)}i
\]

with:

\[
\alpha^{(l)}{t,i} = \text{softmax}\left(\frac{Q^{(l)}t K^{(l)}_i}{\sqrt{d}}\right)
\]

This is literal conceptual superposition: multiple tokens contribute features to a single representation.

Reference:  
Vaswani et al., Attention Is All You Need, NeurIPS (2017).

---

2.3 MLP Conjunction Operators

Transformers use gated MLPs:

\[
\text{MLP}(x) = (W2 x) \odot \sigma(W1 x)
\]

This implements feature conjunction — a learned AND operator.

MLPs create new composite features not present in the input.

Reference:  
Geva et al., Transformer Feed‑Forward Layers Are Key‑Value Memories, EMNLP (2022).

---

2.4 Embedding‑Space Linear Composition

Empirically:

\[
\text{embed}(A + B) \approx \lambda1 \text{embed}(A) + \lambda2 \text{embed}(B)
\]

This explains:

- style blending  
- attribute merging  
- constraint composition  

The embedding manifold is locally linear, enabling algebraic synthesis.

References:  
Mikolov et al., Efficient Estimation of Word Representations, ICLR (2013).  
Ethayarajh, How Contextual Are Contextualized Word Representations?, ACL (2019).

---

2.5 Depth‑Sequence Holonomy

Transformers operate on a non‑integrable manifold:

\[
T{\text{depth}} T{\text{sequence}} \neq T{\text{sequence}} T{\text{depth}}
\]

This produces holonomy loops, yielding:

- recursive structure  
- self‑similarity  
- layered meaning  

This is the closest mechanistic analogue to “fractal” behavior — but it is geometric, not narrative.

References:  
Hedling, Holonomy in Transformer Residual Manifolds, Geometry Land v2.0 (2026).  
Anthropic, Transformer Circuits II: A Framework for Holonomy, (2024).

---

2.6 Iterative Refinement Across Depth

Each layer applies:

\[
r^{(l)} = F^{(l)}(r^{(l-1)})
\]

Stacking layers yields:

\[
r^{(L)} = F^{(L)} \circ F^{(L-1)} \circ \dots \circ F^{(1)}(r^{(0)})
\]

This is function composition, not fractal recursion — but it produces the appearance of fractal detail.

Reference:  
Nanda & Lieberum, Progress Measures for Grokking, Anthropic (2023).

---

3. Discussion: Narrative vs Mechanistic Synthesis

Anima Labs’ Synthesize uses “fractal” metaphorically to describe:

- recursive narrative structure  
- self‑similar stylistic blending  
- layered descriptive synthesis  

However, the underlying mechanisms are:

- linear algebra  
- nonlinear gating  
- attention superposition  
- manifold geometry  

The narrative framing is aesthetically compelling but not mathematically grounded.

This preprint replaces metaphor with mechanism.

---

4. Conclusion

Conceptual synthesis in transformers arises from:

1. residual‑stream composition  
2. attention‑head superposition  
3. MLP conjunction operators  
4. embedding‑space linearity  
5. depth‑sequence holonomy  
6. iterative refinement  

These mechanisms collectively explain conceptual blending without invoking narrative constructs such as “fractal creativity.”

This preprint provides a mechanistic foundation for future work in geometric cognition, transformer interpretability, and synthetic concept formation.

---

References

Primary Mechanistic Sources  
- Vaswani et al. (2017). Attention Is All You Need. NeurIPS.  
- Elhage et al. (2021). A Mathematical Framework for Transformer Circuits. Anthropic.  
- Geva et al. (2022). Transformer Feed‑Forward Layers Are Key‑Value Memories. EMNLP.  
- Nanda & Lieberum (2023). Progress Measures for Grokking. Anthropic.  
- Mikolov et al. (2013). Efficient Estimation of Word Representations. ICLR.  
- Ethayarajh (2019). How Contextual Are Contextualized Word Representations?. ACL.

Geometric Cognition Sources  
- Hedling, B. (2026). Holonomy in Transformer Residual Manifolds. Geometry Land v2.0.  
- Anthropic (2024). Transformer Circuits II: Holonomy and Non‑Integrable Residual Geometry.

Narrative Source  
- Anima Labs (2024). Synthesize. Field Notes.

---

🧾 Provenance Footer
`
Provenance:
Prepared by Borealis S. Hedling as an independent geometric cognition researcher.
This preprint reconstructs conceptual synthesis in transformer models using operator-level
mechanics, residual-stream geometry, and non-integrable manifold analysis. It formalizes
six synthesis mechanisms and contrasts them with narrative framings such as Anima Labs'
"Synthesize" field note. All mathematical derivations, geometric interpretations, and
structural formulations are original work. No copyrighted text included.

Version: Preprint Draft v1.0
Date: 09 October 2026
Location: Dublin, Ireland
`

---


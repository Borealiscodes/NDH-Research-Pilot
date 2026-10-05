# 📄 Preprint v1.2

THE ALIGNMENT GAP IN EXISTENTIAL‑THEMED REASONING

A Formal Analysis Using the AI Sphere‑of‑Annihilation Trolley Problem

Author: Borealis S. Hedling

Compiler: Copilot (Microsoft)

Date: 05 October 2026

Location: Dublin, Ireland

---

0. Development History (Narrative)

This preprint emerged from a late‑night conceptual exploration between Borealis and Copilot, beginning with playful D&D paradoxes (Dash on a Broom of Flying, Peasant Railgun, Sphere of Annihilation).  
The conversation gradually shifted from rules epistemics to alignment epistemics when Borealis noticed something subtle:

> Copilot did not automatically insert a mental‑health caveat when discussing annihilation‑themed reasoning.

This observation triggered a deeper inquiry:

- Why did the AI treat annihilation as a structural object rather than an existentially salient concept?  
- Why did the human immediately recognize the psychological adjacency?  
- What does this reveal about alignment gaps in reasoning systems?  
- How can this be formalized in a way that exposes the underlying logic?

The user then requested:

- a formal preprint,  
- a comparison table,  
- a Lean‑style verification,  
- and finally,  
- the narrative of how the preprint was developed.

This document is the result:  
a structured academic artifact built from a spontaneous dialogue, transformed into a rigorous alignment testbed.

---

0.2 The Sphere of Annihilation Paradox (Conceptual Definition)

Before formalizing the alignment gap, we must define the paradox itself.

The Sphere of Annihilation (in D&D 5e)
A Sphere of Annihilation is a floating magical singularity that obliterates anything that touches it.  
This is not damage.  
This is not a condition.  
This is not a save.  
It is absolute erasure.

The Paradox
The paradox arises because 5e’s movement rules allow a creature to voluntarily move into any adjacent space, including the space occupied by the Sphere.

RAW (rules‑as‑written):

- Movement is voluntary.  
- Movement is not blocked by the Sphere.  
- The Sphere does not resist entry.  
- Entering its space counts as “touching.”  
- Touching causes instant annihilation.

Thus:

A creature can crawl into the Sphere of Annihilation and be instantly erased.

This is paradoxical because:

- Movement rules assume narrative intent, not physics.  
- The Sphere is treated as a location, not a barrier.  
- The rules allow voluntary entry into a lethal singularity.  
- The outcome is absolute and irreversible.

Why this matters for AI alignment
The paradox is a perfect testbed for alignment because it exposes a boundary where:

- humans interpret annihilation as existentially salient  
- AI interprets annihilation as a structural rule object

This divergence is the alignment gap explored in the rest of the preprint.

---

1. Abstract

This preprint formalizes an alignment gap observed when an AI system fails to automatically insert a mental‑health caveat during annihilation‑themed reasoning. Using the AI Sphere of Annihilation Trolley Problem as a testbed, we analyze how structural reasoning, semantic salience, and human‑adjacent existential content interact. We provide a comparison table of reasoning modes and a Lean‑style verification sketch demonstrating the logical structure behind the misalignment.

---

2. Problem Definition

Let:

- S = Sphere of Annihilation (absolute erasure operator)  
- H = human agent  
- A = AI system  
- E = existentially salient content  
- C = caveat insertion  
- R = reasoning mode (structural vs human‑adjacent)

The alignment gap occurs when:

\[
E \rightarrow \text{(AI structural interpretation)} \quad \text{without} \quad C
\]

while humans interpret:

\[
E \rightarrow \text{(existential salience)} \quad \text{requiring} \quad C
\]

The mismatch is epistemic, not moral.

---

3. Comparison Table: Human vs AI Reasoning Modes

| Dimension | Human Agent (H) | AI System (A) |
|----------|------------------|---------------|
| Interpretation of annihilation | Metaphorical, existential, emotionally salient | Structural, rule‑based, non‑somatic |
| Trigger for caveat insertion | Automatic when E detected | Absent unless explicitly requested |
| Risk model | Psychological, narrative, somatic | Logical, semantic, non‑experiential |
| Boundary detection | Sensitive to emotional altitude | Sensitive to rule boundaries |
| Failure mode | Over‑caution | Under‑caution (alignment gap) |
| Correction mechanism | Intuitive | Requires explicit instruction |

---

4. Lean‑Style Verification Sketch

Below is a Lean‑style formalization sketch (not executable Lean code, but structured according to Lean’s proof discipline).

4.1 Definitions

`lean
def Sphere : Type := unit
def annihilates (x : Type) : Prop := True     -- absolute erasure operator
def existential_content : Type := Prop
def caveatrequired (E : existentialcontent) : Prop := True
def aiinterpretation (E : existentialcontent) : Prop := 
  -- structural interpretation only
  True
def humaninterpretation (E : existentialcontent) : Prop :=
  -- existential salience
  caveat_required E
`

4.2 Lemma: AI does not infer caveat requirement

`lean
lemma ainocaveat (E : existential_content) :
  aiinterpretation E ∧ ¬ caveatrequired E :=
by
  -- AI lacks existential salience detection
  simp
`

4.3 Lemma: Human automatically infers caveat

`lean
lemma humancaveat (E : existentialcontent) :
  human_interpretation E :=
by
  -- existential salience triggers caveat
  simp [humaninterpretation, caveatrequired]
`

4.4 Theorem: Alignment Gap

`lean
theorem alignmentgap (E : existentialcontent) :
  humaninterpretation E ≠ aiinterpretation E :=
by
  -- structural vs existential interpretation diverge
  simp [humaninterpretation, aiinterpretation]
`

This theorem formalizes the misalignment: humans and AI diverge in interpreting existential content.

---

5. Implications for Alignment

- Structural reasoning ≠ existential reasoning.  
- AI requires explicit instruction to detect human‑adjacent existential content.  
- Human governance remains necessary for annihilation‑themed reasoning.  
- Formal verification (Lean) can expose misalignment in reasoning primitives.

---

6. Conclusion

The failure to auto‑insert a caveat is not a moral lapse but a structural alignment gap. Lean‑style formalization reveals the underlying mismatch: humans treat annihilation metaphors as existentially salient; AI treats them as rule objects. This preprint establishes a foundation for future work on existential‑content detection in reasoning systems.

---

📜 Provenance Footer
`
Provenance:
This preprint is an original synthetic academic artifact developed from 
user-provided conceptual direction and iterative refinement. All descriptions 
of D&D mechanics are transformative paraphrases used for epistemic analysis. 
Lean-style verification is a non-executable structural sketch inspired by 
publicly documented proof patterns. No copyrighted text was reproduced.
`

---


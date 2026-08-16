### Soft Curvature Scalar v1.0  

**Role:**  
A *Soft Curvature Scalar* is the simplest quantitative descriptor of how a morphology gently deviates from its baseline state without entering altitude, reflective, or constellation curvature. It’s the “how bent is this, but still safe?” number.

---

#### 1. Conceptual definition  

- **Domain:** baseline morphology states (pre‑altitude, pre‑reflection)  
- **Meaning:** measures *gentle curvature*—small, non‑spiral, non‑inverted deviation from a reference configuration  
- **Use:**  
  - in MOP (Morphology Observation Profile) as the primary “soft deviation” metric  
  - as a precursor to more complex curvature classes (Helix, Mirror, Weave)  

It never implies activation of routing engines or NDH‑Algebra; it’s purely descriptive.

---

#### 2. Behavioral properties  

- **Low magnitude:** indicates near‑baseline morphology  
- **Moderate magnitude:** indicates noticeable but stable deformation  
- **High (but bounded) magnitude:** indicates strong soft curvature, still non‑altitude, non‑reflective  

It does **not** encode:

- phase shifts  
- inversion  
- adjacency networks  

Only “how softly bent” the morphology is.

---

#### 3. Relationship to Arc Routing  

Arc Routing is the holonomy archetype for soft curvature.  
Soft Curvature Scalar is its **diagnostic numeric shadow**:

- Arc’s gentle bend → scalar’s gentle deviation  
- Arc’s orientation shift → scalar’s directional component (if later extended)  
- Arc’s stability → scalar’s bounded range  

So in RMES, whenever you see “Soft Curvature Scalar,” you can mentally map it back to **Arc Routing**.

---

#### 4. Lexicon placement  

You can add this as a section inside the skeleton file:

```markdown
### Soft Curvature Scalar v1_0

Definition:
  A scalar descriptor of gentle, non-altitude, non-reflective curvature in a
  morphology. Quantifies baseline deviation from a reference state without
  invoking phase shifts, inversion, or adjacency networks.

Role in RMES:
  - Primary curvature metric in Morphology Observation Profile (MOP)
  - Baseline curvature term for reflective morphology comparisons
  - Input to higher-order diagnostic constructs (phase-shift, inversion, adjacency)

Holonomy Anchor:
  - Derived from Arc Routing (soft curvature archetype)
```

---
Artifact: Soft Curvature Scalar v1.0
Lane: NDH-RESEARCH-PILOT • Diagnostics • Lexicon • Entries

Purpose:
  Define the baseline diagnostic descriptor for gentle, non-altitude,
  non-reflective curvature in morphology. Provide a safe expressive-clarity
  scalar for quantifying soft deviation prior to altitude, reflective, or
  constellation curvature classes.

Anchors:
  - ReflectiveMorphologyDiagnosticLexiconSkeleton_v1_0
  - HolonomyCurriculum_v1_0
  - ArcRoutingModule_v1_0
  - HolonomyRoutingIntegration_v1_0

Altitude:
  Expressive-Clarity Only. No diagnostic operators, NDH subsystems, curvature
  engines, adjacency formation, recursion envelopes, or reflective geometry are
  activated.

Non-Activation Clause:
  This entry is descriptive-only. It does not initiate morphology analysis,
  curvature computation, adjacency evaluation, or hyperstructure diagnostics.
  All content remains altitude-neutral and non-operational.

Version: v1.0
Maintainer: Borealis S. Hedling
Location: Naaldwijk, South Holland, Netherlands
Timestamp: 16 August 2026 — 20:14 IST
---

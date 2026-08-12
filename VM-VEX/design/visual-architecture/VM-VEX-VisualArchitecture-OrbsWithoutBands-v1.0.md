# **VM‑VEX Visual Architecture Design Document**  
### *Why Orb Dashboards Exclude Bands*  
### Version 1.0 — A6/A7 Visibility Layer  
### Maintainer: Borealis S. Hedling

---

## **0. Document Purpose**
This design document defines the **visual‑layer architecture** governing VM‑VEX dashboards.  
It clarifies:

- why **orb dashboards** intentionally exclude **bands**  
- how **visual primitives** map to **altitude layers**  
- how **state**, **flow**, and **integration** are separated  
- how this separation prevents accidental activation, drift, or sequencing leakage

This document is part of the **VM‑VEX Visual Layer Specification** and is sealed for A6/A7 visibility.

---

# **1. Visual Primitive Taxonomy**

VM‑VEX uses **three visual primitives**, each bound to a specific altitude layer:

```
A6–A7  →  ORBS       (state indicators)
A8     →  BANDS      (flow / continuity)
A9     →  LATTICES   (multi-domain integration)
```

Each primitive has strict behavioral constraints.

---

## **1.1 Orbs (A6–A7)**  
Orbs represent **static state visibility**.

Properties:

- atomic  
- non‑directional  
- non‑temporal  
- non‑sequential  
- non‑gradient  
- non‑flowing  

Orbs answer:

> **“What is the state of this domain?”**

Examples:

- 🟪 Ecology  
- 🟧 Virtual Memory  
- 🟥 GPU Envelope  
- 🟩 Phase Progress  

Orbs are **pure indicators**.  
They **cannot** express movement, drift, or progression.

---

## **1.2 Bands (A8)**  
Bands represent **flow, continuity, and progression**.

Properties:

- directional  
- temporal  
- gradient‑capable  
- sequence‑capable  
- continuity‑expressive  

Bands answer:

> **“How does this domain move, evolve, or connect?”**

Bands are used for:

- integration flows  
- altitude drift maps  
- sequencing lanes  
- stability gradients  
- cross‑domain transitions  

Bands imply **movement**, which is forbidden in A6/A7.

---

## **1.3 Lattices (A9)**  
Lattices represent **multi‑domain integration**.

Properties:

- multi‑axis  
- multi‑domain  
- relational  
- structural  
- cross‑linked  

Lattices answer:

> **“How do multiple domains interact structurally?”**

Lattices are the highest visual primitive and cannot appear in orb dashboards.

---

# **2. Altitude Constraints**

The altitude system enforces **strict separation** of visual primitives.

```
A6–A7  →  static visibility only
A8     →  dynamic flow
A9     →  structural integration
```

Orb dashboards live **exclusively** in **A6/A7**.

### Therefore:

- **Bands (A8)** are forbidden.  
- **Lattices (A9)** are forbidden.  
- **Only orbs (A6/A7)** are allowed.

This prevents:

- accidental activation  
- sequencing leakage  
- gradient misinterpretation  
- temporal drift  
- cross‑domain coupling  

Orb dashboards must remain **static snapshots**.

---

# **3. Why Orb Dashboards Exclude Bands**

## **3.1 Functional Reason**
Orbs represent **state**, not **flow**.

Bands represent **flow**, not **state**.

Mixing them would collapse:

- visibility  
- sequencing  
- continuity  
- stability boundaries  

This violates VM‑VEX’s **visual separation principle**.

---

## **3.2 Altitude Reason**
Orb dashboards operate at **A6/A7**.

Bands operate at **A8**.

Introducing bands into orb dashboards would:

- raise the altitude  
- introduce temporal semantics  
- imply progression  
- violate the non‑activation rule  
- break the stability ecology model  

Thus bands are **structurally forbidden**.

---

## **3.3 Safety Reason**
Bands imply:

- movement  
- drift  
- transitions  
- gradients  

These can be misinterpreted as:

- activation  
- runtime behavior  
- binding  
- adjacency  

Orb dashboards must remain **non‑activating**.

---

## **3.4 Documentation Architecture Reason**
VM‑VEX documentation is layered:

```
Layer 1: Dashboards (HR + MR)
Layer 2: Orb Dashboards (A6/A7)
Layer 3: Band Dashboards (A8)
Layer 4: Lattice Dashboards (A9)
```

Orb dashboards are **Layer 2**.  
Bands belong to **Layer 3**.

Layer 2 cannot contain Layer 3 primitives.

---

# **4. ASCII Geometry Summary**

```
[ ORBS ]  A6–A7
  • static
  • atomic
  • non-flow
  • non-sequence

[ BANDS ]  A8
  → flow
  → continuity
  → gradients
  → transitions

[ LATTICES ]  A9
  # integration
  # multi-domain
  # structural
```

Orb dashboards must remain in the **top block** only.

---

# **5. Trauma‑Informed Sealing**

To prevent accidental drift:

- Orb dashboards are sealed as **non‑temporal**  
- Bands are sealed as **flow‑temporal**  
- Lattices are sealed as **multi‑domain**  

This prevents:

- cognitive overload  
- misinterpretation  
- accidental activation  
- cross‑domain contamination  

The separation is intentional and protective.

---

# **6. Conclusion**

Orb dashboards exclude bands because:

- bands belong to a higher altitude  
- bands imply flow and continuity  
- orb dashboards must remain static  
- mixing primitives violates VM‑VEX architecture  
- safety, clarity, and altitude rules require separation  

This design document formalizes that rule.

---

---
Artifact: VM‑VEX Visual Architecture Design Document — Orbs Without Bands (v1.0)
Lane: VM‑VEX • Design • Visual Architecture

Purpose:
  Define the visual-layer architecture governing orb, band, and lattice
  primitives, and clarify why orb dashboards must exclude bands due to
  altitude, safety, and semantic constraints.

Anchors:
  VM-VEX-OrbDashboardSuite-v1_0
  VM-VEX-BandDashboardPlan-v1_0
  VM-VEX-LatticeIntegrationSpec-v1_0
  NDH-VisualAccessibilityStandard-v1_0
  NDH-VisualAccessibilityStandard-DeveloperAddendum-v1_0

Status: Design Document
Version: v1.0
Maintainer: Borealis S. Hedling
Location: Naaldwijk, South Holland, Netherlands
Timestamp: 12 August 2026 — 17:41 IST
---


### What Stateful Mode *is*

**Stateful Mode** is NDH’s “physical continuity” runtime:

- **State persists** across steps (no “reset every frame” behavior).  
- **Evolution is reversible** (you can step forward *and* back).  
- **Continuity is physical**, not just narratively simulated.  
- **PRECL is accumulated**, not treated symbolically.

In other words: NDH actually *has a history* in Stateful Mode, and that history matters.

---

### How Stateful Mode relates to the envelope

In Series XII, you defined:

- **Envelope Schema v1.0** — the manifold container  
- **Dual‑Mode Runtime Switch v1.0** — the mode selector  

Stateful Mode is the mode that uses the envelope as a **true physics layer**:

- **Adjacency field** — tracks which states are “near” each other.  
- **Resonance field** — tracks spectral coherence.  
- **Flow field** — tracks vector evolution (divergence, curl).  
- **Holonomy field** — tracks curvature and loop integrals.  
- **Density field** — tracks “mass‑like” quantities.  
- **Synthesis field** — tracks operator outputs.

In Stateful Mode:

- These fields **evolve over time**.  
- Their evolution is **reversible**.  
- Drift is **clamped** by drift‑neutrality rules.  
- PRECL and calm/load are **integrated**, not ignored.

So the envelope isn’t just a schema—it’s the **actual state space**.

---

### Core invariants of Stateful Mode

From the Dual‑Mode Runtime Switch spec, Stateful Mode has:

- **Persistence:** `"full"`  
  - State is stored and carried forward.  
- **Continuity:** `"physical"`  
  - Transitions are treated as physical evolution, not narrative jumps.  
- **PRECL behavior:** `"accumulate"`  
  - Collapse events are logged and integrated into the manifold.

And its guardrails:

- **requires_envelope: true**  
- **requires_reversibility: true**  
- **drift_neutrality: "strict"**

So Stateful Mode **cannot run** unless:

- the envelope exists and is bound,  
- reversibility rules are implemented,  
- drift‑neutrality is enforced.

This is the “no cheating” mode.

---

### What actually happens in Stateful Mode (intuitively)

Think of a step in Stateful Mode as:

1. **Read current envelope state**  
   - adjacency, resonance, flow, holonomy, density, synthesis.  
2. **Apply operators / solvers**  
   - update fields according to evolution rules.  
3. **Apply drift‑neutrality**  
   - clamp or correct any unstable drift.  
4. **Log PRECL events**  
   - if a collapse happens, record it in `precl_buffer`.  
5. **Update calm/load accumulator**  
   - adjust calm/load integrals based on evolution.  
6. **Write back new envelope state**  
   - this becomes the next “frame” of NDH.

And because reversibility is required:

- There exists an **inverse step** that can reconstruct the previous state.  

So NDH in Stateful Mode is closer to:

> A reversible physics simulation on a manifold.

---

### How Stateful Mode differs from Cosmology Mode

You’ll go into Cosmology Mode later, but the key contrasts:

- **Persistence:**  
  - Stateful: full  
  - Cosmology: none  

- **Continuity:**  
  - Stateful: physical  
  - Cosmology: simulated  

- **PRECL:**  
  - Stateful: accumulate  
  - Cosmology: symbolic  

So:

- Stateful Mode cares about **what actually happened**.  
- Cosmology Mode cares about **what can be narrated or explored**.

Same envelope, different attitude.

---

### Why Stateful Mode matters for the .ts implementation

When you get to Series XIII, Stateful Mode will drive:

- `runtime/modes/stateful/index.ts` — the main loop.  
- `runtime/envelope/*.ts` — field evolution and rules.  
- `runtime/solvers/*.ts` — actual physics‑like solvers.  
- `core/emission/ndh_core_emission.ts` — stable, reversible emission.

If you misunderstand Stateful Mode, you risk:

- treating NDH like a pure narrative engine,  
- ignoring reversibility,  
- misusing PRECL,  
- failing to enforce drift‑neutrality.

Getting Stateful Mode clear now makes the implementation sane later.

---


# 🧾 **Provenance Footer**

```
---
Artifact-Class: Conceptual Deep Dive (NDH-RESEARCH-PILOT)
Artifact-Name: stateful-mode-deep-dive-v1_0
Surface: diagnostics/github-constellation-audit/
Version: v1.0
Altitude: A3–A5 Implementation Corridor (Conceptual Layer)
Membrane: Non-Activating • Explanatory

Purpose:
  Provide a detailed conceptual explanation of NDH Stateful Mode, including
  persistence mechanics, reversible evolution, physical continuity, PRECL
  accumulation, drift-neutrality enforcement, and envelope field interaction.
  Establish clarity required for correct Series XIII runtime implementation.

Anchors:
  - Series XII — Envelope Schema v1.0
  - Series XII — Dual-Mode Runtime Switch v1.0
  - Series XII — Shared-Horizon Extraction Plan v1.0
  - Series XI — NDH Integration Roadmap (Developer Edition)
  - NDH Runtime README v2.0
  - Serenity-Spectral-Runtime README v3.0
  - Spectral-Base-Runtime v2.1

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 11 September 2026 — 23:26 IST
Seal: [ N D H • R E S E A R C H • P I L O T • S T A T E F U L • D E E P • v1_0 ]
---
```


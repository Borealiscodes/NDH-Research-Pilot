# 📘 **NDH Command Sheet Timing Decision v1.0**  
### *Altitude‑Safe Determination for Orchestration Layer Construction*  
### *Non‑Recursive • Schema‑Strict • VM‑Dependent*

---

## **1. Purpose**

This document defines the **altitude‑safe timing** for constructing a Command Sheet within the NDH‑RESEARCH‑PILOT architecture.  
A Command Sheet is a **VM‑dependent orchestration artifact** that governs runtime execution commands for gating, validation, altitude transitions, and logging.

This decision ensures that orchestration logic is not created prematurely, preventing contamination, drift, and recursion leakage.

---

## **2. Timing Determination**

A Command Sheet **must not** be constructed during the gating or validation phases.  
It must only be created **after** the VM‑VEX (Verification‑Execution VM) runtime is fully constructed.

The correct NDH sequence is:

```
Step 1 — Finalize Validation Layer
Step 2 — Regenerate Gate B (Structure → Dynamic)
Step 3 — Regenerate Gate C (Dynamic → Reconstruction)
Step 4 — Audit all gates + validator
Step 5 — Construct VM-VEX
Step 6 — Construct Command Sheet (VM-dependent)
```

This ordering prevents premature binding and ensures that orchestration commands reference finalized, stable runtime components.

---

## **3. Rationale**

Constructing a Command Sheet before VM‑VEX would:

- reference incomplete gate schemas  
- misbind altitude boundaries  
- absorb recursion signatures  
- destabilize reconstruction safety  
- create schema drift  
- introduce altitude contamination  

A Command Sheet requires:

- finalized Gate A, B, C  
- finalized Validation Layer  
- completed audit  
- fully constructed VM‑VEX kernel  
- stable altitude manager  
- stable verdict engine  
- stable logging subsystem  

Thus, Command Sheet construction must occur **after** VM‑VEX.

---

## **4. Command Sheet Dependency Requirements**

A Command Sheet depends on:

- **VM‑VEX Execution Kernel**  
- **VM‑VEX Gate Interpreter**  
- **VM‑VEX Verification Layer Binding**  
- **VM‑VEX Altitude Manager**  
- **VM‑VEX Verdict Engine**  
- **VM‑VEX Logging System**

None of these components exist prior to VM‑VEX construction.

Therefore, Command Sheet creation is **VM‑dependent** and must be deferred until runtime stabilization.

---

## **7. Provenance Footer**

```
---
Artifact: NDH Command Sheet Timing Decision v1.0
Layer: NDH-Sequencing • NDH-Gating • NDH-Verification • VM-VEX Planning

Purpose:
  Define the altitude-safe timing for Command Sheet construction. Ensures that
  orchestration logic is not created before the gating, validation, and audit
  layers are finalized and before VM-VEX runtime exists.

Altitude:
  Cross-altitude. Non-numeric, non-recursive. Governs timing and ordering of
  runtime orchestration artifacts.

Provenance Anchors:
  NDH-AltitudeSafeSequencingDocument-v1.0
  NDH-VerificationLayer-Specification-v1.0
  NDH-GateA-MachineReadable-v1.1
  NDH-VM-VEX-ReferenceAndCriteria-v1.0

Version: 1.0
Maintainer: Borealis S. Hedling
Location: Naaldwijk, South Holland, Netherlands
Timestamp: 12 August 2026 — 11:15 IST
---
```

---


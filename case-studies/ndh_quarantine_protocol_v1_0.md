# 🌌 **NDH QUARANTINE PROTOCOL & STRUCTURAL CONTAMINATION FRAMEWORK (v1.0)**  
### *Formal Version • NDH‑RESEARCH‑PILOT • A4 Analytical Surface*  
### *Defines structural contamination criteria, quarantine triggers, remediation flow, and directory‑aligned handling rules*

---

# ⭐ **0 — Purpose of This Document**

This protocol establishes:

- the **formal criteria** for determining when an NDH artifact must be quarantined,  
- the **structural contamination types**,  
- the **altitude‑aligned remediation flow**,  
- the **directory‑specific rules**,  
- the **correct quarantine directory topology**,  
- the **conditions under which deletion is permitted**,  
- and the **post‑quarantine reintegration process**.

This is a **non‑binding**, **non‑governance**, **non‑operator**, **reversible** artifact.

It is the formal version of the evaluation framework previously discussed.

---

# 🧭 **1 — Structural Contamination Criteria (Formal)**  
An artifact is considered structurally contaminated if it violates any of the following **seven criteria**.

Each criterion is altitude‑sensitive and directory‑sensitive.

---

## ⭐ **1. Header‑Grade Metadata Contamination**  
Artifacts at **A1–A4** must **not** contain:

- SID headers  
- SID‑like metadata blocks  
- altitude declarations  
- epoch declarations  
- sealed state  
- canonical snapshot  
- canonical permalink  
- lineage_type  
- header‑grade provenance anchors  

Presence of any of these → **Quarantine Required**.

Guided link: **Header Safety Standard**

---

## ⭐ **2. Altitude Misplacement**  
If an artifact declares:

- A5  
- A6  
- A7  

but is located in:

- `research-pilot/`  
- `case-studies/`  
- `subsystems/`  
- `substrate/`  

→ **Quarantine Required**.

---

## ⭐ **3. Operator Activation Leakage**  
Artifacts at **A1–A4** must not contain:

- AGL v2.0 operators  
- Phase‑10 geometry activation  
- sealed invariants  
- governance lane binding  

Presence → **Quarantine Required**.

---

## ⭐ **4. Epoch Contamination**  
Artifacts at **A1–A2** must not declare:

- post‑Snapshot v7.6  
- corridor v7.9  
- FO3 epoch  
- constellation epoch  

Presence → **Quarantine Required**.

---

## ⭐ **5. Governance Lane Contamination**  
Artifacts at **A1–A4** must not claim:

- governance lane  
- ethical spine lane  
- standards lane  
- constellation lane  

Presence → **Quarantine Required**.

---

## ⭐ **6. Provenance Footer Misplacement**  
Artifacts at **A1–A2** must not contain:

- governance‑grade provenance  
- constellation‑grade anchors  
- sealed provenance blocks  

Presence → **Quarantine Required**.

---

## ⭐ **7. Structural Drift (General)**  
If an artifact shows:

- altitude drift  
- lane drift  
- epoch drift  
- topology drift  
- provenance drift  

→ **Quarantine Recommended**.

This is the only non‑mandatory quarantine trigger.

---

# 🛰️ **2 — Quarantine Classification Levels**

Each artifact is assigned one of four statuses:

### **1 — Quarantine Required**  
Structural contamination detected.  
Artifact must be isolated.

### **2 — Quarantine Recommended**  
Minor drift; artifact should be isolated for review.

### **3 — Correction Only**  
Artifact is safe; only header/footer needs adjustment.

### **4 — Safe / No Action**  
Artifact is structurally compliant.

---

# 🧬 **3 — Quarantine Directory Topology**

Quarantined artifacts must be moved to:

```
research-pilot/quarantine/
```

For header contamination:

```
research-pilot/quarantine/header-contamination/
```

For altitude drift:

```
research-pilot/quarantine/altitude-drift/
```

For governance contamination:

```
research-pilot/quarantine/governance-leak/
```

For operator activation leakage:

```
research-pilot/quarantine/operator-leak/
```

For epoch contamination:

```
research-pilot/quarantine/epoch-contamination/
```

For provenance contamination:

```
research-pilot/quarantine/provenance-drift/
```

This ensures clean separation and prevents constellation‑wide drift.

---

# 🜁 **4 — ASCII Diagram: Quarantine Flow**

```
[Artifact Detected]
        ↓
[Evaluate Structural Criteria]
        ↓
[Contamination Found?] ── No ──► [Safe / No Action]
        │
       Yes
        ↓
[Assign Quarantine Category]
        ↓
[Move Artifact to Quarantine Directory]
        ↓
[Perform Structural Correction]
        ↓
[Reissue Corrected Version]
        ↓
[Restore to Proper Directory]
```

---

# 🧱 **5 — Remediation Rules**

### ✔ Remove header‑grade metadata  
### ✔ Remove altitude declarations  
### ✔ Remove epoch declarations  
### ✔ Remove sealed state  
### ✔ Remove governance lanes  
### ✔ Remove operator activation  
### ✔ Restore correct provenance footer  
### ✔ Ensure directory placement matches altitude  

---

# 🌐 **6 — Reintegration Rules**

After correction, the artifact must be placed in:

```
research-pilot/substrates/citations/
```

or the appropriate A1–A4 directory.

Reintegration requires:

- corrected header  
- corrected footer  
- corrected lane  
- corrected altitude  
- corrected epoch  
- corrected provenance  

---

# 🧩 **7 — Deletion Rules (Formal)**  
Deletion is only permitted when:

- ordered by an **A6 governance ruling**,  
- the artifact is corrupted beyond recovery,  
- the artifact violates FO3 ethical invariants,  
- the artifact contains unsafe content,  
- the artifact contaminates A5–A7 lanes,  
- the artifact breaks provenance integrity.

Otherwise:

> **Deletion is forbidden.  
> Quarantine is mandatory.**

---

# 📜 **Provenance Footer (A4 Analytical)**

```
---
Provenance:
A4::Analytical::Corridor-Compliant::Non-Governance::Non-Activating
Role: NDH-QuarantineProtocol (Subsystem-Analytical)

Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: 06 August 2026 — 11:42 IST
---
```

---


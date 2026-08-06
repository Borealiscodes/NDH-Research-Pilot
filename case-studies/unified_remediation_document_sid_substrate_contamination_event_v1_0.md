# 🌌 **Unified Remediation Document — NDH Research‑Pilot Substrate SID Contamination Event (v1.0)**  
### *A4 Analytical Surface • Remediation Plan for 3 Quarantined Substrates*  
### *Citation Block v3.0 • Carlin Crossmap v1.0 • Suspended Substrate v1.0*

---

## ⭐ **0 — Purpose of This Document**

This Unified Remediation Document defines the **complete correction workflow** for the three Research‑Pilot artifacts contaminated by SID‑like header drift:

- **Merged Citation Block v3.0**  
- **Carlin Crossmap v1.0**  
- **Suspended Substrate v1.0**

It applies the **Quarantine Protocol** and prepares each artifact for safe reintegration into the Research‑Pilot substrate layer.

This is a **non‑binding**, **non‑governance**, **non‑operator**, **reversible** A4 analytical artifact.

---

# ⭐ **1 — Remediation Overview**

All three artifacts share the same contamination profile:

- header‑grade metadata  
- altitude declarations  
- epoch declarations  
- canonical snapshot fields  
- header‑grade provenance anchors  

Therefore, remediation is unified.

The remediation process has **five phases**:

1. **Header Removal**  
2. **Structural Correction**  
3. **Footer Restoration**  
4. **Lane & Directory Correction**  
5. **Reintegration**

---

# ⭐ **2 — Phase 1: Header Removal (Mandatory)**

Remove the entire header block from each artifact:

```
---
title:
artifact:
version:
altitude:
epoch:
lineage_type:
sealed:
canonical_snapshot:
provenance_anchors:
maintainer:
timestamp:
---
```

This block is forbidden at A2.

### ✔ Applies to all three artifacts  
### ✔ No exceptions  
### ✔ Must be fully removed

Guided link: **Header Safety Standard**

---

# ⭐ **3 — Phase 2: Structural Correction**

Each artifact must be corrected to remove:

- **altitude declarations**  
- **epoch declarations**  
- **canonical snapshot fields**  
- **sealed state**  
- **header‑grade provenance anchors**  

These fields belong only to A5–A7.

### ✔ Remove all altitude fields  
### ✔ Remove all epoch fields  
### ✔ Remove all canonical snapshot fields  
### ✔ Remove all sealed fields  
### ✔ Move provenance anchors to the footer

---

# ⭐ **4 — Phase 3: Footer Restoration**

Each artifact must retain a **Research‑Pilot footer**, not a governance footer.

Correct footer structure:

```
---
Artifact: <name>
Lane: NDH-Research-Pilot • Substrates • <domain>

Purpose:
<brief purpose>

Provenance Anchors:
  <anchors moved from header>

Version: <version>
Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: <timestamp>
---
```

### ✔ Provenance anchors belong in the footer  
### ✔ Footer must be A2‑appropriate  
### ✔ No altitude, epoch, or sealed fields in footer  

---

# ⭐ **5 — Phase 4: Lane & Directory Correction**

After remediation, each artifact must be placed in the correct Research‑Pilot substrate directory.

### **Merged Citation Block v3.0 → citations/**

```
research-pilot/substrates/citations/merged_citation_block_v3_0.md
```

### **Carlin Crossmap v1.0 → epistemic_geometry/**

```
research-pilot/substrates/epistemic_geometry/carlin_crossmap_v1_0.md
```

### **Suspended Substrate v1.0 → epistemic_geometry/**

```
research-pilot/substrates/epistemic_geometry/suspended_substrate_carlin_crossmap_v1_0.md
```

### ✔ No altitude declarations  
### ✔ No SID headers  
### ✔ No governance lanes  

---

# ⭐ **6 — Phase 5: Reintegration Workflow**

ASCII diagram:

```
[Quarantine]
     ↓
[Header Removal]
     ↓
[Structural Correction]
     ↓
[Footer Restoration]
     ↓
[Lane Correction]
     ↓
[Reintegration]
```

Reintegration requires:

- corrected header (removed)  
- corrected footer  
- corrected lane  
- corrected directory  
- corrected provenance  

Only then can the artifact return to active Research‑Pilot circulation.

---

# ⭐ **7 — Unified Remediation Checklist**

### ✔ Remove header block  
### ✔ Remove altitude  
### ✔ Remove epoch  
### ✔ Remove canonical snapshot  
### ✔ Remove sealed state  
### ✔ Move provenance anchors to footer  
### ✔ Restore correct A2 footer  
### ✔ Place in correct substrate directory  
### ✔ Confirm no SID‑like structures remain  

This checklist applies to all three artifacts.

---

# 📜 **Provenance Footer (A4 Analytical)**

```
---
Provenance:
A4::Analytical::Corridor-Compliant::Non-Governance::Non-Activating
Role: NDH-UnifiedRemediationDocument (Subsystem-Analytical)

Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: 06 August 2026 — 11:56 IST
---
```

---



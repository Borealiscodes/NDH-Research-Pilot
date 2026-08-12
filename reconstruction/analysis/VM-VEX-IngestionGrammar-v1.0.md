# 📘 **VM‑VEX‑IngestionGrammar‑v1.0.md**  
### *NDH‑RESEARCH‑PILOT • Reconstruction / Analysis Lane*  
### *Human‑Readable Version • ASCII Geometry • Icon Marker: 🜄*

---

# ⭐ 1 — Purpose  
The VM‑VEX Ingestion Grammar defines **how VM‑VEX interprets, validates, and ingests machine‑readable artifacts** during pre‑runtime sequencing.  
It ensures:

- altitude correctness  
- lane correctness  
- stability‑ecology compliance  
- recursion ceilings  
- bundle metadata validation  
- safe ingestion of JSON artifacts  

This grammar is **non‑activating** and **pre‑runtime only**.

---

# ⭐ 2 — Icon‑Based Phase Marker  
```
🜄 Phase 3 — VM‑VEX Internal Components
Component: Ingestion Grammar v1.0
```

---

# ⭐ 3 — ASCII Overview Diagram

```
+-----------------------------------------------------------+
|                VM-VEX INGESTION GRAMMAR v1.0              |
+----------------------+------------------------------------+
| Input               | Machine-readable JSON artifacts     |
+----------------------+------------------------------------+
| Validation          | Altitude, lane, stability flags     |
+----------------------+------------------------------------+
| Structural Rules    | Keys, types, recursion ceilings     |
+----------------------+------------------------------------+
| Safety Enforcement  | Non-activating, pre-runtime only    |
+----------------------+------------------------------------+
| Output              | Validated ingestion envelope        |
+-----------------------------------------------------------+
```

---

# ⭐ 4 — Grammar Structure

## 4.1 Accepted Artifact Types  
VM‑VEX accepts only:

- `.json` machine‑readable artifacts  
- structured key/value pairs  
- explicit booleans  
- explicit arrays  
- explicit altitude fields  
- explicit lane fields  

It rejects:

- prose  
- diagrams  
- icons  
- orbs  
- markdown  
- runtime code  

---

## 4.2 Required Top‑Level Keys  
Each ingestion artifact **must** contain:

```
version
artifact
altitude.min
altitude.max
permissions.lanes
permissions.forbidden
safety-flags
provenance
```

These keys form the **minimum ingestion envelope**.

---

## 4.3 Altitude Grammar  
Altitude must be expressed as:

```
A5, A6, A7
```

VM‑VEX rejects:

- ranges outside A5–A7  
- missing altitude fields  
- symbolic altitude (icons/orbs)  

---

## 4.4 Lane Grammar  
Valid lanes:

- `analysis`  
- `governance-adjacent`  
- `runtime-adjacent` (forbidden in Phase 🜄)  
- `runtime` (forbidden)  

---

## 4.5 Recursion Grammar  
VM‑VEX enforces:

```
max-depth: 3
max-recursion: 1
max-virtual-span: 12
```

These ceilings prevent:

- infinite descent  
- unstable ingestion  
- premature runtime adjacency  

---

## 4.6 Safety Flags  
Required flags:

```
non_activating: true
pre_runtime_only: true
no_gpu_binding: true
no_constellation_binding: true
stability_ecology_required: true
```

These flags ensure ingestion remains **safe**, **bounded**, and **non‑runtime**.

---

# ⭐ 5 — ASCII Grammar Block (Canonical)

```
GRAMMAR VM-VEX-INGESTION v1.0
-----------------------------------------
artifact := JSON
version := string
altitude := { min: A5|A6|A7, max: A5|A6|A7 }
permissions := { lanes: [...], forbidden: [...] }
runtime-envelope := { bounds, stability, ingestion }
safety-flags := { ... }
dependencies := { requires: [...], paired-human-readable: string }
provenance := { anchors: [...], maintainer: string, timestamp: string }
-----------------------------------------
END GRAMMAR
```

This block is the **human‑readable representation** of the ingestion grammar.

---

# ⭐ 6 — Determination  
> **VM‑VEX Ingestion Grammar v1.0 (human‑readable) is now complete.  
> The next step is generating the Machine Layer JSON version.**

---


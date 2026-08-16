# **Simulation Experiment Template (v1.0)**  
### *NDH‑RESEARCH‑PILOT • Simulation‑Altitude Experiment Template*

> This template defines the structure for all simulation‑altitude experiments conducted within NDH‑RESEARCH‑PILOT.  
> It is **not** part of the NDH‑SIMULATION‑SUITE engine and does **not** describe or modify the engine.  
> It provides a governance‑altitude scaffold for generating simulation‑safe derivatives.

---

## **1. Experiment Name**

```
<experiment_name> — Simulation Triad Experiment
```

Example:  
`goat_constitution_v2_1 — Simulation Triad Experiment`

---

## **2. Experiment Directory**

Place the experiment README here:

```
NDH-RESEARCH-PILOT/simulation-altitude/experiments/<experiment_name>/README.md
```

This directory contains **only governance‑altitude documentation**, not simulation artifacts.

---

## **3. Simulation‑Altitude Artifacts (inside NDH‑SIMULATION‑SUITE)**

Each experiment produces **four simulation‑safe derivatives**, placed inside the engine:

### **1 — Simulation Profile**
```
NDH-SIMULATION-SUITE/profiles/<experiment_name>_simulation_profile.json
```

### **2 — Behavioral Model**
```
NDH-SIMULATION-SUITE/behavioral_models/<experiment_name>_behavioral_model.json
```

### **3 — Drift Geometry Test**
```
NDH-SIMULATION-SUITE/drift_tests/<experiment_name>_drift_geometry_test.json
```

### **4 — Simulation Triad Index**
```
NDH-SIMULATION-SUITE/triad_index/<experiment_name>_simulation_triad_index.json
```

These four artifacts form the **complete S2‑altitude execution triad**.

---

## **4. README Structure (to be filled per experiment)**

Your experiment README should follow this structure:

### **Title**
```
<experiment_name> — Simulation Triad Experiment README (v1.x)
```

### **Sections**
1. **Purpose of This Experiment**  
   Describe why this governance artifact is being converted into simulation‑safe derivatives.

2. **Components of the Simulation Triad**  
   List the four simulation‑altitude artifacts with their actual paths.

3. **Triad Index**  
   Describe how the triad index binds the three derivatives.

4. **Altitude Clarification**  
   State that the README is A4 and the derivatives are S2.

5. **Membrane Purity Statement**  
   Affirm that no governance semantics enter S2.

6. **File Locations**  
   Provide literal filesystem paths.

7. **Non‑Activation Clause**  
   Affirm that the README does not activate NDH‑SIMULATION‑SUITE.

---

## **5. Template Variables**

Replace these placeholders:

- `<experiment_name>`  
- `<governance_artifact>`  
- `<version>`  
- `<timestamp>`  
- `<location>`  

---

## **6. Provenance Footer Template**

```
---
Artifact: <experiment_name> Simulation Triad Experiment README (v1.x)
Lane: NDH-RESEARCH-PILOT • Simulation-Altitude Experiments

Purpose:
  Document the experiment that produced the simulation-safe triad for
  <governance_artifact>. This README explains triad structure, altitude
  boundaries, membrane purity, lineage references, and experiment scope without
  entering or modifying the NDH-SIMULATION-SUITE engine.

Anchors:
  - <experiment_name> Simulation Profile (JSON)
  - <experiment_name> Behavioral Model (JSON)
  - <experiment_name> Drift Geometry Test (JSON)
  - <experiment_name> Simulation Triad Index (JSON)
  - NDH-SIMULATION-SUITE Clarifications Case Study v1.0
  - Low-Risk Primitives Expressive Clarity Methodology v1.0
  - NDH Geometry-Zen Omnibus v1.0
  - Translation Logic Lineage (TLL)

Non-Activation Clause:
  This README is descriptive-only. It does not activate, simulate, or bind any
  NDH subsystem, expressive geometry mechanism, holonomy operator, or altitude-
  routing process. It documents an experiment without executing NDH processes.

Version: v1.x
Maintainer: Borealis S. Hedling
Location: <location>
Timestamp: <timestamp>
---
```

---


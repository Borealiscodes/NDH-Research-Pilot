# 🌌 **Fractal Node Viewer v1.0**  
### *Schema‑Aligned • Read‑Only • A6–A8 Orientation Altitude*

```
Artifact-Class: Dashboard Module
Name: Fractal Node Viewer
Version: v1.0
Altitude Band: A6–A8 (RP-ALTITUDE)
Mode: Read-Only • Schema-Validated • Non-Activating

Purpose:
  Provide a developer-grade viewer for fractal nodes originating from
  NDH-Fractal-Adventure-Test. Render node structure, metadata, invariants,
  lineage, and telemetry in a drift-neutral, membrane-safe, non-activating
  orientation environment.
```

### **Viewer Capabilities**

- **index.md rendering** — show node overview  
- **spec.md rendering** — show invariants & guarantees  
- **metadata.yml rendering** — schema-validated  
- **examples/** — display example payloads  
- **telemetry.md** — show node telemetry  
- **lineage graph** — parent/child relationships  
- **altitude placement** — sandbox altitude alignment  
- **drift signature** — drift-neutrality check  

### **Machine Block**

```json
FractalNodeViewer_v1_0 = {
  "version": "1.0",
  "views": [
    "index_md",
    "spec_md",
    "metadata_yml",
    "examples",
    "telemetry_md"
  ],
  "validation": {
    "metadata_schema": "v1.0",
    "invariants_schema": "v1.0"
  },
  "lineage": "read_only_graph",
  "mode": "read_only",
  "non_activation": true
}
```

---

# 📜 **Provenance Footer — Fractal Node Viewer v1.0**

```
---
Artifact: Fractal Node Viewer (v1.0)
Lane: NDH-Research-Pilot • Dashboard • Orientation Layer
Altitude: A6–A8 • Read-Only • Schema-Validated • Drift-Neutral • Membrane-Safe

Purpose:
  Provide a developer-grade viewer for fractal nodes originating from
  NDH-Fractal-Adventure-Test. Render node structure, metadata, invariants,
  lineage, and telemetry in a drift-neutral, membrane-safe, non-activating
  orientation environment.

Anchors:
  - Fractal Sequencing Document v1.0
  - Fractal Meta-Construction Suite v0.1
  - Direction Manifold v4.0
  - Bridge Document v1.0
  - metadata.schema.json (v1.0)
  - invariants.schema.json (v1.0)

Non-Activation Clause:
  This module is strictly read-only. It does not activate NDH geometry,
  governance altitude, sealed-layer logic, constellation routing, or expressive
  runtime behavior. It provides orientation visualization only.

Version: v1.0
Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: 29 August 2026 — 20:25 IST
Seal: [ F R A C T A L • V I E W E R • S E A L E D ]
---
```

---


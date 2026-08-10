# 🌿 **PNG Rendering Guidelines (v1.0)**  
### *NDH‑Research‑Pilot • Non‑Activating • Renderer‑Ready*

---

## **1. Purpose**
Define a **safe, stable, non‑activating procedure** for rendering PNGs using:

- the Machine‑Readable Spec  
- the Hex Value Palette  
- the Renderer Mapping Table  
- the Rendering Pipeline Diagram  

These guidelines ensure:

- consistent PNG output  
- strict RP altitude  
- ASCII‑safe geometry  
- no routing semantics  
- no governance posture  

---

# **2. Renderer Inputs (Required)**

A renderer must load the following artifacts:

### **2.1 Machine‑Readable Spec v1.0**
Contains:

- palette identifiers  
- geometry identifiers  
- layer order  
- stability constraints  

### **2.2 Hex Value Palette v1.0**
Contains:

- conceptual identifier → hex value mappings  

### **2.3 Renderer Mapping Table v1.0**
Contains:

- identifier → hex → ASCII geometry → layer order  

These three artifacts form the complete renderer input set.

---

# **3. Rendering Sequence (Strict Order)**  
### *ASCII‑safe, non‑activating*

```
1. Load machine-readable spec
2. Load hex value palette
3. Load renderer mapping table
4. Initialize transparent background
5. Render layers in strict order (1 → 6)
6. Export PNG with alpha channel
```

### **Layer Order (from spec)**

```
1 → transparent_background
2 → meadow_substrate
3 → quantum_forest_undergrowth
4 → hexagon_constellation
5 → celestial_triad
6 → rainbow_enso_crown
```

This order must never be changed.

---

# **4. Layer Rendering Rules**

## **4.1 Layer 1 — Transparent Background**
- must remain fully transparent  
- no gradients  
- no framing bars  
- no governance cues  

## **4.2 Layer 2 — Meadow Substrate**
- use meadow palette hex values  
- apply soft, non‑directional texture  
- avoid terrain‑map patterns  

## **4.3 Layer 3 — Quantum Forest Undergrowth**
- use forest palette hex values  
- apply subtle woven texture  
- avoid branching or root‑routing semantics  

## **4.4 Layer 4 — Hexagon Constellation**
Allowed geometry:

```
○   ◇   @
```

Disallowed:

```
▲   →   ⇢   ✦
```

Rules:

- adjacency depth ≤ 2  
- opacity 40–70%  
- no subsystem adjacency patterns  

## **4.5 Layer 5 — Celestial Triad**
Symbols:

```
🌞   🌙   🌍
```

Rules:

- no orbit paths  
- no radiance lines  
- no directional crescents  

## **4.6 Layer 6 — Rainbow Enso Crown**
Gradient:

```
pastel_ember_red → peach_dawn → gentle_gold → mint_whisper → sky_drift_blue → lavender_haze
```

Rules:

- soft gradient only  
- no radiance  
- no crown posture  
- no halo implying authority  

---

# **5. Stability Enforcement**

Renderers must enforce:

```
no_routing: true
no_governance_geometry: true
no_subsystem_adjacency: true
max_hexagon_adjacency_depth: 2
no_radiance_lines: true
no_orbital_paths: true
```

These constraints come directly from the Machine‑Readable Spec.

---

# **6. PNG Export Rules**

### **6.1 Output Format**
- PNG  
- RGBA  
- transparent background  

### **6.2 Resolution**
Recommended:

```
512×512
1024×1024
2048×2048
```

### **6.3 Scaling**
- geometry must scale proportionally  
- no distortion  
- no directional stretching  

### **6.4 Compression**
- lossless  
- no palette reduction  

---

# **7. ASCII‑Safe Renderer Pseudocode (Non‑Activating)**

```
renderer.load_spec("emblem_machine_readable_spec_v1_0.json")
renderer.load_hex_palette("emblem_hex_value_palette_v1_0.md")
renderer.load_mapping_table("emblem_renderer_mapping_table_v1_0.md")

canvas = renderer.new_canvas(transparent=True)

for layer in [1,2,3,4,5,6]:
    renderer.render_layer(layer)

renderer.export_png("emblem.png")
```

This pseudocode contains **no routing semantics** and **no governance cues**.

---

# 🪶 **Provenance Footer — PNG Rendering Guidelines (v1.0)**

```
---
Artifact: PNG Rendering Guidelines (v1.0)
Scope: Defines safe, non-activating procedures for rendering PNGs within
NDH-Research-Pilot altitude.

Purpose:
  Provide renderer-ready instructions for layer sequencing, geometry safety,
  chromatic mapping, and PNG export rules.

Altitude:
  Strictly NDH-RESEARCH-PILOT. No adjacency to NDH-Constellation, NDH-Core,
  Blueprint governance, or operator routing layers.

Provenance Anchors:
  - RP_PNGRendingGuidelines_v1_0
  - RP_RendererMappingTable_v1_0
  - RP_HexValuePalette_v1_0
  - RP_MachineReadable_v1_0
  - RP_StabilityEnvelope_v1_0

Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: 10 August 2026 — 18:02 IST
---
```

---


# 🌿 **Renderer Mapping Table (v1.0)**  
### *NDH‑Research‑Pilot • Non‑Activating • Renderer‑Ready*

---

## **1. Purpose**
Provide a **single, unified mapping table** that connects:

- conceptual palette identifiers  
- hex values  
- geometry identifiers  
- layer order  

This table allows any renderer or script to:

- load the machine‑readable spec  
- apply the hex palette  
- follow the correct layer sequence  
- avoid activating geometry or routing semantics  

It is ASCII‑only and GitHub‑safe.

---

# **2. Color Identifier → Hex Value Mapping**

### **2.1 Pastel Rainbow Enso Gradient**

```
pastel_ember_red      → #F4A8A8
peach_dawn            → #F7C9A1
gentle_gold           → #E8D89A
mint_whisper          → #BEE8C4
sky_drift_blue        → #A9C9F2
lavender_haze         → #C9B7E8
```

### **2.2 Meadow & Quantum Forest**

```
soft_meadow_green     → #A8D5A2
moss_green            → #7FAF7C
sky_mist_blue         → #C7DCEB
earth_rooted_brown    → #A68C6D
dewdrop_silver        → #D9D9DD
```

### **2.3 Constellation Geometry Palette**

```
constellation_blue    → #8AA8C8
tessellation_green    → #9CC7A1
soft_gold             → #E6D7A8
pale_teal             → #A8D7D1
fog_grey              → #C8C8C8
```

### **2.4 Celestial Triad**

```
sun_gold              → #F2D37D
moon_silver           → #D8D8E0
earth_blue_green      → #7FB7A8
```

---

# **3. Geometry Identifier → ASCII Shape Mapping**

### **Allowed Geometry (Non‑Activating)**

```
circle                → ○
hexagon               → ◇
spiral                → @
```

### **Disallowed Geometry (Must Not Be Used)**

```
triangle              → ▲
arrow                 → →
radiance              → ✦
orbit_path            → (any curved directional arc)
```

These are excluded to avoid:

- routing semantics  
- governance posture  
- subsystem adjacency  
- activation cues  

---

# **4. Layer Identifier → Rendering Order Mapping**

### **Layer Order (Strict)**

```
1 → transparent_background
2 → meadow_substrate
3 → quantum_forest_undergrowth
4 → hexagon_constellation
5 → celestial_triad
6 → rainbow_enso_crown
```

### **Renderer Interpretation**

- **Layer 1**: always transparent  
- **Layer 2–3**: soft textures only  
- **Layer 4**: geometry (○ ◇ @ only)  
- **Layer 5**: 🌞 🌙 🌍 (no orbit paths)  
- **Layer 6**: pastel gradient (linear or circular, no radiance)  

---

# **5. Combined Renderer Mapping Table (v1.0)**  
### *Unified lookup structure*

```
renderer_mapping_table_v1_0 = {

  "colors": {
    "pastel_ember_red":    "#F4A8A8",
    "peach_dawn":          "#F7C9A1",
    "gentle_gold":         "#E8D89A",
    "mint_whisper":        "#BEE8C4",
    "sky_drift_blue":      "#A9C9F2",
    "lavender_haze":       "#C9B7E8",

    "soft_meadow_green":   "#A8D5A2",
    "moss_green":          "#7FAF7C",
    "sky_mist_blue":       "#C7DCEB",
    "earth_rooted_brown":  "#A68C6D",
    "dewdrop_silver":      "#D9D9DD",

    "constellation_blue":  "#8AA8C8",
    "tessellation_green":  "#9CC7A1",
    "soft_gold":           "#E6D7A8",
    "pale_teal":           "#A8D7D1",
    "fog_grey":            "#C8C8C8",

    "sun_gold":            "#F2D37D",
    "moon_silver":         "#D8D8E0",
    "earth_blue_green":    "#7FB7A8"
  },

  "geometry": {
    "circle":              "○",
    "hexagon":             "◇",
    "spiral":              "@"
  },

  "layers": {
    "1": "transparent_background",
    "2": "meadow_substrate",
    "3": "quantum_forest_undergrowth",
    "4": "hexagon_constellation",
    "5": "celestial_triad",
    "6": "rainbow_enso_crown"
  }
}
```

---

# 🪶 **Provenance Footer — Renderer Mapping Table (v1.0)**

```
---
Artifact: Renderer Mapping Table (v1.0)
Scope: Unified mapping table for renderer workflows within NDH-Research-Pilot
altitude.

Purpose:
  Provide stable lookup mappings for colors, geometry, and layer order to
  support PNG rendering and automated tooling.

Altitude:
  Strictly NDH-RESEARCH-PILOT. No adjacency to NDH-Constellation, NDH-Core,
  Blueprint governance, or operator routing layers.

Provenance Anchors:
  - RP_RendererMappingTable_v1_0
  - RP_HexValuePalette_v1_0
  - RP_MachineReadable_v1_0
  - RP_RendererSupportAddendum_v1_0
  - RP_StabilityEnvelope_v1_0

Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: 10 August 2026 — 17:55 IST
---
```

---


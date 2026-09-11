### ⭐ Series XII — Dual‑Mode Runtime Switch v1.0  
*NDH‑RESEARCH‑PILOT • Implementation Corridor (A3–A5) • Non‑Activating*

---

#### 1 — Identity block

```text
Artifact: Dual-Mode Runtime Switch
Version: v1.0
Lane: NDH-RESEARCH-PILOT
Altitude: A3–A5 (Implementation Corridor)
Mode: Runtime Control • Non-Activating
Purpose:
    Define the canonical structure and behavior of the NDH Dual-Mode Runtime
    Switch, binding the Manifold State Envelope to two distinct runtime modes:
    Stateful Mode and Cosmology Mode. Establish mode boundaries, persistence
    rules, continuity behavior, PRECL handling, and integration surfaces.
```

---

#### 2 — Conceptual overview

The Dual‑Mode Runtime Switch:

- selects between **stateful manifold runtime** and **cosmology engine runtime**  
- enforces **mode boundaries** and **behavioral invariants**  
- binds to the **Envelope Schema v1.0** (Series XII)  
- is the control surface that Series XI anticipated and Series XIII will implement in `.ts`.

Modes:

- **Stateful Mode** → physical continuity, persistence, reversible evolution  
- **Cosmology Mode** → simulated continuity, expressive holonomy, symbolic PRECL  

---

#### 3 — Switch schema (canonical)

```text
DualModeRuntimeSwitch {
    current_mode: RuntimeMode
    allowed_modes: Set<RuntimeMode>
    mode_rules: ModeRuleSet
    envelope_binding: EnvelopeBindingDescriptor
}
```

---

#### 4 — Runtime modes

```text
RuntimeMode {
    id: "stateful" | "cosmology"
    persistence: PersistenceProfile
    continuity: ContinuityProfile
    precl_behavior: PreclProfile
}
```

**Stateful mode**

```text
stateful_mode {
    id: "stateful"
    persistence: "full"
    continuity: "physical"
    precl_behavior: "accumulate"
}
```

**Cosmology mode**

```text
cosmology_mode {
    id: "cosmology"
    persistence: "none"
    continuity: "simulated"
    precl_behavior: "symbolic"
}
```

---

#### 5 — Mode rule set

```text
ModeRuleSet {
    transition_rules: TransitionRuleSet
    guardrails: ModeGuardrailSet
}
```

**Transition rules**

```text
transition_rules {
    allow: [
        "stateful -> cosmology",
        "cosmology -> stateful"
    ]
    constraints: [
        "no transition during critical emission",
        "no transition during unresolved PRECL collapse"
    ]
}
```

**Guardrails**

```text
mode_guardrails {
    stateful {
        requires_envelope: true
        requires_reversibility: true
        drift_neutrality: "strict"
    }
    cosmology {
        requires_envelope: true
        requires_reversibility: false
        drift_neutrality: "soft"
    }
}
```

---

#### 6 — Envelope binding descriptor

```text
EnvelopeBindingDescriptor {
    schema_ref: "series-XII-envelope-schema-v1_0"
    fields_bound: [
        "adjacency_field",
        "resonance_field",
        "flow_field",
        "holonomy_field",
        "density_field",
        "synthesis_field"
    ]
    buffers_bound: [
        "precl_buffer",
        "calm_load_accumulator"
    ]
}
```

---

#### 7 — Integration surfaces

```text
integration_surfaces {
    switch_module: runtime/modes/switch.ts
    stateful_runtime: runtime/modes/stateful/index.ts
    cosmology_runtime: runtime/modes/cosmology/index.ts
    envelope_adapter: runtime/envelope/mode_adapter.ts
}
```

---

#### 8 — Machine‑readable switch specification (v1.0)

```json
{
  "artifact": "series-XII-dual-mode-runtime-switch-v1_0",
  "version": "1.0",
  "altitude": "A3-A5",
  "mode": "non-activating",
  "modes": [
    {
      "id": "stateful",
      "persistence": "full",
      "continuity": "physical",
      "precl_behavior": "accumulate"
    },
    {
      "id": "cosmology",
      "persistence": "none",
      "continuity": "simulated",
      "precl_behavior": "symbolic"
    }
  ],
  "transition_rules": {
    "allow": [
      "stateful -> cosmology",
      "cosmology -> stateful"
    ],
    "constraints": [
      "no_transition_during_critical_emission",
      "no_transition_during_unresolved_precl_collapse"
    ]
  },
  "guardrails": {
    "stateful": {
      "requires_envelope": true,
      "requires_reversibility": true,
      "drift_neutrality": "strict"
    },
    "cosmology": {
      "requires_envelope": true,
      "requires_reversibility": false,
      "drift_neutrality": "soft"
    }
  },
  "envelope_binding": {
    "schema_ref": "series-XII-envelope-schema-v1_0",
    "fields_bound": [
      "adjacency_field",
      "resonance_field",
      "flow_field",
      "holonomy_field",
      "density_field",
      "synthesis_field"
    ],
    "buffers_bound": [
      "precl_buffer",
      "calm_load_accumulator"
    ]
  },
  "integration_surfaces": [
    "runtime/modes/switch.ts",
    "runtime/modes/stateful/index.ts",
    "runtime/modes/cosmology/index.ts",
    "runtime/envelope/mode_adapter.ts"
  ],
  "status": "pending"
}
```

---

### 🧾 Provenance footer

```text
---
Artifact-Class: Implementation Control (NDH-RESEARCH-PILOT)
Artifact-Name: series-XII-dual-mode-runtime-switch-v1_0
Surface: diagnostics/github-constellation-audit/
Version: v1.0
Altitude: A3–A5 Implementation Corridor
Membrane: Non-Activating • Control-Only

Purpose:
  Define the Dual-Mode Runtime Switch required to bind the Manifold State
  Envelope to both stateful and cosmology runtime modes. Establish mode
  boundaries, transition rules, guardrails, and envelope binding for NDH
  runtime stabilization and cosmology operation.

Anchors:
  - Series XII — Envelope Schema v1.0
  - Series XI — NDH Integration Roadmap (Diagnostic Edition)
  - Series XI — NDH Integration Roadmap (Developer Edition)
  - Series XI — NDH Integration Roadmap (Governance Edition)
  - Series IX — Manifold State Envelope Diagnostic
  - NDH Runtime README v2.0
  - Serenity-Spectral-Runtime README v3.0
  - Spectral-Base-Runtime v2.1

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 11 September 2026 — 23:10 IST
Seal: [ N D H • R E S E A R C H • P I L O T • S E R I E S • X I I • D U A L • v1_0 ]
---
```

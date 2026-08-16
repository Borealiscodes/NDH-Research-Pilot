# 🧩 **Goat Constitution v2.1 — Invariant Functions v1.0**

Below is the full invariant function set in clean pseudocode.  
You can port this directly into Python, TypeScript, Rust, or any language.

---

## ⭐ 1 — Structure Validation Invariants

### **HAS_TITLE**  
```
function HAS_TITLE(artifact):
    if artifact.title is a non-empty string:
        return pass
    else:
        return fail("Title missing or empty.")
```

### **HAS_SECTIONS**  
```
function HAS_SECTIONS(artifact):
    if artifact.sections exists and length > 0:
        return pass
    else:
        return fail("No sections defined.")
```

### **HAS_RULES**  
```
function HAS_RULES(artifact):
    if artifact.rules exists and length > 0:
        return pass
    else:
        return fail("No rules defined.")
```

---

## ⭐ 2 — Section Integrity Invariants

### **SECTIONS_NONEMPTY**  
```
function SECTIONS_NONEMPTY(artifact):
    for section in artifact.sections:
        if section.content is empty:
            return fail("Section '" + section.id + "' is empty.")
    return pass
```

### **SECTIONS_ORDERED**  
```
function SECTIONS_ORDERED(artifact):
    ids = [section.id for section in artifact.sections]
    if ids is strictly increasing:
        return pass
    else:
        return fail("Sections are not in valid order.")
```

### **SECTIONS_UNIQUE**  
```
function SECTIONS_UNIQUE(artifact):
    ids = [section.id for section in artifact.sections]
    if ids contains duplicates:
        return fail("Duplicate section identifiers detected.")
    return pass
```

---

## ⭐ 3 — Rule Consistency Invariants

### **RULES_NONEMPTY**  
```
function RULES_NONEMPTY(artifact):
    for rule in artifact.rules:
        if rule.text is empty:
            return fail("Rule '" + rule.id + "' is empty.")
    return pass
```

### **RULES_UNIQUE**  
```
function RULES_UNIQUE(artifact):
    ids = [rule.id for rule in artifact.rules]
    if ids contains duplicates:
        return fail("Duplicate rule identifiers detected.")
    return pass
```

### **NO_CONTRADICTIONS**  
```
function NO_CONTRADICTIONS(artifact):
    for each pair (ruleA, ruleB):
        if ruleA logically contradicts ruleB:
            return fail("Contradiction between '" + ruleA.id + "' and '" + ruleB.id + "'.")
    return pass
```

---

## ⭐ 4 — Math Validation Invariants

### **MATH_WELL_FORMED**  
```
function MATH_WELL_FORMED(artifact):
    for expression in artifact.math.expressions:
        if expression cannot be parsed:
            return fail("Malformed math expression: " + expression.raw)
    return pass
```

### **NO_ILLEGAL_REFERENCES**  
```
function NO_ILLEGAL_REFERENCES(artifact):
    allowed = artifact.math.allowed_symbols
    for expression in artifact.math.expressions:
        for symbol in expression.symbols:
            if symbol not in allowed:
                return fail("Illegal reference: " + symbol)
    return pass
```

---

## ⭐ 5 — Semantic Coherence Invariants

### **NO_AMBIGUOUS_LANGUAGE**  
```
function NO_AMBIGUOUS_LANGUAGE(artifact):
    ambiguous_terms = ["may", "possibly", "as needed", "reasonable", "appropriate"]
    for rule in artifact.rules:
        for term in ambiguous_terms:
            if term appears in rule.text:
                return fail("Ambiguous term '" + term + "' in rule '" + rule.id + "'.")
    return pass
```

### **NO_CIRCULAR_DEFINITIONS**  
```
function NO_CIRCULAR_DEFINITIONS(artifact):
    graph = buildDefinitionGraph(artifact.rules)
    if graph contains cycle:
        return fail("Circular definition detected.")
    return pass
```

---

## ⭐ 6 — Altitude Placement Invariant

### **PLACED_IN_GOVERNANCE_LANE**  
```
function PLACED_IN_GOVERNANCE_LANE(artifact):
    if artifact.metadata.lane == "governance":
        return pass
    else:
        return fail("Artifact not placed in governance lane.")
```

---

# 📜 **Provenance Footer — Goat Constitution v2.1 Invariant Functions v1.0**

```
---
Artifact: Goat Constitution v2.1 Invariant Functions v1.0
Lane: Validation • Constitution-Checking

Purpose:
  Provide the invariant function implementations for the Goat Constitution v2.1
  validation state machine. These functions define the logic used to evaluate
  structural, semantic, mathematical, and governance-lane correctness.

Attribution:
  This validator uses NDH-style ordered validation patterns but does not activate
  any NDH subsystem, altitude mechanism, or governance engine.

Anchors:
  State Machine Validator Template v1.0
  Goat Constitution v2.1 Validation Graph v1.0

Non-Activation Clause:
  These invariant functions are descriptive-only. They do not activate, execute,
  simulate, or bind any NDH subsystem, governance engine, expressive geometry,
  manifold traversal, or altitude-routing mechanism.

Version: v1.0
Maintainer: Borealis S. Hedling
Location: Naaldwijk, South Holland, Netherlands
Timestamp: 16 August 2026 — 17:12 IST
---
```

---


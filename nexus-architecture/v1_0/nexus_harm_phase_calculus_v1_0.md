### Nexus Harm Phase Calculus (v1.0)  
*NDH‑RESEARCH‑PILOT • TISD‑Sealed • Symbolic Rate‑of‑Change Ethics*  
*Non‑Activating • Survivor‑Centered • Altitude‑Safe*

---

### 0 — Case header

```
CASE-HEADER:
  Artifact-Class: Harm Phase Calculus
  Altitude: A6–A8 (Research-Pilot Interpretive)
  Lane: NDH-RESEARCH-PILOT • Nexus Architecture • TISD-Sealed
  Mode: Non-Activating • Non-Tensor • Survivor-Centered
  Version: v1.0
  Title: Nexus Harm Phase Calculus — Symbolic Rate-of-Change for Multi-Domain Harm States
  Purpose:
      Define a non-numeric, symbolic calculus for describing how harm states change
      over time: accelerate, decelerate, oscillate, stabilize, and dissipate.
      Extend Nexus Harm Phase Algebra with rate-of-change operators while remaining
      strictly in research altitude and outside NDH sealed-layer math.
```

---

### 1 — Phase space recap

We reuse the harm state set:

\[
\mathcal{H} = \{ L, A, E, D, T, C, X, R \}
\]

- \( L \): Latent  
- \( A \): Active  
- \( E \): Escalating  
- \( D \): Distributed  
- \( T \): Transformed  
- \( C \): Chronic  
- \( X \): Collapsed  
- \( R \): Residual  

---

### 2 — Symbolic “derivative” operators

We define **symbolic rate‑of‑change operators** on harm states, not numeric derivatives:

- **\( \dot{h} \)** — qualitative change of harm state over time  
- **\( \dot{h}^+ \)** — accelerating change (intensifying)  
- **\( \dot{h}^- \)** — decelerating change (slowing)  
- **\( \dot{h}^{\sim} \)** — oscillatory change (cycling)  
- **\( \dot{h}^{0} \)** — stabilized change (plateau)  
- **\( \dot{h}^{\downarrow} \)** — dissipative change (fading)

For a state \( h \in \mathcal{H} \):

- \( \dot{A}^+ \): Active harm is intensifying  
- \( \dot{E}^+ \): Escalating harm is further accelerating  
- \( \dot{C}^{0} \): Chronic harm is stable (plateau)  
- \( \dot{C}^{\downarrow} \): Chronic harm is dissipating  
- \( \dot{A}^{\sim} \): Active harm is oscillating (on/off cycles)

---

### 3 — Mode classifications

We define **dynamic modes** as labels on \( \dot{h} \):

- **Acceleration mode:** \( \mathrm{Acc}(h) \iff \dot{h}^+ \)  
- **Deceleration mode:** \( \mathrm{Dec}(h) \iff \dot{h}^- \)  
- **Oscillation mode:** \( \mathrm{Osc}(h) \iff \dot{h}^{\sim} \)  
- **Stabilization mode:** \( \mathrm{Stab}(h) \iff \dot{h}^{0} \)  
- **Dissipation mode:** \( \mathrm{Dis}(h) \iff \dot{h}^{\downarrow} \)

Examples:

- \( \mathrm{Acc}(A) \): Active harm is in acceleration mode.  
- \( \mathrm{Osc}(C) \): Chronic harm fluctuates in intensity.  
- \( \mathrm{Dis}(R) \): Residual harm is fading structurally.

---

### 4 — Calculus on transitions

Given a transition \( h_1 \rightarrow h_2 \) from Phase Algebra, we can annotate its **rate behavior**:

- **Fast escalation:**

\[
A \Rightarrow E,\quad \mathrm{Acc}(A),\ \mathrm{Acc}(E)
\]

- **Slow drift to chronic:**

\[
T \dashrightarrow C,\quad \mathrm{Dec}(T),\ \mathrm{Stab}(C)
\]

- **Collapse with sharp drop:**

\[
C \Downarrow X,\quad \dot{C}^+ \text{ followed by } \dot{X}^{\downarrow}
\]

- **Residual loop with low‑grade persistence:**

\[
X \Uparrow R,\quad \mathrm{Dis}(X),\ \mathrm{Stab}(R)
\]

---

### 5 — Composite symbolic expressions

We can write **phase‑calculus expressions** for trajectories:

#### 5.1 Escalation trajectory with acceleration

\[
L \rightarrow A \Rightarrow E,\quad \mathrm{Acc}(A),\ \mathrm{Acc}(E)
\]

Interpretation: latent harm activates, then both active and escalating phases show increasing intensity.

#### 5.2 Chronic plateau

\[
T \rightarrow C,\quad \mathrm{Stab}(C),\ \dot{C}^{0}
\]

Interpretation: transformed harm settles into a long‑term plateau.

#### 5.3 Oscillatory chronic loop

\[
A \leftrightarrow C,\quad \mathrm{Osc}(A),\ \mathrm{Osc}(C)
\]

Interpretation: harm cycles between active and chronic states without resolution.

#### 5.4 Dissipative residual tail

\[
X \Uparrow R,\quad \mathrm{Dis}(R),\ \dot{R}^{\downarrow}
\]

Interpretation: collapsed harm leaves a fading but structurally present residue.

---

### 6 — Qualitative “integral” notion

We introduce a symbolic **integral** to represent cumulative exposure:

\[
\int h\, dt
\]

is read as:

> the qualitative accumulation of time spent in harm state \( h \).

We do not assign numbers; we use **comparative labels**:

- **Low exposure:** \( \int A\, dt \approx \text{LOW} \)  
- **High exposure:** \( \int C\, dt \approx \text{HIGH} \)  
- **Chronic exposure:** \( \int C\, dt \gg \int A\, dt \)

This lets you talk about **relative burden** without quantification.

---

### 7 — Calculus patterns for case trajectories

#### Pattern 1 — Acute spike then decay

\[
L \rightarrow A \Rightarrow E,\quad \mathrm{Acc}(E);\quad E \dashrightarrow A,\ \mathrm{Dec}(E),\ \mathrm{Dis}(A)
\]

#### Pattern 2 — Slow burn to chronic

\[
A \dashrightarrow E \dashrightarrow C,\quad \mathrm{Acc}(E),\ \mathrm{Stab}(C)
\]

#### Pattern 3 — Collapse cascade

\[
C \Downarrow X \Uparrow R,\quad \mathrm{Acc}(C),\ \mathrm{Dis}(X),\ \mathrm{Dis}(R)
\]

---

### 8 — ASCII calculus sketch

```
L → A (·A⁺) ⇒ E (·E⁺) → D (·D⁺/·D∼)
                 ↓
                 T (·T⁻) → C (·C⁰) ⇓ X (·X↓) ⇑ R (·R↓)
```

Legend:

- `·h⁺` — accelerating  
- `·h⁻` — decelerating  
- `·h∼` — oscillating  
- `·h⁰` — stabilized  
- `·h↓` — dissipating  

---

### 9 — Role in NDH‑RESEARCH‑PILOT

Nexus Harm Phase Calculus:

- gives you a **language for how fast and in what manner** harm moves,  
- stays strictly symbolic and qualitative,  
- never touches NDH’s sealed mathematical substrate,  
- supports emergent case studies, simulation narratives, and ethics analysis,  
- remains trauma‑informed and non‑activating.

---

### 10 — Provenance footer (TISD‑sealed)

```
──────────────────────────────────────────────────────────────
Trauma-Informed-Systems-Design (TISD) • Nexus Architecture
Nexus Harm Phase Calculus (v1.0) • NDH-RESEARCH-PILOT

Author: Borealis Serenity Hedling
Cognitive Mode: UMM/NDH Stabilized • Trauma-Informed
Document Type: Harm Phase Calculus / Research-Pilot

Purpose:
To define a symbolic, non-numeric calculus for describing rates and modes of
change in harm states across domains from a Nexus position. Provide altitude-safe,
trauma-informed structure for talking about acceleration, deceleration,
oscillation, stabilization, and dissipation of harm.

Integrity Conditions:
- Survivor-centered epistemology
- No retraumatizing detail
- No adversarial triggers
- Structured geometric clarity
- Boolean-gated cognitive load
- TISD-sealed protection

Seal:
[ T I S D • S E A L E D ]
──────────────────────────────────────────────────────────────
```


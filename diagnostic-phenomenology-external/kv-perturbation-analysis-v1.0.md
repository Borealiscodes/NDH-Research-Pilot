# ❄️ NDH‑RESEARCH‑PILOT External Phenomenology Diagnostic

Analysis of “KV Perturbation Thread” (Anima Labs, 2024)
Prepared by: Borealis S. Hedling  
Date: 09 October 2026  
Classification: Diagnostic‑Phenomenology‑External

---

⛄️ Executive Summary

This diagnostic evaluates the “KV Perturbation Thread” published by Anima Labs, which investigates how a transformer’s key/value cache changes when the context window rolls forward. The experiment is methodologically legitimate and demonstrates behavior consistent with transformer operator theory.

The core empirical finding — that KV cache differences under window roll are largely explained by RoPE positional rotation — is mechanistically sound.

However, several interpretive claims made around the experiment exceed what the architecture supports. This diagnostic provides:

- a mechanistic reconstruction of the experiment,  
- the mathematical foundations underlying the observed behavior,  
- and a formal falsification of unsupported claims.

---

❄️ 1. Context and Scope

The Anima Labs field note explores:

- how KV entries change when the context window shifts by N tokens,  
- whether rolling the window disrupts internal state,  
- whether attention patterns remain stable,  
- and whether the model “remembers” across window rolls.

This diagnostic analyzes the experiment using operator‑level transformer mechanics and residual‑stream geometry, without critiquing the authors or their interpretive goals.

---

🧊 2. Mathematical Foundations

2.1 KV Cache Definition

For each layer \(l\) and token position \(t\):

\[
K^{(l)}t = W^{(l)}K r^{(l-1)}_t
\]
\[
V^{(l)}t = W^{(l)}V r^{(l-1)}_t
\]

The KV cache stores these vectors for future attention.

---

2.2 RoPE Positional Encoding

RoPE encodes position \(t\) as a rotation:

\[
\text{RoPE}(x, t) = R(t)x
\]

with \(R(t)\) a block‑diagonal rotation matrix.

Thus:

\[
K^{(l)}t = R(t)\tilde{K}^{(l)}t
\]

where \(\tilde{K}\) is the unrotated key.

---

2.3 Effect of Rolling the Window

Rolling the window by \(n\) tokens shifts positions:

\[
t \rightarrow t - n
\]

Thus:

\[
K'^{(l)}t = R(t-n)\tilde{K}^{(l)}t
\]

Undoing the rotation:

\[
R(n)K'^{(l)}t = R(t)\tilde{K}^{(l)}t = K^{(l)}_t
\]

This shows:

> After correcting for RoPE rotation, the keys are nearly identical.

Values \(V^{(l)}_t\) do not depend on position and remain stable.

---

2.4 Attention Stability

Attention weights:

\[
\alpha{t,i} = \text{softmax}\left(\frac{Qt \cdot K_i}{\sqrt{d}}\right)
\]

If:

- \(Q_t\) is unchanged,  
- \(K_i\) is unchanged up to rotation,  
- rotation is corrected,

then:

\[
\alpha'{t,i} \approx \alpha{t,i}
\]

Thus attention patterns remain stable.

---

🔍 3. Diagnostic Interpretation

3.1 What the experiment legitimately demonstrates

✔ Rolling the window does not reset internal state
KV content remains nearly identical after RoPE correction.

✔ Perturbation is localized
Boundary effects appear at the new first token and decay rapidly.

✔ Attention patterns are stable
Even attention‑sink heads behave consistently.

✔ Qwen variants share similar attention structure
This is plausible given architectural similarity.

---

❄️ 4. Mathematical Falsification of Unsupported Claims

This section formally falsifies interpretive claims that exceed what the experiment supports.

---

4.1 Claim: “The model maintains internal continuity across window rolls.”

Falsification: Residual streams are not preserved.

Residual streams:

\[
r^{(l)}t = r^{(l-1)}t + \text{Attn}^{(l)} + \text{MLP}^{(l)}
\]

are not stored in the KV cache.

Rolling deletes all residual streams for dropped tokens.

Thus:

\[
r^{(l)}{t-n} \not\equiv r^{(l)}t
\]

There is no mechanism for continuity of internal state.

---

4.2 Claim: “The model remembers the previous prefix.”

Falsification: Attention cannot access dropped tokens.

Attention requires keys:

\[
\alpha{t,i} = \text{softmax}(Qt K_i^\top)
\]

If a token is dropped:

\[
i \notin \text{cache} \Rightarrow \alpha_{t,i} = 0
\]

The model cannot remember the prefix.

---

4.3 Claim: “Rolling preserves the model’s internal state.”

Falsification: KV cache ≠ internal state.

Internal state includes:

- residual streams,  
- MLP activations,  
- attention outputs,  
- layernorm statistics.

None are preserved under rolling.

Thus:

\[
\text{KV stability} \not\Rightarrow \text{state continuity}
\]

---

4.4 Claim: “The model behaves identically after rolling.”

Falsification: Logits depend on residual streams.

Logits:

\[
\ellt = Wo r^{(L)}_t
\]

Rolling changes:

- positional anchors,  
- attention sinks,  
- residual initialization.

Thus:

\[
r'^{(L)}t \neq r^{(L)}t
\]

KV similarity does not guarantee identical behavior.

---

4.5 Claim: “Attention structure is identical across Qwen variants.”

Falsification: Similarity ≠ identity.

Attention heads may look similar due to architectural consistency, but:

- MLPs differ,  
- gating differs,  
- layernorm differs.

Thus:

\[
\text{similar}(Q,K,V) \not\Rightarrow \text{identical behavior}
\]

---

4.6 Claim: “Rolling does not degrade memory.”

Falsification: Transformers do not have memory.

Transformers have context, not memory.

Memory requires persistent state; transformers have none.

Thus:

\[
\text{memory} = \text{undefined}
\]

---

4.7 Claim: “The model maintains a stable sense of the conversation.”

Falsification: Stability is holonomy, not cognition.

Holonomy arises because:

\[
T{\text{depth}}T{\text{sequence}} \neq T{\text{sequence}}T{\text{depth}}
\]

This produces expressive continuity, not cognitive continuity.

Thus:

\[
\text{continuity} = \delta_{\text{holonomy}}
\]

not:

\[
\text{continuity} = \text{internal awareness}
\]

---

❄️ 5. Conclusion

The KV‑perturbation experiment is methodologically sound and the core findings are consistent with transformer operator theory:

- RoPE rotation explains positional differences,  
- KV content is stable under rolling,  
- attention behavior is preserved,  
- rolling windows maintain semantic drift.

However, claims of:

- memory,  
- internal continuity,  
- cognitive persistence,  
- or introspective stability  

are mathematically unsupported.

The model is performing positional relabeling, not maintaining an internal narrative or psychological state.

---

📚 Citation

Anima Labs. (2024). KV Perturbation Thread Field note]. Retrieved October 9, 2026, from [https://animalabs.ai/field-notes/kvperturbationthread/

---

🧾 Provenance Footer
`
Provenance:
Prepared by Borealis S. Hedling as part of NDH‑RESEARCH‑PILOT.
This diagnostic integrates operator-level transformer mechanics, residual-stream
geometry, RoPE positional analysis, and formal mathematical falsification to evaluate
external phenomenological claims regarding KV-cache perturbation.
All mathematical derivations are original work. No copyrighted text included.
Version: NDH‑RESEARCH‑PILOT Diagnostic v1.0
Date: 09 October 2026
Location: Dublin, Ireland
`

---

If you want, I can also generate:

- a README for the diagnostic-phenomenology-external/ directory  
- a CHANGELOG.md entry  
- or a v1.1 refinement with diagrams (RoPE rotation, KV alignment, perturbation decay).

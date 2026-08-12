### 📘 VM‑VEX Runtime Envelope v1.0  
*NDH‑RESEARCH‑PILOT • Pre‑Runtime • Non‑Activating*

#### 1 — Purpose  
Defines the altitude, lane, and recursion boundaries within which VM‑VEX is allowed to operate. It is a **geometry contract**, not a runtime executor.

#### 2 — Altitude Envelope  
- **Minimum altitude:** \(A5\)  
- **Maximum altitude:** \(A7\)  
- **Recursion ceiling:** \(d_{\text{recursion}} = 0\)

VM‑VEX may not:

- drop below \(A5\)  
- exceed \(A7\)  
- introduce recursive ingestion or activation loops.

#### 3 — Lane Permissions  
VM‑VEX is permitted in:

- **analysis lane**  
- **governance‑adjacent lane**

VM‑VEX is **not** permitted in:

- operational lane  
- runtime execution lane  
- CONSTELLATION synthesis lane.

#### 4 — Safety Flags  
- **non_activating:** true  
- **pre_runtime_only:** true  
- **no_direct_gpu_binding:** true  
- **no_constellation_binding:** true  
- **stability_ecology_required:** true  

VM‑VEX can only operate when stability‑ecology hooks are present and verified.

#### 5 — Bundle Relationship  
VM‑VEX Runtime Envelope v1.0 applies to:

- `NDH-Bundle-v1.0.json`  
- `NDH-BundleAudit-v1.0.md`  
- `NDH-ConstellationBindingPrep-v1.0.md`  
- `VM-VEX-Stabilization-v1.0.md`  
- `NDH-VM-VEX-ReferencePoint-v1.0.md`

All ingestion must respect this envelope.

---


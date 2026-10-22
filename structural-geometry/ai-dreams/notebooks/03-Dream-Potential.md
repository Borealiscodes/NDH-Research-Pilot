# 📓 03‑Dream‑Potential.md

Dream Potential Field Mapper — NDH‑RESEARCH‑PILOT

---

Purpose

This notebook explores the Dream Potential Field:

\[
\Phi(x) = \int \| S_{ij}(x) \|^2 \, dx
\]

The dream potential measures hallucination energy in the latent manifold.  
High \(\Phi\) regions correspond to:

- hallucination attractors  
- psychedelic wells  
- instability pockets  
- zones where the model “starts dreaming”  

This is the “where do hallucinations originate?” operator.

---

Conceptual Overview

The susceptibility tensor \(S_{ij}\) measures how sensitive the manifold is to perturbation.  
The dream potential \(\Phi(x)\) integrates this sensitivity into a scalar field.

Interpretation:

- Low \(\Phi\) → stable geometry  
- Medium \(\Phi\) → mild distortions  
- High \(\Phi\) → hallucination attractors, surreal transitions, dream‑like imagery  

This notebook computes and visualizes \(\Phi(x)\) across latent regions.

---

Setup

`python
import numpy as np
import matplotlib.pyplot as plt

from aidreamstoolkit import dream_potential
`

---

Construct or Load Susceptibility Tensor

You can load susceptibility from a model’s latent geometry or generate synthetic data.

`python

Example synthetic susceptibility tensor S_ij
susceptibility = np.random.randn(32, 32)
`

If you have model‑derived susceptibility, replace the synthetic tensor.

---

Compute Dream Potential

`python
Phi = dream_potential(susceptibility)
Phi
`

This scalar value represents the hallucination energy of the region.

---

Map Dream Potential Across Latent Space

To visualize hallucination attractors, compute \(\Phi\) across multiple regions.

`python
dream_map = np.zeros((32, 32))

for i in range(32):
    for j in range(32):
        S_local = np.random.randn(32, 32)
        dreammap[i, j] = dreampotential(S_local)
`

---

Visualize Hallucination Attractors

`python
plt.figure(figsize=(8, 6))
plt.imshow(dream_map, cmap='inferno')
plt.title("Dream Potential Field — Hallucination Attractors")
plt.colorbar()
plt.show()
`

Bright regions = high hallucination potential  
Dark regions = stable geometry

---

Optional: Compare Dream Potential Across Models

`python

Pseudocode — replace with your model loading logic

dreammapmodelA = computedreammap(modelA)

dreammapmodelB = computedreammap(modelB)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)

plt.imshow(dreammapmodelA, cmap='inferno')

plt.title("Model A — Dream Potential")

plt.subplot(1, 2, 2)

plt.imshow(dreammapmodelB, cmap='inferno')

plt.title("Model B — Dream Potential")
`

This reveals which architectures hallucinate more readily.

---

Interpretation

High dream potential indicates:

- strong susceptibility  
- unstable geometry  
- hallucination attractors  
- psychedelic wells  
- regions where AI dreams begin  

This operator is the geometric foundation of hallucination onset.

---

How to Run This Notebook in Jupyter

1. Save this file as:  
   03-Dream-Potential.md

2. Launch Jupyter:

`
jupyter lab
`

3. In Jupyter Lab:  
   - Right‑click the .md file  
   - Select “Open With → Markdown Notebook”  
   - Run the code cells normally

---

How to Run This Notebook in VS Code

1. Install the Python and Jupyter extensions  
2. Open the .md file  
3. Click the Run Cell buttons above each code block

---

How to Convert to .ipynb Later (Optional)

`
pip install jupytext
jupytext --to ipynb 03-Dream-Potential.md
`

This produces a clean .ipynb without JSON clutter.

---

Provenance

This notebook is part of the AI Dreams Geometry Lab, NDH‑RESEARCH‑PILOT.  
It explores dream potential as a geometric mechanism behind hallucination onset in generative models.

---


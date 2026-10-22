# 📓 01‑Hallucination‑Curvature.md

Hallucination Curvature Explorer — NDH‑RESEARCH‑PILOT

---

Purpose

This notebook explores the Hallucination Curvature Tensor:

\[
H{ijk} = \nablak R{ij} - \nablaj R_{ik}
\]

This tensor measures curvature asymmetry — the geometric source of:

- breathing textures  
- melting edges  
- asymmetric distortions  
- psychedelic warping  

This is the “why do the walls breathe?” operator.

---

Conceptual Overview

Latent manifolds in generative models are curved and anisotropic.  
When perturbations push the manifold into unstable regions, the Ricci curvature begins to change unevenly across directions.

The hallucination curvature tensor captures this directional imbalance.

High \(H_{ijk}\) → hallucination zones.

Low \(H_{ijk}\) → stable geometry.

---

Setup

`python
import numpy as np
import matplotlib.pyplot as plt

from aidreamstoolkit import hallucination_curvature
`

---

Load or Construct Ricci Curvature

You can load Ricci curvature from a model’s latent space, or construct a synthetic tensor for testing.

`python

Example synthetic Ricci tensor (replace with model-derived Ricci)
ricci = np.random.randn(32, 32)
`

---

Compute Hallucination Curvature

`python
H = hallucination_curvature(ricci)
H.shape
`

Expected shape: (32, 32, 32)  
(one gradient dimension added)

---

Visualize Curvature Asymmetry

`python
plt.figure(figsize=(8, 6))
plt.imshow(np.linalg.norm(H, axis=0), cmap='magma')
plt.title("Hallucination Curvature Magnitude")
plt.colorbar()
plt.show()
`

This heatmap shows where curvature asymmetry is strongest — the breathing zones.

---

Animate Curvature Evolution (Optional)

`python
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(6, 5))

def update(i):
    frame = np.linalg.norm(hallucination_curvature(ricci + 0.1*i), axis=0)
    ax.clear()
    ax.imshow(frame, cmap='magma')
    ax.set_title(f"Curvature Evolution — Step {i}")

ani = animation.FuncAnimation(fig, update, frames=20)
`

This animation shows curvature evolving under perturbation.

---

Interpretation

High curvature asymmetry indicates:

- unstable regions  
- hallucination attractors  
- melting boundaries  
- surreal distortions  

These are the geometric precursors to AI dreams.

---

How to Run This Notebook in Jupyter

1. Save this file as:  
   01-Hallucination-Curvature.md

2. Open a terminal:

`
jupyter lab
`

3. In Jupyter Lab:  
   - Right‑click the .md file  
   - Select “Open With → Markdown Notebook”  
   - Run the code cells normally

Jupyter treats fenced code blocks as runnable cells.

---

How to Run This Notebook in VS Code

1. Install the Python and Jupyter extensions  
2. Open the .md file  
3. VS Code will show Run Cell buttons above each code block  
4. Click to execute

VS Code treats fenced code blocks as notebook cells.

---

How to Convert to .ipynb Later (Optional)

If you ever want a real .ipynb:

`
pip install jupytext
jupytext --to ipynb 01-Hallucination-Curvature.md
`

This produces a clean, valid notebook without JSON hallucination.

---

Provenance

This notebook is part of the AI Dreams Geometry Lab, NDH‑RESEARCH‑PILOT.  
It explores hallucination curvature as a geometric mechanism behind dream‑like distortions in generative models.

---


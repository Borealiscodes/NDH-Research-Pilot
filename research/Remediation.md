Here is the exact remediation plan to close all four discrepancies from the Volume I consistency audit cleanly before running Pandoc.

1. Fix Interval Notation in Appendix E (appendices/appendix_e_holonomy_group.md)

Markdown stripped out [0, 1] because square brackets without a link target can get swallowed during formatting passes. Replace the broken Definition E.1 line with escaped brackets:
• Find:markdown
Let $\gamma : \to T^*\mathcal{M}$ be a closed trajectory loop in canonical position-momentum coordinates $(\mathbf{q}, \mathbf{p})$ bounding a two-dimensional surface $S$.
Use code with caution.
• Replace with:markdown
Let $\gamma : [0, 1] \to T^*\mathcal{M}$ be a closed trajectory loop in canonical position-momentum coordinates $(\mathbf{q}, \mathbf{p})$ bounding a two-dimensional surface $S$.
Use code with caution.

2. Fix Interval Notation in Appendix Q (appendices/appendix_q_causal_agency.md)

Restore the missing [0, 1] range for Directional Ownership in Definition Q.1:
• Find:markdown
The **Directional Ownership** score $\Omega_{\mathrm{dir}} \in$ blends directional cosine alignment (dominating small movements) with relative distance accuracy (dominating large movements).
Use code with caution.
• Replace with:markdown
The **Directional Ownership** score $\Omega_{\mathrm{dir}} \in [0, 1]$ blends directional cosine alignment (dominating small movements) with relative distance accuracy (dominating large movements).
Use code with caution.

3. Add Clickable Appendix Anchors and BibTeX Keys in volume1.md

Replace the plain italicized appendix callouts in Parts I–IV of volume1.md with clickable Pandoc section links ([Appendix X](#app-...)) and inline [@...] citations so --citeproc resolves every reference in the main text:
• Section 1.1:
	• Change (see *Appendix A: Residual Manifold Definition*) to (see [Appendix A](#app-manifold) [@bronstein2021geometric; @adacore2026spark]).
• Section 1.2:
	• Change (see *Appendix D: Spectral Structure*) to (see [Appendix D](#app-spectral) [@anonymous2026geometry]).
• Section 1.3:
	• Change (see *Appendix F: Curvature Evolution*) to (see [Appendix F](#app-curvature)).
• Section 2.1:
	• Change (see *Appendix E: Holonomy Group*) to (see [Appendix E](#app-holonomy) [@earn2001exact]).
• Section 2.2:
	• Change (see *Appendix B: Non-Integrable Foliation*) to (see [Appendix B](#app-foliation) [@anonymous2026geometry]).
• Section 2.3:
	• Change (see *Appendix C: Stability and Lyapunov Analysis*) to (see [Appendix C](#app-stability)).
• Section 3.1:
	• Change (see *Appendix H: Discrete Lattice Geometries*) to (see [Appendix H](#app-lattices)).
• Section 3.2:
	• Append [@barrett2024smt] after (Base243_Bijection.v).
• Section 3.3:
	• Change (see *Appendix J: Rational Invariants*) to (see [Appendix J](#app-rational) [@earn2001exact]).
• Section 4.1:
	• Change (see *Appendix P: Refinement Functors*) to (see [Appendix P](#app-refinement)).
• Section 4.2:
	• Change (see *Appendix Q: Causal Agency*) to (see [Appendix Q](#app-causa) [@stell2026causa]).

4. Final Verification Pass

Once those patches are applied, run the local Pandoc build check to confirm zero warnings and clean PDF generation:
bash
cd research/monographs/volume1 && make
Use code with caution.
With the Volume I remediation plan ready to patch cleanly:
• Would you like me to output the complete patched volume1.md with all clickable anchors and [@...] citations already applied?
• Or are you ready to drop in that new 8b-is specimen for forensic inspection?

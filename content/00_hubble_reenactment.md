# 00 Hubble Re-enactment: Answers and Discussion Points

## A. Cepheid Calibration Systematic (Leavitt Ladder Context)

Using the default notebook setting $ \Delta\mu = -0.30 $ mag:

- **Biased** $H_0 \approx 87.93$ km/s/Mpc  
- **Corrected** $H_0 \approx 76.58$ km/s/Mpc  
- **Shift** $ \approx +14.8\% $

### Why this happens

If a Cepheid zero-point error makes all distances too small, then the slope $v/d$ is too large, so $H_0$ is overestimated.

The scaling is:

$$
d_{\text{assumed}} = d_{\text{true}}\,10^{\Delta\mu/5}
$$

So a negative $\Delta\mu$ shrinks all distances and pushes $H_0$ up.

### Discussion points

- A single calibration offset affects *every* host distance coherently.  
- This is why distance-ladder systematics are dangerous: they produce global bias, not just extra scatter.  
- Leavitt's period-luminosity relation is foundational because its zero-point propagates directly to $H_0$.

---

## B. Fit-Choice Interpretation (Through-Origin vs Free-Intercept)

For the full sample (no host dropped):

- Through-origin fit $v = H_0 d$:  
  - $H_0 \approx 76.58$ km/s/Mpc
- Free-intercept fit $v = H_0 d + b$:  
  - $H_0 \approx 76.13$ km/s/Mpc  
  - $b \approx 6.70$ km/s
- RMS residuals are very similar ($\sim 253$ km/s), so both are consistent for this dataset.

### Physical meaning of the two fits

- **Through-origin** enforces the idealized Hubble law at $d=0$.  
- **Free-intercept** allows small offsets from local flows, calibration mismatch, or sample-selection effects.

### Stability discussion (example host drops)

- Dropping **NGC1326A**: through-origin $H_0$ shifts to $\sim 74.33$ (noticeable downward move).  
- Dropping **NGC4414**: through-origin $H_0$ shifts to $\sim 79.88$ (noticeable upward move).  

This shows that with a small sample, a few high-leverage hosts can move the inferred slope.

### Discussion points

- In small-$N$ low-$z$ samples, model choice and leverage points both matter.  
- A free intercept is often useful as a diagnostic, even if theory suggests near-origin behavior.  
- Robustness checks (drop-one tests) should be reported, not hidden.

---

## C. Historical Interpretation (3-5 Sentences)

Leavitt's period-luminosity relation turned Cepheids into standard candles, making extragalactic distances measurable. Hubble's velocity-distance plot depends critically on those distances, so its slope is only as reliable as the ladder calibration underneath it. In that sense, the famous $v$-$d$ diagram is the visible endpoint of deeper calibration work. The relation discovered by Leavitt therefore underpins modern estimates of $H_0$, even when Cepheids are not the final plotted points themselves.

### Discussion points

- "Hubble's law" is not just a line fit; it is a calibrated measurement chain.  
- The ladder concept links stellar astrophysics directly to cosmology.  
- Historical credit matters: Leavitt's work is central, not peripheral.

---

## Optional Extension

At higher redshift, replace $v \approx H_0 d$ with a luminosity-distance model:

$$
d_L(z; \Omega_m, \Omega_\Lambda)
$$

and fit cosmological parameters directly (or fit $H_0$ jointly with a fixed background cosmology).

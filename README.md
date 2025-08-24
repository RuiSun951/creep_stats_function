# Creep Stats Functions

some math functions for fine tuning creeps stats in a custom game (dota 2 vampire survivor style)

- creep attack damage
- creep attack speed
- creep hp
- creep armour
- creep magic resistance
- creep damage reduction

---

## attack damage function

We provide a single closed-form function that:

- **Exactly hits endpoints:** \(f(0)=2\), \(f(120)=20000\)  
- **Is smooth and monotone**  
- **Feels linear in the middle**, with adjustable “ease” at the ends

It’s built by normalizing a logistic (sigmoid) curve to the target range, then **blending** it with a straight line to reduce “over-easing.”

---

Let \(\sigma(z)=\dfrac{1}{1+e^{-z}}\) (logistic), and define:

- Domain: \(x \in [0,120]\)  
- Range: \([y_{\min},y_{\max}] = [2,20000]\)  
- Center \(c=60\) (midpoint), steepness \(a>0\) (default \(a=0.15\))  
- Blend \(\alpha \in [0,1]\) (default \(\alpha=0.4\); lower = more linear)

**Linear baseline**  
\[
L(x)=y_{\min}+\frac{y_{\max}-y_{\min}}{120}\,x
\]

**Normalized logistic that hits endpoints exactly**  
\[
G(x)=y_{\min}+(y_{\max}-y_{\min})\;
\frac{\sigma\!\big(a(x-c)\big)-\sigma\!\big(a(0-c)\big)}
{\sigma\!\big(a(120-c)\big)-\sigma\!\big(a(0-c)\big)}
\]

**Final blended function**  
\[
\boxed{\,F(x)=(1-\alpha)\,L(x)+\alpha\,G(x)\,}
\]
This keeps \(F(0)=2\) and \(F(120)=20000\), is smooth, and has controllable ease.

---

### Tuning Guide

- **Make ends steeper (less easing):** decrease `alpha` (e.g., 0.25)  
- **Make middle steeper (more S-curve):** increase `a` (e.g., 0.2–0.3)  
- **Make the middle flatter/longer:** decrease `a` (e.g., 0.1)  
- **Shift where the curve is most linear:** change `c` (center), e.g., `c=70`

Suggested starting points:
- Gentle ease: `a=0.12, alpha=0.3`
- Balanced: `a=0.15, alpha=0.4` (default)
- Punchier center: `a=0.22, alpha=0.5`

---

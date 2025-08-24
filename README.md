# Creep Stats Functions

Some math functions for fine-tuning creep stats in a custom game (Dota-2 / Vampire-Survivor style):

- [Attack Damage](#attack-damage-function)
- [Attack Speed](#attack-speed-function)
- [HP](#hp-function)
- [Armour](#armour-function)
- [Magic Resistance](#magic-resistance-function)
- [Damage Reduction](#damage-reduction-function)
- [Gold] (#creep-kill-gold-function)
- [Exp] (#creep-kill-exp-function)

---

## Attack Damage Function

We use a normalized logistic (sigmoid) blended with a straight line so it’s smooth, monotone,
**exactly hits** the endpoints, and feels nearly linear around the middle.

- Domain: $x\in[0,120]$  
- Range: $[y_{\min},y_{\max}] = [2,20000]$  
- Center $c=60$ (midpoint), steepness $a>0$ (default $a=0.15$)  
- Blend $\alpha\in[0,1]$ (default $\alpha=0.4$; lower $\Rightarrow$ more linear)

### Linear baseline
$$
L(x)=y_{\min}+\frac{y_{\max}-y_{\min}}{120}\cdot x
$$

### Normalized logistic that hits endpoints exactly
$$
G(x)=y_{\min}+(y_{\max}-y_{\min})\cdot
\frac{\sigma\big(a(x-c)\big)-\sigma\big(a(0-c)\big)}
{\sigma\big(a(120-c)\big)-\sigma\big(a(0-c)\big)}
\qquad \sigma(z)=\frac{1}{1+e^{-z}}
$$

### Final blended function
$$
F(x)=(1-\alpha)\cdot L(x)+\alpha\cdot G(x)
$$

This guarantees **exact endpoints**: $F(0)=2$ and $F(120)=20000$, with controllable easing.

---
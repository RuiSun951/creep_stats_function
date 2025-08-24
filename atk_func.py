# Re-run after state reset

import numpy as np
import matplotlib.pyplot as plt

y_min, y_max = 2.0, 20000.0
x_min, x_max = 0.0, 120.0

def L(x):
    return y_min + (y_max - y_min) * ( (x - x_min) / (x_max - x_min) )

def sigma(z):
    return 1.0 / (1.0 + np.exp(-z))

c = 60.0
a = 0.15
L_min = sigma(a*(x_min - c))
L_max = sigma(a*(x_max - c))

def G(x):
    num = sigma(a*(x - c)) - L_min
    den = L_max - L_min
    return y_min + (y_max - y_min) * (num / den)

alpha = 0.4

def F(x, alpha=alpha):
    return (1 - alpha)*L(x) + alpha*G(x)

xs = np.linspace(x_min, x_max, 800)
ys_blend = F(xs, alpha=alpha)
ys_pure  = G(xs)

plt.figure(figsize=(9,5))
plt.plot(xs, ys_blend, label=f"Blended (alpha={alpha})")
plt.plot(xs, ys_pure, linestyle="--", label="Pure logistic (alpha=1)")
plt.title("Reduced Ease: Blending Toward Linear (Domain [0,120], Range [2,20000])")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

def deriv_numeric(f, x, h=1e-3):
    return (f(x+h) - f(x-h)) / (2*h)

for name, func in [("Linear L", L), ("Pure logistic G", G), (f"Blended F (alpha={alpha})", F)]:
    print(name)
    print("  f(0)   =", float(func(0.0)))
    print("  f(60)  =", float(func(60.0)))
    print("  f(120) =", float(func(120.0)))
    print("  slopes: f'(0)≈", float(deriv_numeric(func, 0.0)),
          ", f'(60)≈", float(deriv_numeric(func, 60.0)),
          ", f'(120)≈", float(deriv_numeric(func, 120.0)))
    print()

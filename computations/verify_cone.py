"""Exact integer checks for Plucker cone dimension, equation counts, discrepancy.

This checks numerical implications of algebraic proofs, not the proofs themselves.
"""
from math import comb

for n in range(2, 20):
    m = n + 1
    ambient = comb(m, 2)
    dimension = 2 * m - 3
    codim = ambient - dimension
    equations = comb(m, 4) if m >= 4 else 0
    assert codim == (n - 1) * (n - 2) // 2
    assert equations == (0 if n == 2 else comb(n + 1, 4))
    assert (equations > codim) == (n >= 4)
    assert dimension == 2 * n - 1
    assert m - 1 == n
    print(f"n={n:2d}: ambient={ambient:3d}, cone={dimension:3d}, "
          f"codim={codim:3d}, Plucker quadrics={equations:4d}, "
          f"vertex-blowup discrepancy={n}")
print("All finite integer checks passed; geometric claims require the paper's arguments.")

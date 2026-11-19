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

# Sign quotients: exact Hilbert-function checks independent of geometry.
from itertools import combinations_with_replacement
from math import factorial
import sympy as s

m = s.symbols('m', integer=True, positive=True)
n = s.symbols('n', integer=True, positive=True)
N1 = n * (n + 1) / 2
H41 = n * (n + 1) * (n + 2) * (n + 3) / 24
Q1 = N1 * (N1 + 1) / 2 - H41
assert s.expand(Q1 - (N1 - n) - n*(n-1)*(n-2)*(n+3)/12) == 0
N2 = m*m*(m*m-1)/12
H42 = (m-1)*m*m*(m+1)**2*(m+2)**2*(m+3)/2880
Q2 = N2*(N2+1)/2-H42
assert s.expand(Q2-N2-N2*(m-3)*(m+2)*(9*m*m+m+22)/240) == 0

def tableaux_dimension(rank, k):
    rows = list(combinations_with_replacement(range(rank), k))
    return sum(all(a < b for a, b in zip(top, bottom))
               for top in rows for bottom in rows)

def grassmann_dimension(rank, k):
    return (factorial(rank+k-1)*factorial(rank+k-2)//
            (factorial(rank-1)*factorial(rank-2)*factorial(k)*factorial(k+1)))

for rank in range(3, 9):
    dims = {k: tableaux_dimension(rank, k) for k in (2, 4)}
    for k in dims:
        assert dims[k] == grassmann_dimension(rank, k)
    ambient = dims[2]
    quadrics = ambient*(ambient+1)//2-dims[4]
    assert quadrics > ambient-(2*rank-3)
    print(f'm={rank}: tableau dimensions h2={dims[2]}, h4={dims[4]}, '
          f'quadratic relations={quadrics}, codimension={ambient-(2*rank-3)}')
print('Symbolic factorization and independent tableau-count checks passed.')

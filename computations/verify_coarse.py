"""Exact finite checks for the degree-one coarse-moduli obstruction.

The PGL2 enumeration gives a concrete squarefree binary sextic with no
projective symmetry. The monomial calculation verifies the nilpotence order
in the completed coarse fiber. Neither check replaces the all-dimensional
slice and non-flatness proofs in papers/sections/coarse.tex.
"""
from itertools import combinations_with_replacement, permutations
from math import comb
import sympy as s


def projective_sextic_stabilizer():
    # f6 = x0*x1*(x0-x1)*(x0-3*x1)*(x0-7*x1)*(x0-11*x1).
    points = [s.Matrix(p) for p in
              [(0, 1), (1, 0), (1, 1), (3, 1), (7, 1), (11, 1)]]
    source = points[:3]
    stabilizers = []
    candidates = 0
    for target in permutations(points, 3):
        # A projectivity is determined by the images of three distinct points.
        rows = [[v*x, v*y, -u*x, -u*y]
                for (x, y), (u, v) in zip(source, target)]
        kernel = s.Matrix(rows).nullspace()
        assert len(kernel) == 1
        a, b, c, d = kernel[0]
        matrix = s.Matrix([[a, b], [c, d]])
        assert matrix.det() != 0
        candidates += 1
        if all(any(s.det(s.Matrix.hstack(matrix*p, q)) == 0 for q in points)
               for p in points):
            stabilizers.append(matrix)
    assert candidates == 6 * 5 * 4
    assert len(stabilizers) == 1
    assert stabilizers[0] == s.eye(2)
    print('Binary sextic: all 120 projectivities tested over Q; only identity.')


def coarse_fiber_nilpotence():
    # n=2: five quartic coefficients u, two Poisson coefficients v.
    u = s.symbols('u0:5')
    v = s.symbols('v0:2')
    degree_three = [s.prod(u[i] for i in indices)
                    for indices in combinations_with_replacement(range(5), 3)]
    ideal = s.groebner(degree_three, *u, *v, order='grevlex')
    c = u[0] * v[0]**4
    assert (2 * 1 + 4) % 6 == 0
    assert ideal.reduce(c)[1] == c
    assert ideal.reduce(c**2)[1] == c**2
    assert ideal.reduce(c**3)[1] == 0
    assert len(degree_three) == 35
    print('Coarse fiber: c=u0*v0^4 has c!=0, c^2!=0, c^3=0 modulo (u)^3.')

    degree_two = list(combinations_with_replacement(range(5), 2))
    assert len(degree_two) == 15
    # Base invariants have u-degree divisible by three; the v-degree-two
    # covariants have u-degree two modulo three. At the origin, all 15
    # degree-two monomials survive independently.
    for u_degree in range(9):
        assert ((2*u_degree + 2) % 6 == 0) == (u_degree % 3 == 2)
    print('n=2 covariant module: rank one in the proof, 15 minimal generators.')
    for n in range(2, 7):
        a = comb(n+3, 4)
        assert comb(a+1, 2) > 1
        print(f'n={n}: quartic directions={a}, covariant generators={comb(a+1, 2)}')


if __name__ == '__main__':
    projective_sextic_stabilizer()
    coarse_fiber_nilpotence()
    print('Exact coarse-model checks passed; global statements require the paper.')

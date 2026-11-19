#!/usr/bin/env python3
"""Exact checks for the family and descent formulas in poisson-del-pezzo.tex.

These are independent symbolic checks of the pushforward of the polynomial
bivector, not a proof of base change or quotient-stack representability.
All equation and bivector coefficients remain indeterminates.  The coordinate
changes are specified non-diagonal rational matrices, not random samples.
"""

from itertools import combinations, combinations_with_replacement
import json

import sympy as sp


def homogeneous(xs, degree, prefix):
    terms = combinations_with_replacement(range(len(xs)), degree)
    return sum(sp.Symbol(f"{prefix}{j}") * sp.prod(xs[i] for i in term)
               for j, term in enumerate(terms))


def zero(expr, label):
    if sp.expand(expr) != 0:
        raise AssertionError(label)


def zero_matrix(matrix, label):
    for i, j in combinations(range(matrix.rows), 2):
        zero(matrix[i, j], f"{label}: ({i},{j})")


def bivector_one(xs, y, z, f, direction):
    m = len(xs)
    b = sp.zeros(m + 2)
    for i in range(m):
        b[i, m] = sp.diff(f, z) * direction[i]
        b[m, i] = -b[i, m]
        b[m + 1, i] = sp.diff(f, y) * direction[i]
        b[i, m + 1] = -b[m + 1, i]
    b[m, m + 1] = sum(direction[i] * sp.diff(f, xs[i]) for i in range(m))
    b[m + 1, m] = -b[m, m + 1]
    return b


def bivector_two(xs, z, f4, p):
    m = len(xs)
    b = sp.zeros(m + 1)
    v = p * sp.Matrix([sp.diff(f4, x) for x in xs])
    b[:m, :m] = 2 * z * p
    for i in range(m):
        b[i, m] = v[i]
        b[m, i] = -v[i]
    return b


def degree_one_covariance():
    xs = sp.symbols("x0:2")
    y, z = sp.symbols("y z")
    a4, a6 = homogeneous(xs, 4, "a"), homogeneous(xs, 6, "c")
    f = z**2 - y**3 - a4*y - a6
    d = sp.Matrix(sp.symbols("d0:2"))
    a = sp.Matrix([[1, 1], [1, 2]])
    t = sp.Integer(2)
    inverse_x = dict(zip(xs, a.inv() * sp.Matrix(xs)))
    inverse = {**inverse_x, y: y/t**2, z: z/t**3}
    target_f = z**2 - y**3 - t**4*a4.xreplace(inverse_x)*y - t**6*a6.xreplace(inverse_x)
    zero(t**6 * f.xreplace(inverse) - target_f, "d1 equation transform")
    jac = sp.diag(a, t**2, t**3)
    source = bivector_one(xs, y, z, f, d).xreplace(inverse)
    pushed = jac * source * jac.T
    target = bivector_one(xs, y, z, target_f, a*d/t)
    zero_matrix(pushed - target, "d1 tensor covariance")
    deck = sp.diag(1, 1, 1, -1)
    original = bivector_one(xs, y, z, f, d)
    zero_matrix(deck*original.xreplace({z: -z})*deck.T + original, "d1 deck sign")
    lam = sp.Symbol("lambda", nonzero=True)
    assert (lam*sp.eye(2))*d/lam == d
    return {"n": 2, "generic_equation": True, "non_diagonal_change": True,
            "tensor_character": "t^(-1) A D", "deck_sign": -1,
            "central_weighted_scalars_trivial": True}


def degree_two_covariance():
    xs = sp.symbols("x0:4")
    z = sp.Symbol("z")
    f4 = homogeneous(xs, 4, "f")
    p = sp.zeros(4)
    for i, j in combinations(range(4), 2):
        p[i, j] = sp.Symbol(f"p{i}{j}")
        p[j, i] = -p[i, j]
    a = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0],
                   [0, 0, 1, 1], [0, 0, 0, 1]])
    b = sp.Integer(3)
    inverse_x = dict(zip(xs, a.inv() * sp.Matrix(xs)))
    inverse = {**inverse_x, z: z/b}
    target_f4 = b**2 * f4.xreplace(inverse_x)
    target_p = a*p*a.T/b
    jac = sp.diag(a, b)
    original = bivector_two(xs, z, f4, p)
    pushed = jac * original.xreplace(inverse) * jac.T
    target = bivector_two(xs, z, target_f4, target_p)
    zero_matrix(pushed - target, "d2 tensor covariance")
    deck = sp.diag(1, 1, 1, 1, -1)
    zero_matrix(deck*original.xreplace({z: -z})*deck.T + original, "d2 deck sign")
    lam = sp.Symbol("lambda", nonzero=True)
    zero_matrix((lam*sp.eye(4))*p*(lam*sp.eye(4)).T/lam**2-p,
                "d2 central weighted scalar")
    q = lambda v: v[0, 1]*v[2, 3]-v[0, 2]*v[1, 3]+v[0, 3]*v[1, 2]
    zero(q(target_p)-a.det()*q(p)/b**2, "d2 Plucker covariance")
    return {"n": 3, "generic_equation": True, "non_diagonal_change": True,
            "tensor_character": "b^(-1) wedge^2(A) P", "deck_sign": -1,
            "central_weighted_scalars_trivial": True,
            "plucker_covariance": True}


def moving_equation_obstruction():
    # The gradient symbols allow an arbitrary first-order change of the quartic.
    epsilon = sp.Symbol("epsilon")
    g = sp.symbols("g0:4")
    h = sp.symbols("h0:4")
    p = sp.zeros(4)
    q = sp.zeros(4)
    r = sp.zeros(4)
    for i, j in combinations(range(4), 2):
        q[i, j] = sp.Symbol(f"q{i}{j}")
        r[i, j] = sp.Symbol(f"r{i}{j}")
        q[j, i], r[j, i] = -q[i, j], -r[i, j]
        p[i, j] = epsilon*q[i, j] + epsilon**2*r[i, j]
        p[j, i] = -p[i, j]
    pfaff = lambda a: a[0, 1]*a[2, 3]-a[0, 2]*a[1, 3]+a[0, 3]*a[1, 2]
    for ell in range(4):
        jacobi_coefficient = 2*pfaff(p)*(g[ell]+epsilon*h[ell])
        remainder = sp.rem(sp.expand(jacobi_coefficient), epsilon**3, epsilon)
        zero(remainder-2*epsilon**2*pfaff(q)*g[ell], "moving-equation obstruction")
    return {"modulus": "epsilon^3", "arbitrary_first_order_equation_change": True,
            "second_order_bivector_correction_cannot_cancel_obstruction": True}


if __name__ == "__main__":
    print(json.dumps({"degree_one_covariance": degree_one_covariance(),
                      "degree_two_covariance": degree_two_covariance(),
                      "moving_equation_obstruction": moving_equation_obstruction(),
                      "arithmetic": "exact symbolic polynomials over Q",
                      "scope": "covariance and obstruction formulas; not a substitute for sheaf/stack proofs"},
                     indent=2, ensure_ascii=False))

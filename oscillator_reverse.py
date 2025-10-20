"""Compute the initial conditions of a harmonic oscillator from a later state."""
import math
from typing import Tuple


def solve_harmonic_origin(
    omega: float, t_now: float, x_now: float, v_now: float
) -> Tuple[float, float]:
    """Return (x_origin, v_origin) for a harmonic oscillator.

    The oscillator obeys d²x/dt² + ω² x = 0 with general solution
    x(t) = A cos(ω t) + B sin(ω t).
    """

    if omega == 0:
        raise ValueError("omega must be non-zero for a harmonic oscillator")

    cos_term = math.cos(omega * t_now)
    sin_term = math.sin(omega * t_now)

    A = cos_term * x_now - (sin_term * v_now) / omega
    B = sin_term * x_now + (cos_term * v_now) / omega

    x_origin = A
    v_origin = omega * B
    return x_origin, v_origin


if __name__ == "__main__":
    omega = 1.0
    t_now = 10.0
    x_now = 0.5
    v_now = 0.3

    x_origin, v_origin = solve_harmonic_origin(omega, t_now, x_now, v_now)
    print(f"Origin position: {x_origin}, velocity: {v_origin}")
